import pandas as pd
import numpy as np
from dateutil import parser
import re

class Conversion:
    @staticmethod
    def detect_and_convert(df):
        type_tags = {}
        for column in df.columns:
            initial_datatype = df[column].dtype
            # Boolean conversion
            if Conversion.is_boolean_column(df[column]):
                df[column], type_tag = Conversion.convert_boolean(df[column])
            # Numeric conversion
            elif Conversion.is_mostly_numeric(df[column]):
                df[column], type_tag = Conversion.convert_numeric(df[column])
            # Datetime conversion
            elif Conversion.is_datetime_column(df[column]):
                df[column], type_tag = Conversion.convert_datetime(df[column])
            # Complex conversion
            elif Conversion.is_complex_column(df[column]):
                df[column], type_tag = Conversion.convert_complex(df[column])
            # Text or Category conversion
            else:
                df[column], type_tag = Conversion.convert_text_or_category(df[column])
            type_tags[column] = type_tag
        return df, type_tags

    @staticmethod
    def is_mostly_numeric(series):
        numeric = pd.to_numeric(series, errors='coerce')
        return numeric.notna().mean() > 0.5

    @staticmethod
    def convert_numeric(series):
        numeric = pd.to_numeric(series, errors='coerce')
        if (numeric % 1 == 0).all():
            return numeric.fillna(0).astype(int), 'Int'
        else:
            return numeric.fillna(0), 'Float'

    @staticmethod
    def is_datetime_column(series):
        # Try to parse each date in the series using dateutil.parser.parse
        date_detected = series.apply(lambda x: Conversion.try_parse_date(x))
        return date_detected.mean() > 0.5  # Consider it a date column if most values are dates

    @staticmethod
    def try_parse_date(x):
        try:
            if pd.isnull(x):
                return False  # Treat null values as non-dates
            parser.parse(str(x))
            return True  # Successfully parsed as date
        except ValueError:
            return False  # Failed to parse as date

    @staticmethod
    def convert_datetime(series):
        # Use apply with dateutil.parser.parse for conversion to ensure compatibility with various formats
        def to_date(x):
            try:
                return parser.parse(str(x)).strftime('%d/%m/%Y') if not pd.isnull(x) else ''
            except ValueError:
                return ''  # Return an empty string for unparseable values

        converted = series.apply(to_date)
        return converted, 'Date'

    @staticmethod
    def is_boolean_column(series):
        # Improved detection for boolean values
        booleans = series.dropna().apply(lambda x: str(x).strip().lower()).isin(['true', 'false', '1', '0'])
        boolean_ratio = booleans.mean()
        return boolean_ratio > 0.5


    def convert_boolean(series):
        # Function to convert values to Boolean
        def to_boolean(value):
            if str(value).strip().lower() in ['true', '1']:
                return True
            elif str(value).strip().lower() in ['false', '0']:
                return False
            else:
                return np.nan  # or use None

        converted_series = series.apply(to_boolean)
        return converted_series, 'Boolean'
    
    @staticmethod
    def to_boolean(value):
        value_str = str(value).strip().lower()
        if value_str in ['true', '1']:
            return True
        elif value_str in ['false', '0']:
            return False
        return np.nan  # or however you wish to handle non-boolean values

    @staticmethod
    def is_complex_column(series):
        complex_regex = r'^[+-]?(\d+(\.\d+)?|\.\d+)([+-]\d+(\.\d+)?|\.\d+)?j$'
        return series.dropna().apply(lambda x: bool(re.match(complex_regex, str(x)))).mean() > 0.5

    @staticmethod
    def convert_complex(series):
        complex_regex = r'^[+-]?(\d+(\.\d+)?|\.\d+)([+-]\d+(\.\d+)?|\.\d+)?j$'
        return series.apply(lambda x: str(x) if bool(re.match(complex_regex, str(x))) else '').fillna(''), 'Complex'

    @staticmethod
    def convert_text_or_category(series):
        # Convert NaN values to empty strings before any other processing
        series = series.fillna('')

        # Now proceed with your original logic to determine if the series should be categorized
        if series.nunique(dropna=True) / len(series.dropna()) < 0.1:
            converted = series.astype('category')
            type_tag = 'Category'
        else:
            converted = series.astype(str)
            type_tag = 'Text'
        return converted, type_tag









