import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''A simple function which uses pandas to read a csv file.

    It prints the dimensions of the data and then returns dataframe.'''
    try:
        data = pd.read_csv(path)
    except Exception as e:
        print("Error loading data:", e)
        return
    print("Loading dataset of dimensions", data.shape)
    return data
