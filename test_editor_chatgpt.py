import tkinter as tk
from tkinter import filedialog

def open_file():
    """
    Open a file dialog to select and open a text file. Display the content in the Tkinter text widget.
    """
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    with open(file_path, "r") as file:
        text.delete("1.0", tk.END)
        text.insert(tk.END, file.read())

def save_file():
    """
    Open a file dialog to choose the save location and save the content of the Tkinter text widget to a text file.
    """
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file_path:
        return
    with open(file_path, "w") as file:
        file.write(text.get("1.0", tk.END))

# Tkinter setup
root = tk.Tk()
root.title("Text Editor")
root.geometry("500x500")

# Text widget
text = tk.Text(root)
text.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Open button
open_button = tk.Button(root, text="Open", command=open_file)
open_button.grid(row=1, column=0, sticky="nsew")

# Save button
save_button = tk.Button(root, text="Save", command=save_file)
save_button.grid(row=2, column=0, sticky="nsew")

# Configure weights for resizing
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Tkinter main loop
root.mainloop()
