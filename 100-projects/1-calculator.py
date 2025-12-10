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
btn_2 = tk.Button(window, text="2", command=lambda: add_to_calculation(1)) 
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(window, text="3", command=lambda: add_to_calculation(1)) 
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(window, text="4", command=lambda: add_to_calculation(1)) 
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(window, text="5", command=lambda: add_to_calculation(1)) 
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(window, text="6", command=lambda: add_to_calculation(1)) 
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(window, text="7", command=lambda: add_to_calculation(1)) 
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(window, text="8", command=lambda: add_to_calculation(1)) 
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(window, text="9", command=lambda: add_to_calculation(1)) 
btn_9.grid(row=4, column=3)
btn_0= tk.Button(window, text="0", command=lambda: add_to_calculation(1)) 
btn_0.grid(row=5, column=1)
btn_ac = tk.Button(window, text="-", command=lambda: add_to_calculation(1)) 
btn_ac.grid(row=5, column=1)
btn_ac = tk.Button(window, text="clear", command=lambda: add_to_calculation(1)) 
btn_ac.grid(row=5, column=1)
window.mainloop() #endpoint