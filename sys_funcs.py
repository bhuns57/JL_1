from pathlib import Path
import csv
import sys_funcs
from pathlib import Path
import csv
import pandas as pd
import numpy as np
import tkinter as tk
import pickle
from pathlib import Path
import csv
import os
import sys
import re
#=======================================================
def clean_wsl_path(raw_path):                            #  raw_path = "bnm.csv"
    """
    Cleans and normalizes a WSL path for safe use in file operations.
    Returns a pathlib.Path object.
    """
    raw_path = raw_path.strip().replace('\\', '/')
    raw_path = re.sub(r'/+', '/', raw_path)
    return Path(raw_path)

#==========================================================================

# sys_funcs.py
import csv
from pathlib import Path

def read_csv_to_array(filepath):
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        array = [row for row in reader if row]
    return array


#=====================================================================

# array_to_dt_row_dict(array) THIS IS THE TOTAL DATA FOR THIS "bnm"
def array_to_dt_row_dict(array):
    header = array[0][1:]  # Skip 'dtv', keep other column names
    dt_row_dict = {} 

    for row in array[1:]:
        key = row[0]  # 'dtv' value
        values = row[1:]
        dt_row_dict[key] = dict(zip(header, values))

    return dt_row_dict
# =====================================================================