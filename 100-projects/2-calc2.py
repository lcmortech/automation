# Tkinter calculator build without using eval function
# Instead, every operation will have its own separate function (Kenny Yip)

#setup

import tkinter as tk

#2D list, each list is a row
button_values = [
    ["AC", "+/-", "%", "//"],
    ["7", "8", "9", "x"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="]
]

right_symbols = ["//", "x", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

# calculator colors