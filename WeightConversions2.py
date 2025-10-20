import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_weight():
    try:
        weight = float(weight_entry.get())
        unit = unit_var.get()

        if unit == "kg":
            converted = weight * 2.205
            result_label.config(text=f"{weight} kg is {round(converted, 1)} lb")
        elif unit == "lb":
            converted = weight / 2.205
            result_label.config(text=f"{weight} lb is {round(converted, 2)} kg")
        else:
            messagebox.showerror("Invalid Unit", "Please select a valid unit.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid numeric weight.")

# Set up main window
root = tk.Tk()
root.title("Weight Converter")
root.geometry("300x200")
root.resizable(False, False)

# Weight input
tk.Label(root, text="Enter weight:").pack(pady=5)
weight_entry = tk.Entry(root, width=20)
weight_entry.pack()

# Unit selection
unit_var = tk.StringVar()
unit_var.set("kg")  # default
ttk.Label(root, text="Select unit:").pack(pady=5)
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["kg", "lb"], state="readonly")
unit_menu.pack()

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_weight)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the app
root.mainloop()
