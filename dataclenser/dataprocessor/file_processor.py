import pandas as pd
from .conversionscript import Conversion

def process_csv(file):
    # Read the CSV file
    df = pd.read_csv(file)
    df = Conversion.conver.dataframe(df)
    return {"message": f"Processed CSV file successfully. Row count: {len(df)}"}

def process_xlsx(file):
    # Read the Excel file
    df = pd.read_excel(file, engine='openpyxl')
    df = Conversion.conver.dataframe(df)
    return {"message": f"Processed Excel file successfully. Row count: {len(df)}"}


