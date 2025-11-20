import tkinter as tk

root = tk.Tk()

root.title("Simple App")

frame = tk.Frame(root)
frame.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=0)

entry_btn = tk.Button(frame, text="Add")

root.mainloop()