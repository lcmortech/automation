# Tkinter calculator build without using eval function
# Instead, every operation will have its own separate function (Kenny Yip)

#setup

import tkinter as tk

#2D list, each list is a row
# reminder: replace placeholders w/ proper symbols
button_values = [
    ["AC", "+/-", "%", "//"],
    ["7", "8", "9", "x"],
    ["1", "2", "3", "+"],
    ["0", ".", "^", "="]
]

right_symbols = ["//", "x", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

# calculator colors
color_light_gray = "#d4d4d2"
color_black = "#1c1c1c"
color_orange = "#ff9500"
color_white = "ffffff"

# window setup
window = tk.Tk() #create the window
window.title("Calculator")
window.resizable(False, False) # cannot resize horizontally,or vertically

frame = tk.Frame(window)
label = tk.Label(frame, text = "0", font=("Arial", 45), background=color_black, foreground=color_white)

label.grid(row=0, column=0)
window.mainloop() # starts program

#new years eve break
#no code
#new years day
#no code