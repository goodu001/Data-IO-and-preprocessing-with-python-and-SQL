import pandas as pd

def convert_datetime_column(dataframe, column_name, year):
    
    # Check if the column is already in datetime format
    if not pd.api.types.is_datetime64_any_dtype(dataframe[column_name]):
        
        # Combine the year with the date strings in the specified column
        dataframe[column_name] = dataframe[column_name] + f" {year}"
        
        # Convert the combined string to datetime format
        dataframe[column_name] = pd.to_datetime(dataframe[column_name], format='%B %d %Y')
    
    return dataframe