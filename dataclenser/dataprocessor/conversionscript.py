import pandas as pd
import numpy as np

class Conversion:
    
    @staticmethod
    def convert_dataframe(df):
        """
        Convert the entire DataFrame by iterating through each column.
        """
        for column in df.columns:
            df[column] = Conversion.convert_column(df, column)
        return df

    @staticmethod
    def convert_column(df, column):
        """
        Convert the data type of a DataFrame column based on its content.
        """
        try:
            if pd.api.types.is_object_dtype(df[column]):
                df[column] = Conversion.infer_object_column_type(df[column])

            if pd.api.types.is_integer_dtype(df[column]):
                df[column] = Conversion.optimize_integer_type(df[column])
            elif pd.api.types.is_float_dtype(df[column]):
                df[column] = df[column]  # Keeping as float to preserve data integrity
            elif pd.api.types.is_datetime64_any_dtype(df[column]):
                pass  # Already in an optimal format
            elif pd.api.types.is_string_dtype(df[column]):
                df[column] = Conversion.convert_to_category_if_applicable(df, column)
            # Handle boolean, complex, and timedelta explicitly if needed
        except Exception as e:
            print(f"Error converting column {column}: {e}")
        return df[column]

    @staticmethod
    def infer_object_column_type(series):
        """
        Infer and convert an object column to a more specific type, prioritizing floats, datetimes, and strings.
        """
        try:
            series_converted = pd.to_datetime(series, errors='coerce')
            if not series_converted.isnull().all():
                return series_converted

            series_converted = pd.to_numeric(series, errors='coerce')
            if not series_converted.isnull().all():
                return series_converted.astype(float)

            return series.astype(str)
        except Exception as e:
            print(f"Error inferring object column type: {e}")
            return series

    @staticmethod
    def optimize_integer_type(series):
        """
        Downcast integers to the smallest possible type to save memory.
        """
        try:
            return pd.to_numeric(series, downcast='integer')
        except Exception as e:
            print(f"Error optimizing integer type: {e}")
            return series

    @staticmethod
    def convert_to_category_if_applicable(df, column):
        """
        Convert string columns to 'category' dtype for memory efficiency.
        """
        try:
            unique_ratio = df[column].nunique() / len(df)
            if unique_ratio < 0.1:
                return df[column].astype('category')
            return df[column]
        except Exception as e:
            print(f"Error converting to category: {e}")
            return df[column]

    @staticmethod
    def convert_to_bool(series):
        """
        Convert strings representing boolean values to actual booleans.
        """
        try:
            return series.replace({'true': True, 'false': False, 'True': True, 'False': False}).astype(bool)
        except Exception as e:
            print(f"Error converting to bool: {e}")
            return series

    @staticmethod
    def convert_to_complex(series):
        """
        Attempt to convert strings to complex numbers.
        """
        try:
            return series.apply(lambda x: complex(x) if isinstance(x, str) else x)
        except Exception as e:
            print(f"Error converting to complex: {e}")
            return series

    @staticmethod
    def convert_to_timedelta(series):
        """
        Convert strings or numeric values to timedelta.
        """
        try:
            return pd.to_timedelta(series)
        except Exception as e:
            print(f"Error converting to timedelta: {e}")
            return series
