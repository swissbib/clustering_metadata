"""General functions for chapter data preparation"""

def transform_list_to_string(df, column):
    df[column] = [', '.join(map(str, list_element)) for list_element in df[column]]

    return df
