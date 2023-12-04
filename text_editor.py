# Importing Tkinter and filedialog module
import tkinter as tk
from tkinter import filedialog

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    with open(file_path, "r") as file:
        text.delete("1.0", tk.END)
        text.insert(tk.END, file.read())

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if not file_path:
        return
    with open(file_path, "w") as file:
        file.write(text.get("1.0", tk.END))

# Creating the main Tkinter window
root = tk.Tk()
root.title("Text Editor")
root.geometry("500x500")

# Creating a Text widget for text editing
text = tk.Text(root)
text.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Adding Open and Save buttons with corresponding functions
open_button = tk.Button(root, text="Open", command=open_file)
open_button.grid(row=1, column=0, sticky="nsew")

save_button = tk.Button(root, text="Save", command=save_file)
save_button.grid(row=2, column=0, sticky="nsew")

# Configuring row and column weights for resizing
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Running the Tkinter main loop
root.mainloop()
