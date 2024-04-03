import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseBadRequest
# Import the custom FileSerializer class from the serializers.py file located in the current directory (.)
from .serializer import FileSerializer
# Import the CSV and XLSX specific processing functions.
from .dataprocessor.file_processor import process_csv_in_chunks, process_xlsx

class FileUploadView(APIView):
    def postReq(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            uploaded_file = request.FILES.get('file')
            file_name = uploaded_file.name
            # Save the uploaded file temporarily
            temp_file_path = os.path.join('temp', file_name)  # Specify your temp directory path
            with open(temp_file_path, 'wb+') as temp_file:
                for chunk in uploaded_file.chunks():
                    temp_file.write(chunk)
            
            # Process the file based on its type
            if file_name.endswith('.csv'):
                result = process_csv_in_chunks(temp_file_path)
            elif file_name.endswith('.xlsx'):
                result = process_xlsx(temp_file_path)
            else:
                return HttpResponseBadRequest("Unsupported file format. Please upload either .csv or .xlsx file.")
            
            # Clean up: remove the temporary file after processing
            os.remove(temp_file_path)
            
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
