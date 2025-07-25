import pandas as pd
from datetime import datetime

def convert_to_datetime(date_text, year):
    """
    Converts a text date like "January 3" and a year into a datetime object.
    
    Parameters:
    date_text (str): Text date in format like "January 3", "February 14", etc.
    year (int): The year to use for the date
    
    Returns:
    datetime: A datetime object representing the date
    """
    # Combine the date text with the year
    full_date_text = f"{date_text}, {year}"
    
    # Convert to datetime object
    try:
        # This format handles dates like "January 3, 2030"
        return datetime.strptime(full_date_text, "%B %d, %Y")
    except ValueError:
        try:
            # This handles dates like "Jan 3, 2030" with abbreviated month names
            return datetime.strptime(full_date_text, "%b %d, %Y")
        except ValueError:
            # Return None or raise an exception if the format is unexpected
            return None

# Renamed function with a clearer name
def convert_datetime_column(df, date_column, year, new_column_name=None):
    """
    Applies the convert_to_datetime function to a DataFrame column.
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing the date column
    date_column (str): Name of the column containing text dates
    year (int): Year to use for the dates
    new_column_name (str, optional): Name for the new datetime column. 
                                     If None, overwrites the original column.
    
    Returns:
    pandas.DataFrame: The DataFrame with the new or modified datetime column
    """
    col_name = new_column_name if new_column_name else date_column
    df[col_name] = df[date_column].apply(lambda x: convert_to_datetime(x, year))
    return df

def normalize(series):
    return (series - series.min()) / (series.max() - series.min())

# Example:
# df = pd.DataFrame({"date": ["January 3", "February 14", "March 30"]})
# df = convert_to_date(df, "date", 2030, "datetime_column")