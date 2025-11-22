import tkinter as tk

#tk._test()

def on_click():
    print("testing...")


root = tk.Tk()
root.title("Simple App")

lbl = tk.Label(root, text="Label 1")
lbl.grid(row=0, column=0) #stacks by default (item.grid())

btn = tk.Button(root, text="Click Me", command=on_click)
btn.grid(row=0, column=1)



root.mainloop()