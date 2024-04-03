import pandas as pd

def process_csv(file):
    # Read the CSV file
    df = pd.read_csv(file)

    return {"message": f"Processed CSV file successfully. Row count: {len(df)}"}

def process_xlsx(file):
    # Read the Excel file
    df = pd.read_excel(file, engine='openpyxl')

    return {"message": f"Processed Excel file successfully. Row count: {len(df)}"}


