import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Canvas with Eraser")
root.geometry("600x600")  # Adjust the window size for better view

# Set the dimensions of the canvas
canvas_width = 500
canvas_height = 500
grid_size = 50  # Size of each cell

# Create the canvas with a light gray background
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#f0f0f0")  # Light gray background
canvas.pack(pady=20)

# Function to draw the grid of cells
def draw_grid():
    for x in range(0, canvas_width, grid_size):
        for y in range(0, canvas_height, grid_size):
            # Draw blue grid cells with a soft color
            canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill="#4a90e2", outline="#3b7bbf", width=2)

# Variables for the eraser's position and size
eraser_size = grid_size
eraser = None

# Function to erase cells in the area covered by the eraser
def erase(event):
    global eraser
    x1 = (event.x // grid_size) * grid_size
    y1 = (event.y // grid_size) * grid_size

    # Draw the eraser rectangle (semi-transparent white)
    if eraser:
        canvas.delete(eraser)
    eraser = canvas.create_rectangle(x1, y1, x1 + eraser_size, y1 + eraser_size, fill="white", outline="white")

    # Erase the grid cells in the eraser area
    for x in range(x1, x1 + eraser_size, grid_size):
        for y in range(y1, y1 + eraser_size, grid_size):
            canvas.create_rectangle(x, y, x + grid_size, y + grid_size, fill="white", outline="white", width=2)

# Mouse event handlers
canvas.bind("<B1-Motion>", erase)  # Erase when the mouse is dragged
canvas.bind("<ButtonRelease-1>", lambda event: canvas.delete(eraser))  # Remove eraser when mouse button is released

# Add title and instruction label
title_label = tk.Label(root, text="Canvas Eraser Tool", font=("Helvetica", 18, "bold"), fg="#333")
title_label.pack(pady=10)

instructions_label = tk.Label(root, text="Click and drag to erase the blue cells", font=("Helvetica", 12), fg="#666")
instructions_label.pack(pady=5)

# Draw the initial grid
draw_grid()

# Start the Tkinter event loop
root.mainloop()
