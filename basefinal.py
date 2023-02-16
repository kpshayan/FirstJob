import csv
import webbrowser
import time
import base64
from random import randint
with open("values.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        for value in row:
            outvalue=base64.standard_b64decode(value)
            webbrowser.open_new_tab(outvalue)
            
            
time.sleep(randint(120,500))
