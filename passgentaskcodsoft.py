import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_digits = digits_var.get()
    use_special_chars = special_chars_var.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    password_display.config(text=password)

root = tk.Tk()
root.title("Task:Password Generator")

# Length Label and Entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Checkboxes for character types
uppercase_var = tk.BooleanVar()
uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_checkbox.pack()

digits_var = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_checkbox.pack()

special_chars_var = tk.BooleanVar()
special_chars_checkbox = tk.Checkbutton(root, text="Include Special Characters", variable=special_chars_var)
special_chars_checkbox.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Display Password
password_display = tk.Label(root, text="")
password_display.pack()

root.mainloop()
