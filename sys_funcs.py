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
# update_dt_row_dict  Makes the empty dictionary to fill
def make_blnk_update_row_dict(dt_row_dict, dvt):
    start_date, end_date = dvt
    update_row_dict = {}

    for date_key in dt_row_dict:  # ✅ use dt_row_dict here
        if start_date <= date_key <= end_date:
            update_row_dict[date_key] = {col: '' for col in dt_row_dict[date_key]}  # also fix xrow_dict if needed

    return update_row_dict

# input function =========================================================================================
def update_serial_values(update_dt_row_dict):
    print("Enter a number for each serial, or press Enter twice to skip.\n")
    for day, serials in update_dt_row_dict.items():
        print(f"\nDay: {day}")
        for serial in serials:
            while True:
                value = input(f"  Serial {serial}: ")
                if value == "":
                    print("  Skipped.")
                    break
                try:
                    update_dt_row_dict[day][serial] = float(value)
                    break
                except ValueError:
                    print("  Invalid input. Please enter a number or press Enter to skip.")
    return update_dt_row_dict
# =========================================================
def transfer_updates(updated_dict, dt_row_dict):
    """
    Transfers non-empty values from updated_dict into dt_row_dict.
    Assumes both dictionaries share the same structure: {day: {serial: value}}.
    """
    for day, serials in updated_dict.items():
        if day not in dt_row_dict:
            dt_row_dict[day] = {}  # Optionally scaffold missing day
        for serial, value in serials.items():
            if value != '':
                dt_row_dict[day][serial] = value
    return dt_row_dict
