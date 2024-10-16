import tkinter as tk
from tkinter import ttk

# Conversion factors for length units
conversion_factors = {
    "Meters": 1,
    "Kilometers": 0.001,
    "Miles": 0.000621371,
    "Feet": 3.28084,
    "Inches": 39.3701,
}

def convert():
    try:
        # Get user input
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        
        # Convert to meters first, then to the desired unit
        value_in_meters = value * conversion_factors[from_unit]
        converted_value = value_in_meters / conversion_factors[to_unit]
        
        # Display result
        label_result.config(text=f"{value} {from_unit} = {converted_value:.4f} {to_unit}")
    except ValueError:
        label_result.config(text="Please enter a valid number!")

# Initialize window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("300x250")

# Input field for value
label_value = ttk.Label(root, text="Enter value:")
label_value.pack(pady=5)
entry_value = ttk.Entry(root)
entry_value.pack(pady=5)

# Dropdown for 'from' unit
label_from = ttk.Label(root, text="Convert from:")
label_from.pack(pady=5)
combo_from = ttk.Combobox(root, values=list(conversion_factors.keys()), state="readonly")
combo_from.current(0)  # Default to the first option
combo_from.pack(pady=5)

# Dropdown for 'to' unit
label_to = ttk.Label(root, text="Convert to:")
label_to.pack(pady=5)
combo_to = ttk.Combobox(root, values=list(conversion_factors.keys()), state="readonly")
combo_to.current(1)  # Default to the second option
combo_to.pack(pady=5)

# Convert button
btn_convert = ttk.Button(root, text="Convert", command=convert)
btn_convert.pack(pady=10)

# Label to show result
label_result = ttk.Label(root, text="")
label_result.pack(pady=10)

# Run the GUI
root.mainloop()
