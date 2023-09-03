import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result.set(num1 + num2)
        elif operator == "-":
            result.set(num1 - num2)
        elif operator == "*":
            result.set(num1 * num2)
        elif operator == "/":
            if num2 == 0:
                result.set("Error")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Error")

# Create the main window
root = tk.Tk()
root.title("Task:Calculator")

# Create and configure input fields and labels
label_num1 = tk.Label(root, text="Number 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Number 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create and configure operator dropdown
operator_var = tk.StringVar()
operator_var.set("+")  # Default operator is addition

label_operator = tk.Label(root, text="Operator:")
label_operator.pack()
operator_dropdown = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_dropdown.pack()

# Create and configure Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

# Create and configure result label
result = tk.StringVar()
result.set("")  # Initialize result to empty string
result_label = tk.Label(root, textvariable=result)
result_label.pack()

root.mainloop()
