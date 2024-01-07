import tkinter as tk
import math

def on_click(button_value):
    current = entry_var.get()
    
    if button_value == "=":
        try:
            result = eval(current)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == "C":
        entry_var.set("")
    elif button_value == "AC":
        entry_var.set("")
    elif button_value == "sqrt":
        try:
            result = math.sqrt(float(current))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif button_value == "^":
        entry_var.set(current + "**")
    elif button_value == "!":
        try:
            result = math.factorial(int(current))
            entry_var.set(result)
        except ValueError:
            entry_var.set("Error")
    elif button_value == "%":
        entry_var.set(str(float(current) / 100))
    elif button_value == "pi":
        entry_var.set(current + str(math.pi))
    elif button_value == "Backspace":
        entry_var.set(current[:-1])
    else:
        entry_var.set(current + button_value)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Entry widget to display the current input
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=6)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'sqrt', '^', '!',
    '%', 'pi', 'AC', 'Backspace'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=5, height=2, command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the Tkinter event loop
root.mainloop()
