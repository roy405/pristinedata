# Importing the serializers module from Django REST Framework (DRF).
# DRF serializers facilitate the conversion of complex data types (such as querysets and model instances)
# to and from native Python datatypes, supporting easy rendering to JSON, XML, etc., while ensuring data validation.
from rest_framework import serializers

# Declaring a FileField to handle file uploads. 
# FileField in DRF corresponds to Django's FileUpload objects, enabling file uploads with built-in validations 
# and constraints (like file size or type restrictions).
class FileSerializer(serializers.Serializer):
    file = serializers.FileField()