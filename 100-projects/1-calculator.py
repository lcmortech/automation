# CR: NeuralNine

import tkinter as tk

# GLOBAL VARIABLES
calculation = ""

# FUNCTIONS
def add_to_calculation(sym):
    pass

def eval_calculation(calc):
    pass

def clear_field():
    pass

# TKINTER SETUP
window = tk.Tk() #entrypoint
window.title = "GUI Calculator" #title
window.geometry("300x275")

# VARIABLES
text_result = tk.text(window, height=2, width=16, font=("Arial",24))
text.grid(row=0,column=1)

window.mainloop() #endpoint
