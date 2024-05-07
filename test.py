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
        root.geometry(f"{width}x{height}")
        root.resizable(width=False, height=False)
        root.configure(bg='#020d11')

        # Initialize cursor position
        self.cursor_x = 290
        self.cursor_y = 275

        # Create entry widget for input
        self.entry = tk.Entry(root)
        self.entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=28)
        self.entry["font"] = ft
        self.entry["fg"] = "#333333"
        self.entry["justify"] = "center"
        self.entry["text"] = "Entry"
        self.entry.place(x=70, y=60, width=471, height=52)


        self.GLineEdit_383=tk.Entry(root)
        self.GLineEdit_383["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=28)
        self.GLineEdit_383["font"] = ft
        self.GLineEdit_383["fg"] = "#333333"
        self.GLineEdit_383["justify"] = "center"
        self.GLineEdit_383["text"] = "Entry"
        self.GLineEdit_383.place(x=70,y=60,width=471,height=52)

        GButton_278=tk.Button(root)
        GButton_278["activebackground"] = "#a02010"
        GButton_278["bg"] = "#78d8f1"
        GButton_278["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_278["font"] = ft
        GButton_278["fg"] = "#020d11"
        GButton_278["justify"] = "center"
        GButton_278["text"] = "1"
        GButton_278.place(x=180,y=180-5,width=70,height=25)
        GButton_278["command"] = lambda: self.display_input("1")

        GButton_594=tk.Button(root)
        GButton_594["activebackground"] = "#a02010"
        GButton_594["bg"] = "#78d8f1"
        GButton_594["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_594["font"] = ft
        GButton_594["fg"] = "#020d11"
        GButton_594["justify"] = "center"
        GButton_594["text"] = "2"
        GButton_594.place(x=270,y=180-5,width=70,height=25)
        GButton_594["command"] = lambda: self.display_input("2")

        GButton_643=tk.Button(root)
        GButton_643["activebackground"] = "#a02010"
        GButton_643["bg"] = "#78d8f1"
        GButton_643["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_643["font"] = ft
        GButton_643["fg"] = "#020d11"
        GButton_643["justify"] = "center"
        GButton_643["text"] = "3"
        GButton_643.place(x=360,y=180-5,width=70,height=25)
        GButton_643["command"] = lambda: self.display_input("3")

        GButton_113=tk.Button(root)
        GButton_113["activebackground"] = "#a02010"
        GButton_113["bg"] = "#78d8f1"
        GButton_113["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_113["font"] = ft
        GButton_113["fg"] = "#020d11"
        GButton_113["justify"] = "center"
        GButton_113["text"] = "4"
        GButton_113.place(x=70,y=240-15,width=70,height=25)
        GButton_113["command"] = lambda: self.display_input("4")

        GButton_396=tk.Button(root)
        GButton_396["activebackground"] = "#a02010"
        GButton_396["bg"] = "#78d8f1"
        GButton_396["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_396["font"] = ft
        GButton_396["fg"] = "#020d11"
        GButton_396["justify"] = "center"
        GButton_396["text"] = "5"
        GButton_396.place(x=70,y=290-15,width=70,height=25)
        GButton_396["command"] = lambda: self.display_input("5")

        GButton_971=tk.Button(root)
        GButton_971["activebackground"] = "#a02010"
        GButton_971["bg"] = "#78d8f1"
        GButton_971["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_971["font"] = ft
        GButton_971["fg"] = "#020d11"
        GButton_971["justify"] = "center"
        GButton_971["text"] = "6"
        GButton_971.place(x=70,y=340-15,width=70,height=25)
        GButton_971["command"] = lambda: self.display_input("6")

        GButton_560=tk.Button(root)
        GButton_560["activebackground"] = "#a02010"
        GButton_560["activeforeground"] = "#ffffff"
        GButton_560["bg"] = "#78d8f1"
        GButton_560["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_560["font"] = ft
        GButton_560["fg"] = "#020d11"
        GButton_560["justify"] = "center"
        GButton_560["text"] = "7"
        GButton_560.place(x=470,y=240-15,width=70,height=25)
        GButton_560["command"] = lambda: self.display_input("7")

        GButton_61=tk.Button(root)
        GButton_61["activebackground"] = "#a02010"
        GButton_61["bg"] = "#78d8f1"
        GButton_61["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_61["font"] = ft
        GButton_61["fg"] = "#020d11"
        GButton_61["justify"] = "center"
        GButton_61["text"] = "8"
        GButton_61.place(x=470,y=290-15,width=70,height=25)
        GButton_61["command"] = lambda: self.display_input("8")

        GButton_383=tk.Button(root)
        GButton_383["activebackground"] = "#a02010"
        GButton_383["bg"] = "#78d8f1"
        GButton_383["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_383["font"] = ft
        GButton_383["fg"] = "#020d11"
        GButton_383["justify"] = "center"
        GButton_383["text"] = "9"
        GButton_383.place(x=470,y=340-15,width=70,height=25)
        GButton_383["command"] = lambda: self.display_input("9")

        GButton_10=tk.Button(root)
        GButton_10["activebackground"] = "#a02010"
        GButton_10["bg"] = "#eca03d"
        GButton_10["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_10["font"] = ft
        GButton_10["fg"] = "#020d11"
        GButton_10["justify"] = "center"
        GButton_10["text"] = "E"
        GButton_10.place(x=180,y=400-25,width=70,height=25)
        GButton_10["command"] = lambda: self.exit()

        GButton_508=tk.Button(root)
        GButton_508["activebackground"] = "#ffffff"
        GButton_508["bg"] = "#78d8f1"
        GButton_508["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_508["font"] = ft
        GButton_508["fg"] = "#020d11"
        GButton_508["justify"] = "center"
        GButton_508["text"] = "0"
        GButton_508.place(x=270,y=400-25,width=70,height=25)
        GButton_508["command"] = lambda: self.display_input("0")

        GButton_40=tk.Button(root)
        GButton_40["activebackground"] = "#ffffff"
        GButton_40["bg"] = "#eca03d"
        GButton_40["borderwidth"] = "0px"
        ft = tkFont.Font(family='Times',size=13)
        GButton_40["font"] = ft
        GButton_40["fg"] = "#020d11"
        GButton_40["justify"] = "center"
        GButton_40["text"] = "C"
        GButton_40.place(x=360,y=400-25,width=70,height=25)
        GButton_40["command"] = lambda: self.clear()

        GButton_139=tk.Button(root)
        GButton_139["bg"] = "#a02010"
        GButton_139["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=18)
        GButton_139["font"] = ft
        GButton_139["fg"] = "#ffffff"
        GButton_139["justify"] = "center"
        GButton_139["text"] = "/"
        GButton_139.place(x=200,y=320-20,width=70,height=25)
        GButton_139["command"] = lambda: self.display_input("/")

        GButton_624=tk.Button(root)
        GButton_624["activebackground"] = "#ffffff"
        GButton_624["bg"] = "#a02010"
        GButton_624["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=18)
        GButton_624["font"] = ft
        GButton_624["fg"] = "#ffffff"
        GButton_624["justify"] = "center"
        GButton_624["text"] = "+"
        GButton_624.place(x=200,y=260-10,width=70,height=25)
        GButton_624["command"] = lambda: self.display_input("+")

        GButton_810=tk.Button(root)
        GButton_810["bg"] = "#a02010"
        GButton_810["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=18)
        GButton_810["font"] = ft
        GButton_810["fg"] = "#ffffff"
        GButton_810["justify"] = "center"
        GButton_810["text"] = "-"
        GButton_810.place(x=340,y=260-10,width=70,height=25)
        GButton_810["command"] = lambda: self.display_input("-")

        GButton_947=tk.Button(root)
        GButton_947["bg"] = "#a02010"
        GButton_947["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=18)
        GButton_947["font"] = ft
        GButton_947["fg"] = "#ffffff"
        GButton_947["justify"] = "center"
        GButton_947["text"] = "*"
        GButton_947.place(x=340,y=320-20,width=70,height=25)
        GButton_947["command"] = lambda: self.display_input("*")

        # Save button positions to an array
        self.buttons = [GButton_278, GButton_594, GButton_643, GButton_113, GButton_396, GButton_971, GButton_560, GButton_61, GButton_383, GButton_10, GButton_508, GButton_40, GButton_139, GButton_624, GButton_810, GButton_947]
        GLabel_267=tk.Label(root)

        ft = tkFont.Font(family='Times',size=13)
        GLabel_267["font"] = ft
        GLabel_267["fg"] = "#333333"
        GLabel_267["justify"] = "center"
        GLabel_267["text"] = "Center"
        GLabel_267.place(x=270,y=290-15,width=70,height=25)
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
        if key == "Up":
            self.cursor_y = max(0, self.cursor_y - 25)
        elif key == "Down":
            self.cursor_y = min(529, self.cursor_y + 25)
        elif key == "Left":
            self.cursor_x = max(0, self.cursor_x - 25)
        elif key == "Right":
            self.cursor_x = min(613, self.cursor_x + 25)

        print(f"Cursor Position: X={self.cursor_x}, Y={self.cursor_y}")
        self.redraw_cursor()

    def toggle_selection(self, event):
        for button in self.buttons:
            if self.is_cursor_over_button(button):
                self.on_button_pressed(button)

    def on_button_pressed(self, button):
        button.invoke()
        self.cursor_x = 290
        self.cursor_y = 275
        self.redraw_cursor()
        # self.entry.insert(tk.END, "Button Pressed")

    def is_cursor_over_button(self, button):
        button_x1 = button.winfo_x()
        button_y1 = button.winfo_y()
        button_x2 = button_x1 + button.winfo_width()
        button_y2 = button_y1 + button.winfo_height()
        return button_x1 <= self.cursor_x <= button_x2 and button_y1 <= self.cursor_y <= button_y2

    def redraw_cursor(self):
        # Remove previous cursor
        self.remove_cursor()

        # Create new cursor
        cell_size = 25
        x1 = self.cursor_x
        y1 = self.cursor_y
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        self.cursor = self.create_cursor_label(x1, y1, x2, y2, bg="blue")

    def create_cursor_label(self, x1, y1, x2, y2, **kwargs):
        cursor_label = tk.Label(self.root, **kwargs)
        cursor_label.place(x=x1, y=y1, width=x2-x1, height=y2-y1)
        return cursor_label

    def remove_cursor(self):
        try:
            self.cursor.destroy()
        except AttributeError:
            pass
    def display_input(self, text):
        self.GLineEdit_383.insert(tk.END, text)
        if len(self.GLineEdit_383.get()) == 3:
            self.solve_equation()

    def clear(self):
        self.GLineEdit_383.delete(0, tk.END)
        
    def exit(self):
        self.root.destroy()    

    def solve_equation(self):
        equation = self.GLineEdit_383.get()
        try:
            result = eval(equation)
            self.GLineEdit_383.insert(tk.END, "= "+str(result))
        except:
            self.GLineEdit_383.delete(0, tk.END)
            self.GLineEdit_383.insert(tk.END, "Invalid equation")
   
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


