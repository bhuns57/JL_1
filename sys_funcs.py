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
def from sys_funcs import (csv_rows):
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
import ipywidgets as widgets
from IPython.display import display, clear_output

def update_values_with_config(blnk_update_dt_row_dict, lut_serial_config):
    update_dt_row_dict = blnk_update_dt_row_dict.copy()
    output = widgets.Output()
    display(output)

    def build_form():
        with output:
            clear_output()
            print("Adjust sliders for each active supplement. Suspended ones are skipped.\n")
            form_items = []
            slider_widgets = {}

            for day, serials in update_dt_row_dict.items():
                day_label = widgets.HTML(value=f"<b>Day: {day}</b>")
                form_items.append(day_label)

                for serial in serials:
                    config = lut_serial_config.get(serial, {})
                    active = config.get('active', True)
                    if str(active).lower() in ['no', 'false']:
                        continue  # Skip suspended supplements

                    name = config.get('name', serial)
                    value = config.get('value', 1)
                    min_val = config.get('min', 0)
                    max_val = config.get('max', 10)
                    step_val = config.get('step', 1)

                    slider = widgets.FloatSlider(
                        value=value,
                        min=min_val,
                        max=max_val,
                        step=step_val,
                        description=f"{name}:",
                        style={'description_width': 'initial'},
                        layout=widgets.Layout(width='400px')
                    )
                    slider_widgets[(day, serial)] = slider
                    form_items.append(slider)

            if not slider_widgets:
                form_items.append(widgets.HTML(value="<i>No active supplements to update.</i>"))

            submit_button = widgets.Button(description="Submit")
            form_items.append(submit_button)
            form = widgets.VBox(form_items)
            display(form)

            def on_submit(b):
                for (day, serial), slider in slider_widgets.items():
                    update_dt_row_dict[day][serial] = slider.value
                clear_output()
                print("✅ Update complete. Here's the result:")
                print(update_dt_row_dict)

            submit_button.on_click(on_submit)

    build_form()
# ========================================================================================

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