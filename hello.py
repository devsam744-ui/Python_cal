import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("My Tkinter App")

# Create a widget (e.g., a Label)
label = tk.Label(root, text="Hello, Tkinter!")
label.pack() # Use a geometry manager to display the widget

# Start the Tkinter event loop
root.mainloop()