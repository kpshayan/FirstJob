import csv
import webbrowser
import time
with open("../values.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        for value in row:
            webbrowser.open_new_tab(value)
            
            
time.sleep(110)
