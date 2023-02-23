def save_to_excel(data, filepath):
    """
    Saves the given data to an Excel file at the given filepath.
    The data should be a list of dictionaries, where each dictionary represents a row in the Excel sheet.

    Parameters:
    data (list): List of dictionaries, where each dictionary represents a row in the Excel sheet.
    filepath (str): The path and filename of the Excel file to be created.

    Returns:
    None
    """
    import pandas as pd

    df = pd.DataFrame(data)
    df.to_excel(filepath, index=False)
