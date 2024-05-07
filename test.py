# import tkinter as tk

# # Function to move the cursor
# def move_cursor(event):
#     global cursor_x, cursor_y
#     key = event.keysym
#     if key == "Up" and cursor_y > 0:
#         cursor_y -= 1
#     elif key == "Down" and cursor_y < canvas_height - 1:
#         cursor_y += 1
#     elif key == "Left" and cursor_x > 0:
#         cursor_x -= 1
#     elif key == "Right" and cursor_x < canvas_width - 1:
#         cursor_x += 1
#     elif key == "space":
#         press_button_under_cursor()

#     redraw_cursor()

# # Function to toggle the selection state
# def toggle_selection():
#     is_selected[cursor_y][cursor_x] = True
#     redraw_cursor()
#     root.after(1000, return_to_initial_position)  # Return to initial position after 1000 milliseconds

# # Function to return to the initial position
# def return_to_initial_position():
#     global cursor_x, cursor_y
#     cursor_x = 0
#     cursor_y = 0
#     redraw_cursor()

# # Function to redraw the cursor
# def redraw_cursor():
#     canvas.delete("cursor")
#     x1 = cursor_x * cell_size
#     y1 = cursor_y * cell_size
#     x2 = x1 + cell_size
#     y2 = y1 + cell_size
#     fill_color = "blue" if is_selected[cursor_y][cursor_x] else "white"
#     canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="white", tags="cursor")

# # Function to handle button clicks
# def button_click(symbol):
#     if symbol == '=':
#         evaluate_expression()
#     else:
#         entry.insert(tk.END, symbol)

# # Function to evaluate expression
# def evaluate_expression():
#     expression = entry.get()
#     try:
#         result = eval(expression)
#         label_result.config(text="Result: " + str(result))
#     except Exception as e:
#         label_result.config(text="Error: " + str(e))

# # Function to press the button under the cursor
# def press_button_under_cursor():
#     global cursor_x, cursor_y
#     col = cursor_x
#     row = cursor_y
#     button_index = row * canvas_width + col
#     if 0 <= button_index < len(button_symbols):
#         button_symbol = button_symbols[button_index]
#         button_click(button_symbol)

# # Initialize cursor position
# cursor_x = 0
# cursor_y = 0

# # Initialize canvas dimensions and cell size
# canvas_width = 4
# canvas_height = 4
# cell_size = 50

# # Initialize selection state
# is_selected = [[False for _ in range(canvas_width)] for _ in range(canvas_height)]

# # Create the main window
# root = tk.Tk()
# root.title("Cursor Application")

# # Create the canvas
# canvas = tk.Canvas(root, width=canvas_width * cell_size, height=canvas_height * cell_size, bg="red")
# canvas.pack()

# # Bind arrow keys and space key
# root.bind("<Up>", move_cursor)
# root.bind("<Down>", move_cursor)
# root.bind("<Left>", move_cursor)
# root.bind("<Right>", move_cursor)
# root.bind("<space>", move_cursor)

# # Draw initial cursor
# redraw_cursor()

# # Draw calculator buttons on the canvas
# button_symbols = ['7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '0', '=', 'C', '+' ]
# for i, symbol in enumerate(button_symbols):
#     col = i % canvas_width
#     row = i // canvas_width
#     x1 = col * cell_size
#     y1 = row * cell_size
#     x2 = x1 + cell_size
#     y2 = y1 + cell_size
#     canvas.create_rectangle(x1, y1, x2, y2, fill="lightgray", outline="white", tags="button")
#     canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=symbol, font=('Arial', 14), tags="button_text")

# # Create an entry widget for input
# entry = tk.Entry(root, font=('Arial', 18), width=20)
# entry.pack()

# # Create a label to display the result
# label_result = tk.Label(root, text="Result: ", font=('Arial', 12))
# label_result.pack()

# # Run the main loop
# root.mainloop()

import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        self.root = root
        # Setting title
        root.title("EOG Calculator")
        # Setting window size
        width = 613
        height = 529
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg='#020d11')

        # Initialize cursor position
        self.cursor_x = 2
        self.cursor_y = 2

        # Create entry widget for input
        self.entry = tk.Entry(root)
        self.entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=28)
        self.entry["font"] = ft
        self.entry["fg"] = "#333333"
        self.entry["justify"] = "center"
        self.entry["text"] = "Entry"
        self.entry.place(x=70, y=60, width=471, height=52)

        # Create label for center
        self.GLabel_267 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=13)
        self.GLabel_267["font"] = ft
        self.GLabel_267["fg"] = "#333333"
        self.GLabel_267["justify"] = "center"
        self.GLabel_267["text"] = "Center"
        self.GLabel_267.place(x=270, y=290, width=70, height=25)

        # Draw initial cursor
        self.redraw_cursor()

        # Bind arrow keys and space key
        root.bind("<Up>", self.move_cursor)
        root.bind("<Down>", self.move_cursor)
        root.bind("<Left>", self.move_cursor)
        root.bind("<Right>", self.move_cursor)
        root.bind("<space>", self.toggle_selection)

    def move_cursor(self, event):
        key = event.keysym
        if key == "Up" and self.cursor_y > 0:
            self.cursor_y -= 1
        elif key == "Down" and self.cursor_y < 4:
            self.cursor_y += 1
        elif key == "Left" and self.cursor_x > 0:
            self.cursor_x -= 1
        elif key == "Right" and self.cursor_x < 4:
            self.cursor_x += 1

        self.redraw_cursor()

    def toggle_selection(self, event):
        self.press_button_under_cursor()

    def press_button_under_cursor(self):
        row = self.cursor_y
        col = self.cursor_x

        # Depending on the button's action, you can add logic here
        print(f"Pressed button at row {row}, column {col}")

    def redraw_cursor(self):
        # Remove previous cursor
        self.remove_cursor()

        # Create new cursor
        cell_size = 50
        x1 = 70 + self.cursor_x * cell_size
        y1 = 60 + self.cursor_y * cell_size
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        self.cursor = self.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")

    def create_rectangle(self, x1, y1, x2, y2, fill, outline):
        return self.root.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)

    def remove_cursor(self):
        try:
            self.root.delete(self.cursor)
        except AttributeError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


