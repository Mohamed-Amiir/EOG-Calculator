import tkinter as tk

# Function to update the display when a button is clicked
def update_display(text):
    display_text.set(display_text.get() + text)

# Function to evaluate the expression and update the display with the result
def calculate():
    try:
        result = eval(display_text.get())
        display_text.set(str(result))
    except Exception as e:
        display_text.set("Error")

# Function to move the cursor
def move_cursor(event):
    global cursor_x, cursor_y
    if event.keysym == 'Up':
        cursor_y -= 50
    elif event.keysym == 'Down':
        cursor_y += 50
    elif event.keysym == 'Left':
        cursor_x -= 70
    elif event.keysym == 'Right':
        cursor_x += 70
    canvas.coords(cursor, cursor_x-5, cursor_y-5, cursor_x+5, cursor_y+5)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Variable to hold the text to be displayed
display_text = tk.StringVar()
display_text.set("")

# Create a canvas widget with fixed height and width
canvas = tk.Canvas(root, width=610, height=530, bg="white")
canvas.pack()

# Display area
display_area = tk.Entry(canvas, textvariable=display_text, font=('Arial', 14), bd=5, relief=tk.SUNKEN, justify='right')
canvas.create_window(305, 50, window=display_area, width=600, height=50)

# Buttons
buttons = [
    ('7', 90, 150), ('8', 210, 150), ('9', 330, 150), ('+', 450, 150),
    ('4', 90, 230), ('5', 210, 230), ('6', 330, 230), ('-', 450, 230),
    ('1', 90, 310), ('2', 210, 310), ('3', 330, 310), ('*', 450, 310),
    ('0', 90, 390), ('.', 210, 390), ('=', 330, 390), ('/', 450, 390)
]

for (text, x, y) in buttons:
    button = tk.Button(canvas, text=text, width=7, height=2, font=('Arial', 14), command=lambda t=text: update_display(t))
    canvas.create_window(x, y, window=button)

# Clear button
clear_button = tk.Button(canvas, text="C", width=7, height=2, font=('Arial', 14), command=lambda: display_text.set(""))
canvas.create_window(450, 80, window=clear_button)

# Calculate button
calculate_button = tk.Button(canvas, text="Calculate", width=10, height=2, font=('Arial', 14), command=calculate)
canvas.create_window(305, 470, window=calculate_button)

# Initial position of cursor
cursor_x = 305
cursor_y = 50

# Cursor
cursor = canvas.create_rectangle(cursor_x-5, cursor_y-5, cursor_x+5, cursor_y+5, fill='red')

# Bind arrow key events to move the cursor
root.bind('<Up>', move_cursor)
root.bind('<Down>', move_cursor)
root.bind('<Left>', move_cursor)
root.bind('<Right>', move_cursor)

# Start the Tkinter event loop
root.mainloop()
