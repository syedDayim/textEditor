import sys

# Version check for Python 2 or 3
v = sys.version
if v.startswith("2.7"):
    from Tkinter import * 
    import tkFileDialog as filedialog  # For Python 2.7, use tkFileDialog
elif v.startswith("3."):
    from tkinter import *  # For Python 3.x, use tkinter
    from tkinter import filedialog

# Create the main application window
root = Tk()
root.title("Text Editor")

# Create a Text widget
text = Text(root)
text.grid()

# Define the saveas function
def saveas():
    global text
    t = text.get("1.0", "end-1c")  # Get all content from the Text widget
    savelocation = filedialog.asksaveasfilename(defaultextension=".txt",
                                                filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
    if savelocation:  # Check if a save location was selected
        with open(savelocation, "w") as file1:
            file1.write(t)

# Create a Save button
button = Button(root, text="Save", command=saveas)
button.grid()

# Define font change functions
def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

# Create a Font menu
font_menu = Menu(root)
root.config(menu=font_menu)

font_submenu = Menu(font_menu, tearoff=0)
font_menu.add_cascade(label="Font", menu=font_submenu)
font_submenu.add_command(label="Courier", command=FontCourier)
font_submenu.add_command(label="Helvetica", command=FontHelvetica)

# Run the Tkinter event loop
root.mainloop()
