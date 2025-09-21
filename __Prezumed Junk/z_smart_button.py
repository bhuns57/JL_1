{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a8ca85df-b56d-4678-902c-8a982673a93a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "6e923144-4aa4-4e38-8d91-5cbfd80e068b",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mNameError\u001b[39m                                 Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[7]\u001b[39m\u001b[32m, line 6\u001b[39m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mIPython\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdisplay\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m display\n\u001b[32m      5\u001b[39m \u001b[38;5;66;03m# Dynamically import your module\u001b[39;00m\n\u001b[32m----> \u001b[39m\u001b[32m6\u001b[39m my_module = importlib.import_module(\u001b[33m\"\u001b[39m\u001b[33mmy_functions\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m      8\u001b[39m \u001b[38;5;66;03m# Create the button and label\u001b[39;00m\n\u001b[32m      9\u001b[39m button = widgets.Button(description=\u001b[33m\"\u001b[39m\u001b[33mGreet Me\u001b[39m\u001b[33m\"\u001b[39m)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~/miniconda3/envs/scu/lib/python3.11/importlib/__init__.py:126\u001b[39m, in \u001b[36mimport_module\u001b[39m\u001b[34m(name, package)\u001b[39m\n\u001b[32m    124\u001b[39m             \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[32m    125\u001b[39m         level += \u001b[32m1\u001b[39m\n\u001b[32m--> \u001b[39m\u001b[32m126\u001b[39m \u001b[38;5;28;01mreturn\u001b[39;00m _bootstrap._gcd_import(name[level:], package, level)\n",
      "\u001b[36mFile \u001b[39m\u001b[32m<frozen importlib._bootstrap>:1204\u001b[39m, in \u001b[36m_gcd_import\u001b[39m\u001b[34m(name, package, level)\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m<frozen importlib._bootstrap>:1176\u001b[39m, in \u001b[36m_find_and_load\u001b[39m\u001b[34m(name, import_)\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m<frozen importlib._bootstrap>:1147\u001b[39m, in \u001b[36m_find_and_load_unlocked\u001b[39m\u001b[34m(name, import_)\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m<frozen importlib._bootstrap>:690\u001b[39m, in \u001b[36m_load_unlocked\u001b[39m\u001b[34m(spec)\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m<frozen importlib._bootstrap_external>:940\u001b[39m, in \u001b[36mexec_module\u001b[39m\u001b[34m(self, module)\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m<frozen importlib._bootstrap>:241\u001b[39m, in \u001b[36m_call_with_frames_removed\u001b[39m\u001b[34m(f, *args, **kwds)\u001b[39m\n",
      "\u001b[36mFile \u001b[39m\u001b[32m~/JL_1/my_functions.py:16\u001b[39m\n\u001b[32m      1\u001b[39m {\n\u001b[32m      2\u001b[39m  \u001b[33m\"\u001b[39m\u001b[33mcells\u001b[39m\u001b[33m\"\u001b[39m: [\n\u001b[32m      3\u001b[39m   {\n\u001b[32m      4\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mcell_type\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mcode\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m      5\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mexecution_count\u001b[39m\u001b[33m\"\u001b[39m: \u001b[32m1\u001b[39m,\n\u001b[32m      6\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mid\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33m9a35c72f-b172-4298-9fe6-7e161446fc54\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m      7\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mmetadata\u001b[39m\u001b[33m\"\u001b[39m: {},\n\u001b[32m      8\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33moutputs\u001b[39m\u001b[33m\"\u001b[39m: [],\n\u001b[32m      9\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33msource\u001b[39m\u001b[33m\"\u001b[39m: [\n\u001b[32m     10\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mdef greet_user(name):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[33m\"\u001b[39m,\n\u001b[32m     11\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33m    return f\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[33mHello, \u001b[39m\u001b[38;5;132;01m{name}\u001b[39;00m\u001b[33m!\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[33m\"\u001b[39m\n\u001b[32m     12\u001b[39m    ]\n\u001b[32m     13\u001b[39m   },\n\u001b[32m     14\u001b[39m   {\n\u001b[32m     15\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mcell_type\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mcode\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m---> \u001b[39m\u001b[32m16\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mexecution_count\u001b[39m\u001b[33m\"\u001b[39m: null,\n\u001b[32m     17\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mid\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mb9ddc801-9eac-40b8-945a-7e0a3bfb0e87\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     18\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mmetadata\u001b[39m\u001b[33m\"\u001b[39m: {},\n\u001b[32m     19\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33moutputs\u001b[39m\u001b[33m\"\u001b[39m: [],\n\u001b[32m     20\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33msource\u001b[39m\u001b[33m\"\u001b[39m: []\n\u001b[32m     21\u001b[39m   }\n\u001b[32m     22\u001b[39m  ],\n\u001b[32m     23\u001b[39m  \u001b[33m\"\u001b[39m\u001b[33mmetadata\u001b[39m\u001b[33m\"\u001b[39m: {\n\u001b[32m     24\u001b[39m   \u001b[33m\"\u001b[39m\u001b[33mkernelspec\u001b[39m\u001b[33m\"\u001b[39m: {\n\u001b[32m     25\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mdisplay_name\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mPython (scu)\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     26\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mlanguage\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mpython\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     27\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mname\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mscu\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m     28\u001b[39m   },\n\u001b[32m     29\u001b[39m   \u001b[33m\"\u001b[39m\u001b[33mlanguage_info\u001b[39m\u001b[33m\"\u001b[39m: {\n\u001b[32m     30\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mcodemirror_mode\u001b[39m\u001b[33m\"\u001b[39m: {\n\u001b[32m     31\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mname\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mipython\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     32\u001b[39m     \u001b[33m\"\u001b[39m\u001b[33mversion\u001b[39m\u001b[33m\"\u001b[39m: \u001b[32m3\u001b[39m\n\u001b[32m     33\u001b[39m    },\n\u001b[32m     34\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mfile_extension\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33m.py\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     35\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mmimetype\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mtext/x-python\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     36\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mname\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mpython\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     37\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mnbconvert_exporter\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mpython\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     38\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mpygments_lexer\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33mipython3\u001b[39m\u001b[33m\"\u001b[39m,\n\u001b[32m     39\u001b[39m    \u001b[33m\"\u001b[39m\u001b[33mversion\u001b[39m\u001b[33m\"\u001b[39m: \u001b[33m\"\u001b[39m\u001b[33m3.11.13\u001b[39m\u001b[33m\"\u001b[39m\n\u001b[32m     40\u001b[39m   }\n\u001b[32m     41\u001b[39m  },\n\u001b[32m     42\u001b[39m  \u001b[33m\"\u001b[39m\u001b[33mnbformat\u001b[39m\u001b[33m\"\u001b[39m: \u001b[32m4\u001b[39m,\n\u001b[32m     43\u001b[39m  \u001b[33m\"\u001b[39m\u001b[33mnbformat_minor\u001b[39m\u001b[33m\"\u001b[39m: \u001b[32m5\u001b[39m\n\u001b[32m     44\u001b[39m }\n",
      "\u001b[31mNameError\u001b[39m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import importlib\n",
    "import ipywidgets as widgets\n",
    "from IPython.display import display\n",
    "\n",
    "# Dynamically import your module\n",
    "my_module = importlib.import_module(\"my_functions\")\n",
    "\n",
    "# Create the button and label\n",
    "button = widgets.Button(description=\"Greet Me\")\n",
    "output = widgets.Output()\n",
    "\n",
    "# Callback to run function when clicked\n",
    "def on_button_clicked(b):\n",
    "    with output:\n",
    "        output.clear_output()\n",
    "        result = my_module.greet_user(\"Bill\")\n",
    "        print(result)\n",
    "\n",
    "button.on_click(on_button_clicked)\n",
    "\n",
    "# Display the widgets\n",
    "display(widgets.VBox([button, output]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9ef76241-0ec7-47d3-86c5-8876067f2f7e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab9b559c-dd9e-4831-a0c6-7cbc8daebb0f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python (scu)",
   "language": "python",
   "name": "scu"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
