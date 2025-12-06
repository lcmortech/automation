# CR: NeuralNine

import tkinter as tk

# GLOBAL VARIABLES
calculation = ""

# FUNCTIONS
def add_to_calculation(sym):
    global calculation
    calculation += str(sym)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def eval_calculation(calc):
    global calculation
    try:
        #result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field(
            text_result.delete(1.0, "Error")
        )
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# TKINTER SETUP
window = tk.Tk() #entrypoint
window.title = "GUI Calculator" #title
window.geometry("300x275")

# VARIABLES
text_result = tk.Text(window, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

#use lambda or else it immediately calls function
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1)) 
btn_1.grid(row=2, column=1)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1)) 
btn_1.grid(row=2, column=1)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1)) 
btn_1.grid(row=2, column=1)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1)) 
btn_1.grid(row=2, column=1)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1)) 
btn_1.grid(row=2, column=1)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1)) 
btn_1.grid(row=2, column=1)
btn_1 = tk.Button(window, text="1", command=lambda: add_to_calculation(1)) 
btn_1.grid(row=2, column=1)
window.mainloop() #endpoint