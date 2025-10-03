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
    blnk_update_dt_row_dict = {}

    for date_key in dt_row_dict:  # ✅ use dt_row_dict here
        if start_date <= date_key <= end_date:
            blnk_update_dt_row_dict [date_key] = {col: '' for col in dt_row_dict[date_key]}  # also fix xrow_dict if needed
    update_row_dict = blnk_update_dt_row_dict 
    return update_row_dict

# obolete becaue of a bug in jupyter lab input function 
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

def xupdate_values_with_config(blnk_update_dt_row_dict, lut_serial_config, pickle_path="update_result.pkl"):
    update_dt_row_dict = {day: dict(serials) for day, serials in blnk_update_dt_row_dict.items()}
    output = widgets.Output()
    display(output)

    form_items = []
    slider_widgets = {}

    for day, serials in update_dt_row_dict.items():
        form_items.append(widgets.HTML(value=f"<b>Day: {day}</b>"))
        for serial in serials:
            config = lut_serial_config.get(serial, {})
            if str(config.get('active', True)).lower() in ['no', 'false']:
                continue
            slider = widgets.FloatSlider(
                value=config.get('value', 1),
                min=config.get('min', 0),
                max=config.get('max', 10),
                step=config.get('step', 1) or 1,
                description=f"{config.get('name', serial)}:",
                layout=widgets.Layout(width='400px')
            )
            slider_widgets[(day, serial)] = slider
            form_items.append(slider)

    submit_button = widgets.Button(description="Submit")

    def on_submit(b):
        for (day, serial), slider in slider_widgets.items():
            update_dt_row_dict[day][serial] = slider.value

        with open(pickle_path, "wb") as f:
            pickle.dump(update_dt_row_dict, f)

        with output:
            clear_output()
            print("✅ Update complete. Result saved to pickle.")
            print("📦 You can now retrieve it using `get_update_result()` in a new cell.")

    submit_button.on_click(on_submit)
    form_items.append(submit_button)
    form = widgets.VBox(form_items)

    with output:
        clear_output()
        print("Adjust sliders for each active supplement. Suspended ones are skipped.\n")
        display(form)
# ===================================================================================
# Step 2: Retrieve the result in a separate cell for sliders
def get_xupdate_result(pickle_path="update_result.pkl"):
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