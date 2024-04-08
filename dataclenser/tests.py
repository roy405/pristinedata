from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient
from .dataprocessor.file_processor import process_csv_in_chunks
from .serializer import FileSerializer
from unittest.mock import patch, MagicMock
from dateutil.parser import parse
import time
import pandas as pd
import numpy as np
from .dataprocessor.conversionscript import Conversion
from rest_framework.test import APITestCase
from .serializer import FileSerializer
from io import BytesIO
import os

class FileUploadTests(APITestCase):
    def test_file_upload_csv_success(self):
        """
        Ensure a CSV file can be uploaded successfully.
        """
        url = reverse('file-upload')  # Use the name of your URL pattern for file upload
        path_to_file = 'E:\RombusAI\\venv\\pristinedata\\dataclenser\\csvfiles\\file.csv' #filepath
        with open(path_to_file, 'rb') as fp:
            data = {'file': SimpleUploadedFile(fp.name, fp.read(), content_type='text/csv')}
            response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('message', response.data)
        self.assertEqual(response.data['message'], 'Processed file successfully.')

    def test_unsupported_file_format(self):
        """
        Test uploading an unsupported file format.
        """
        url = reverse('file-upload')
        data = {'file': SimpleUploadedFile('test.txt', b'Hello, world!', content_type='text/plain')}
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class ProcessCsvInChunksTests(TestCase):
    @patch('dataclenser.dataprocessor.conversionscript.Conversion.detect_and_convert')
    def test_process_csv_in_chunks(self, mock_detect_and_convert):
        processed_chunk = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'Score': [90, 75]
        })
        types_dict = {'Name': 'Text', 'Score': 'Numeric'}
        mock_detect_and_convert.return_value = (processed_chunk, types_dict)
        csv_content = b'Name,Score\nAlice,90\nBob,75\n'
        file_like_object = BytesIO(csv_content)
        result = process_csv_in_chunks(file_like_object)
        mock_detect_and_convert.assert_called()
        self.assertIn('data', result)
        self.assertEqual(len(result['data']), 2)

class PerformanceTests(TestCase):
    def test_csv_processing_performance(self):
        # Create a file-like object
        csv_content = b'Name,Score\nAlice,90\nBob,75\n'
        file_like_object = BytesIO(csv_content)
        start_time = time.time()
        # Pass the file-like object instead of a file path
        process_csv_in_chunks(file_like_object)
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 10)  # Assert the processing takes less than 10 seconds

class ConversionTests(TestCase):
    def test_boolean_conversion(self):
        series = pd.Series(['True', 'False', 'True', '1', '0', 'False'])
        converted_series, type_tag = Conversion.convert_boolean(series)
        # Note the dtype change to bool here
        expected_result = pd.Series([True, False, True, True, False, False], dtype=bool)
        pd.testing.assert_series_equal(converted_series, expected_result)
        self.assertEqual(type_tag, 'Boolean')


    def test_complex_conversion(self):
        series = pd.Series(['1+2j', '3+4j', '5+6j', '', 'not complex'])
        converted_series, type_tag = Conversion.convert_complex(series)
        self.assertTrue(all([a == b for a, b in zip(converted_series, ['1+2j', '3+4j', '5+6j', '', ''])]))
        self.assertEqual(type_tag, 'Complex')
    
    def test_datetime_conversion(self):
        series = pd.Series(['2020-01-01', '2021-02-02', '', 'not a date', '2022-03-03'])
        converted_series, type_tag = Conversion.convert_datetime(series)
        # Check if the non-date string and empty string are handled properly, and others are converted
        expected_dates = ['01/01/2020', '02/02/2021', '', '', '03/03/2022']
        self.assertTrue(all([a == b for a, b in zip(converted_series, expected_dates)]))
        self.assertEqual(type_tag, 'Date')

        # Optionally, you can also check if valid dates are parsed correctly
        valid_parsed_dates = [parse(date) for date in converted_series if date]
        self.assertTrue(all([date.strftime('%d/%m/%Y') == expected for date, expected in zip(valid_parsed_dates, expected_dates) if expected]))

    def test_numeric_conversion_float(self):
        series = pd.Series(['1.5', '2.5', '3.0', 'nan', '4.2'])
        converted_series, type_tag = Conversion.convert_numeric(series)
        expected_result = pd.Series([1.5, 2.5, 3.0, 0.0, 4.2], dtype='float')
        pd.testing.assert_series_equal(converted_series, expected_result)
        self.assertEqual(type_tag, 'Float')

    def test_numeric_conversion_int(self):
        series = pd.Series(['1', '2', '3', '4', '5'])
        converted_series, type_tag = Conversion.convert_numeric(series)
        expected_result = pd.Series([1, 2, 3, 4, 5], dtype='int')
        pd.testing.assert_series_equal(converted_series, expected_result)
        self.assertEqual(type_tag, 'Int')

    def test_text_conversion(self):
        series = pd.Series(['text1', 'text2', 'text3', '', 'text5'])
        converted_series, type_tag = Conversion.convert_text_or_category(series)
        self.assertTrue(all([a == b for a, b in zip(converted_series, ['text1', 'text2', 'text3', '', 'text5'])]))
        self.assertEqual(type_tag, 'Text')

    def test_category_conversion(self):
        # Include an initial NaN value to test its conversion to an empty string
        series = pd.Series(['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'A', np.nan])
        converted_series, type_tag = Conversion.convert_text_or_category(series)
        self.assertTrue(isinstance(converted_series.dtype, pd.CategoricalDtype) or isinstance(converted_series.dtype, pd.StringDtype))
        # Additional check to ensure NaN was replaced and categorized or kept as text
        self.assertTrue('' in converted_series.values or converted_series.isna().sum() == 0)
        self.assertIn(type_tag, ['Category', 'Text'])


   