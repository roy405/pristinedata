from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseBadRequest
# Import the custom FileSerializer class from the serializers.py file located in the current directory (.)
from .serializer import FileSerializer
# Import the CSV and XLSX specific processing functions.
from .dataprocessor.file_processor import process_csv, process_xlsx

class FileUploadView(APIView):
    # POST request handler
    def postReq(self, request, *args, **kwargs):
        # Deserialize the incoming data to a Python data type and validate it.
        file_serializer = FileSerializer(data=request.data)
        # Check if the deserialized data is valid.
        if file_serializer.is_valid():
            # Extract the file from the validated data.
            uploaded_file = request.FILES.get('file')
            # Get the file name to determine its type.
            file_name = uploaded_file.name
            # Route to the appropriate processing function based on the file extension.
            if file_name.endswith('.csv'):
                # Process .csv file
                result = process_csv(uploaded_file)
            elif file_name.endswith('.xlsx'):
                # Process .xlsx (MSExcel) file
                result = process_xlsx(uploaded_file)
            else:
                # Return an error response if the file format is unsupported.
                return HttpResponseBadRequest("Unsupported file format.")
            # Return a success response with the result of processing.
            return Response(result, status=status.HTTP_201_CREATED)
        else:
            # Return an error response if the input data failed validation.
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
