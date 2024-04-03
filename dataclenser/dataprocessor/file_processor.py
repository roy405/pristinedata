import pandas as pd
from .conversionscript import Conversion

def process_csv_in_chunks(file_path, chunk_size=5000):
    """
    Process a CSV file in chunks for efficient memory usage.
    Each chunk is processed through the Conversion class for data type adjustments.
    """
    processed_chunks = []  # List to hold processed chunks

    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        # Apply data type conversions to each chunk
        chunk_processed = Conversion.convert_dataframe(chunk)
        processed_chunks.append(chunk_processed)

    # Concatenate all processed chunks back into a single DataFrame
    df = pd.concat(processed_chunks, ignore_index=True)
    
    # Additional whole DataFrame processing can go here
    
    return {"message": f"Processed CSV file successfully. Row count: {len(df)}"}

def process_xlsx(file_path):
    """
    Read the Excel file and process it through the Conversion class for data type adjustments.
    Note: Excel files are not processed in chunks due to limitations with the pd.read_excel method.
    """
    df = pd.read_excel(file_path, engine='openpyxl')
    df = Conversion.convert_dataframe(df)  # Correct method call
    
    # Additional whole DataFrame processing can go here
    
    return {"message": f"Processed Excel file successfully. Row count: {len(df)}"}



