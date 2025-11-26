import tkinter as tk
import pandas as pd
from bs4 import BeautifulSoup

root = tk.Tk()

df = read_csv("csv")

# extra feature using sqlite3 to store db from csv
# use beautifulsoup with sqlite3 and pandas to create db from dataframe or vice versa