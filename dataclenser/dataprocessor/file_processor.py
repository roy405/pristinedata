import pandas as pd
from io import BytesIO
import numpy as np
from .conversionscript import Conversion

def process_csv_in_chunks(file_buffer, chunk_size=5000):
    text_stream = BytesIO(file_buffer.read())
    processed_chunks = []
    all_types = {}  # To store detected types for all columns
    for chunk in pd.read_csv(text_stream, chunksize=chunk_size):
        chunk_processed, chunk_types = Conversion.detect_and_convert(chunk)  # Adjusted to receive types
        all_types.update(chunk_types)  # Assuming later chunks can't introduce new types
        processed_chunks.append(chunk_processed)
    df = pd.concat(processed_chunks, ignore_index=True)
    return generate_response(df, all_types)  # Adjusted to pass types

def process_xlsx(file_buffer):
    binary_stream = BytesIO(file_buffer.read())
    df = pd.read_excel(binary_stream, engine='openpyxl')
    df, data_types = Conversion.detect_and_convert(df)  # Adjusted to receive types
    return generate_response(df, data_types)  # Adjusted to pass types

def generate_response(df, data_types):
    # Format datetime columns to Australian date format with 24-hour time.
    for col in df.columns:
        if pd.api.types.is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.strftime('%d/%m/%Y %H:%M:%S').str.replace(' 00:00:00', '')

    # Handle infinity and NaN
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.fillna('NaN', inplace=True)  # Convert NaN to 'NaN' string
    try:
        response_data = {
            "message": "Processed file successfully.",
            "data": df.to_dict(orient='records'),
            "columns": df.columns.tolist(),
            "types": data_types  # Include the data types in the response
        }
        return response_data
    except Exception as e:
        raise


