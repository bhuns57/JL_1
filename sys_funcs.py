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
# ==============================================
from pathlib import Path
import pandas as pd
import os
# ======================================================================================
def load_dataframes_from_folder(folder_path, extension=".csv", encoding="utf-8", use_full_path=False):
    """
    Recursively loads all files with the given extension from a folder into pandas DataFrames.

    Args:
        folder_path (str): Windows-style path to the folder.
        extension (str): File extension to search for (e.g., ".csv", ".txt").
        encoding (str): Encoding used to read the files.
        use_full_path (bool): If True, keys will be full paths; otherwise, just filenames.

    Returns:
        dict: Dictionary of DataFrames keyed by filename or full path.
    """
    # Convert Windows path to WSL format if needed
    if os.name != "nt":  # If running in WSL/Linux
        folder_path = folder_path.replace("\\", "/")
        if folder_path.startswith("/mnt/") is False:
            drive_letter = folder_path[0].lower()
            folder_path = f"/mnt/{drive_letter}{folder_path[2:]}"
    
    folder = Path(folder_path)

    # Recursively find all matching files
    files = list(folder.rglob(f"*{extension}"))

    if not files:
        print(f"⚠️ No files with extension '{extension}' found in {folder_path}")
        return {}

    # Load each file into a DataFrame
    dataframes = {}
    for file in files:
        try:
            df = pd.read_csv(file, encoding=encoding) if extension == ".csv" else pd.read_table(file, encoding=encoding)
            key = str(file) if use_full_path else file.name
            dataframes[key] = df
        except Exception as e:
            print(f"❌ Failed to load {file}: {e}")

    return dataframes















#=====================================================================
def get_dtv_range():
    try:
        start_dtv = int(input("Enter beginning dtv: "))
        end_dtv = int(input("Enter ending dtv: "))
        return [start_dtv, end_dtv]
    except ValueError:
        print("Invalid input. Please enter integer values.")
        return None
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
    blnk_update_dt_row_dict = {}

    for date_key in dt_row_dict:  # ✅ use dt_row_dict here
        if start_date <= date_key <= end_date:
            blnk_update_dt_row_dict [date_key] = {col: '' for col in dt_row_dict[date_key]}  # also fix xrow_dict if needed
#    update_row_dict = blnk_update_dt_row_dict 
#    return update_row_dict
    return blnk_update_row_dict
# =========================================================

# DEF transpose lut from rows to cols
def transpose_csv_to_col_dict(csv_rows):
    headers = csv_rows[0][1:]  # skip BOM or placeholder
    col_dict = {}

    for col_index, serial in enumerate(headers):
        entry = {}
        for row in csv_rows[1:]:
            key = row[0].strip('"')  # remove quotes
            value = row[col_index + 1].strip('"')
            # Convert types if needed
            if key in ['value', 'min', 'max', 'step']:
                try:
                    entry[key] = float(value) if '.' in value else int(value)
                except ValueError:
                    entry[key] = None
            elif key == 'active':
                entry[key] = value.lower() not in ['no', 'false', '0', '']
            else:
                entry[key] = value
        col_dict[serial] = entry

    return col_dict

# =========================================================
# step 1 for sliders ✅ Final Pattern: Interactive Form + Pickle-Based Retrieval
import ipywidgets as widgets
from IPython.display import display, clear_output
import pickle


# ===================================================================================
# Step 2: Retrieve the result in a separate cell for sliders
def get_update_dt_row_dict(pickle_path="update_dt_row_dict"):
    import pickle
    with open(pickle_path, "rb") as f:
        result = pickle.load(f)
    print("📤 Retrieved result from pickle:")
    return result

#========================================================================================

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
# ============ put values into the" blnk_update_dt_row_dict" ================================================
#==================================================================

def universal_import(folder_path, pattern="*", expected_columns=None, df_name=None, verbose=True):
    folder = Path(folder_path)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder_path}")
    
    file_list = list(folder.glob(pattern))
    dfs = []
    
    for f in file_list:
        for encoding in ['utf-8', 'ISO-8859-1']:
            try:
                if f.suffix in ['.xlsx', '.xls']:
                    df = pd.read_excel(f)
                else:
                    df = pd.read_csv(f, encoding=encoding, sep=None, engine='python')
                
                if expected_columns and df.shape[1] != expected_columns:
                    if verbose:
                        print(f"⚠️ Skipped {f.name}: expected {expected_columns} columns, got {df.shape[1]}")
                    break
                
                df['source_file'] = f.name
                df['encoding_used'] = encoding
                dfs.append(df)
                if verbose:
                    print(f"✅ Loaded {f.name} with {encoding}")
                break
            except Exception as e:
                if encoding == 'ISO-8859-1' and verbose:
                    print(f"❌ Skipped {f.name}: {e}")
    
    if dfs:
        combined = pd.concat(dfs, ignore_index=True)
        label = df_name if df_name else "imported_dataframe"
        pickle_path = Path.cwd() / f"{label}.pkl"
        combined.to_pickle(pickle_path)
        if verbose:
            print(f"✅ [{label}] Final DataFrame: {len(combined)} rows from {len(dfs)} files.")
            print(f"💾 Saved to pickle: {pickle_path}")
        return combined
    else:
        if verbose:
            print("🚫 No valid files loaded.")
        return pd.DataFrame()

###_adding [iclel save]
