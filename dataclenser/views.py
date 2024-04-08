import os
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseBadRequest
# Import the custom FileSerializer class from the serializers.py file located in the current directory (.)
from .serializer import FileSerializer
# Import the CSV and XLSX specific processing functions.
from .dataprocessor.file_processor import process_csv_in_chunks, process_xlsx

class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        # Check if the deserialized data is valid.
        if file_serializer.is_valid():
            # Extract the file from the validated data.
            uploaded_file = request.FILES.get('file')
            # Get the file name to determine its type.
            file_name = uploaded_file.name
            try:
                if file_name.endswith('.csv'):
                    result = process_csv_in_chunks(uploaded_file)
                elif file_name.endswith('.xlsx'):
                    result = process_xlsx(uploaded_file)
                else:
                    return HttpResponseBadRequest("Unsupported file format. Please upload either .csv or .xlsx file.")
                return Response(result, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            # Return an error response if the input data failed validation.
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
