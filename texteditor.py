import sys
from tkinter import *
from tkinter import filedialog, font, messagebox

# Create the main application window
root = Tk()
root.title("Text Editor")
root.geometry("800x600")

# Create a Text widget
text = Text(root, wrap="word", undo=True, font=("Helvetica", 12))
text.pack(fill="both", expand=True)

# Function to open a file
def open_file():
    file = filedialog.askopenfilename(defaultextension=".txt",
                                      filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file:
        text.delete(1.0, END)
        with open(file, "r") as file_obj:
            text.insert(1.0, file_obj.read())
        root.title(f"Text Editor - {file}")

# Function to save a file
def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if file:
        with open(file, "w") as file_obj:
            file_obj.write(text.get(1.0, END))
        root.title(f"Text Editor - {file}")

# Function to change font to Helvetica
def set_font_helvetica():
    text.config(font=("Helvetica", font_size.get()))

# Function to change font to Courier
def set_font_courier():
    text.config(font=("Courier", font_size.get()))

# Function to change font size
def change_font_size(event=None):
    current_font = font.nametofont(text.cget("font"))
    current_font.configure(size=font_size.get())

# Function to display a status bar
def update_status(event=None):
    row, col = text.index(INSERT).split(".")
    status_var.set(f"Line: {row} | Column: {col}")

# Create a Font menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

font_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Courier", command=set_font_courier)
font_menu.add_command(label="Helvetica", command=set_font_helvetica)

# Add a Font Size Option
font_size = IntVar(value=12)
font_size_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Font Size", menu=font_size_menu)
for size in range(8, 32, 2):
    font_size_menu.add_radiobutton(label=str(size), variable=font_size, command=change_font_size)

# Add a Status Bar
status_var = StringVar()
status_bar = Label(root, textvariable=status_var, anchor='e')
status_bar.pack(side="bottom", fill="x")

# Bind events for updating the status bar
text.bind("<KeyRelease>", update_status)
text.bind("<ButtonRelease>", update_status)

# Initialize status bar
update_status()

# Run the Tkinter event loop
root.mainloop()
