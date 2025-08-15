# file_utils.py
import os
from pathlib import Path
import pandas as pd

def get_csv_path(filename, folder="JL_1", base="/home/bhuns"):
    """Constructs a stable absolute path to a CSV file."""
    return os.path.join(base, folder, filename + ".csv")

def load_csv(filename, folder="JL_1", base="/home/bhuns", **kwargs):
    """Loads a CSV file using a stable absolute path."""
    path = get_csv_path(filename, folder, base)
    print(f"Loading from: {path}")
    return pd.read_csv(path, **kwargs)

def save_csv(df, filename, folder="JL_1", base="/home/bhuns", **kwargs):
    """Saves a DataFrame to a CSV file using a stable absolute path."""
    path = get_csv_path(filename, folder, base)
    print(f"Saving to: {path}")
    df.to_csv(path, index=False, **kwargs)

## your loading functions helped greatly. Extending that technique I am trying to make a structure that can handle a large quanity of data reliably and logically with consitant memberable names.
