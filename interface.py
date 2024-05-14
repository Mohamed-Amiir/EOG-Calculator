import tkinter as tk
import tkinter.font as tkFont
import time
import main, Classification as CL
import backend 
# load the ML model
Model = CL.LoadModel('SVM')
# load test signals
TestSignels = main.Get_Prepared_Signals(1)

class Button:
    position = (0, 0)
    size = (0, 0)
    default_color = "#78d8f1"
    button_function = None
    def __init__(self, position, size):
        self.position = position
        self.size = size
        self.button_function = tk.Button(root)

class Cursor:
    size = (70, 70)
    current_button = None
    def __init__(self, current_button:Button, size):
        self.size = size
        self.current_button = current_button

class App:
    def __init__(self, root):
        self.root = root
        # Setting title
        root.title("EOG Calculator")
        # Setting window size
        width = 680
        height = 500
        root.geometry(f"{width}x{height}")
        root.resizable(width=False, height=False)
        root.configure(bg='#020d11')

        # Create all button objects
        self.main = Button((280, 250), (120, 120))
        self.one = Button((210, 180), (80, 40))
        self.two = Button((300, 180), (80, 40))
        self.three = Button((390, 180), (80, 40))
        self.four = Button((100, 240), (80, 40))
        self.five = Button((100, 290), (80, 40))
        self.six = Button((100, 340), (80, 40))
        self.seven = Button((500, 240), (80, 40))
        self.eight = Button((500, 290), (80, 40))
        self.nine = Button((500, 340), (80, 40))
        self.zero = Button((300, 400), (80, 40))
        self.exit = Button((210, 400), (80, 40))
        self.clear = Button((390, 400), (80, 40))
        self.divide = Button((300, 450), (80, 40))
        self.add = Button((300, 130), (80, 40))
        self.subtract = Button((10, 290), (80, 40))
        self.multiply = Button((590, 290), (80, 40))

        self.buttons = [self.zero,self.one,self.two,self.three,self.four,self.five,self.six,self.seven,self.eight,self.nine]

        self.cursor = Cursor(self.main, (130,130))

        for i in range(len(self.buttons)):
            self.buttons[i].button_function["activebackground"] = "#a02010"
            self.buttons[i].button_function["bg"] = self.buttons[i].default_color
            self.buttons[i].button_function["borderwidth"] = "0px"
            ft = tkFont.Font(family='Helvetica', size=13)
            self.buttons[i].button_function["font"] = ft
            self.buttons[i].button_function["fg"] = "#020d11"
            self.buttons[i].button_function["justify"] = "center"
            self.buttons[i].button_function["text"] = str(i)
            self.buttons[i].button_function.place(x=self.buttons[i].position[0], y=self.buttons[i].position[1], width=self.buttons[i].size[0], height=self.buttons[i].size[1])
            self.buttons[i].button_function["command"] = lambda i=i: self.display_input(str(i))

        


        # self.multiply.button_function["command"] = lambda: self.display_input("*")
        # Create entry widget for input
        # self.entry = tk.Entry(root)
        # self.entry["borderwidth"] = "1px"
        # ft = tkFont.Font(family='Times', size=28)
        # self.entry["font"] = ft
        # self.entry["fg"] = "#333333"
        # self.entry["justify"] = "center"
        # self.entry["text"] = "Entry"
        # self.entry.place(x=60, y=60, width=500, height=52)


        self.GLineEdit_383=tk.Entry(root)
        self.GLineEdit_383["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=28)
        self.GLineEdit_383["font"] = ft
        self.GLineEdit_383["fg"] = "#333333"
        self.GLineEdit_383["justify"] = "center"
        self.GLineEdit_383["text"] = "Entry"
        self.GLineEdit_383.place(x=40,y=60,width=600,height=52)

        self.exit.button_function["activebackground"] = "#a02010"
        self.exit.default_color = "#eca03d"
        self.exit.button_function["bg"] = "#eca03d"
        self.exit.button_function["borderwidth"] = "5px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.exit.button_function["font"] = ft
        self.exit.button_function["fg"] = "#020d11"
        self.exit.button_function["justify"] = "center"
        self.exit.button_function["text"] = "Exit"
        self.exit.button_function.place(x=self.exit.position[0],y=self.exit.position[1],width=self.exit.size[0],height=self.exit.size[1])
        self.exit.button_function["command"] = lambda: self.exit_window()

        self.clear.button_function["activebackground"] = "black"
        self.clear.default_color = "#eca03d"
        self.clear.button_function["bg"] = "#eca03d"
        self.clear.button_function["borderwidth"] = "5px"
        ft = tkFont.Font(family='Helvetica',size=13)
        self.clear.button_function["font"] = ft
        self.clear.button_function["fg"] = "#020d11"
        self.clear.button_function["justify"] = "center"
        self.clear.button_function["text"] = "Clear"
        self.clear.button_function.place(x=self.clear.position[0],y=self.clear.position[1],width=self.clear.size[0],height=self.clear.size[1])
        self.clear.button_function["command"] = lambda: self.clear_eq()

        self.divide.default_color = "#a02010"
        self.divide.button_function["bg"] = "#a02010"
        self.divide.button_function["borderwidth"] = "5px"
        ft = tkFont.Font(family='Helvetica',size=18)
        self.divide.button_function["font"] = ft
        self.divide.button_function["fg"] = "black"
        self.divide.button_function["justify"] = "center"
        self.divide.button_function["text"] = "/"
        self.divide.button_function.place(x=self.divide.position[0],y=self.divide.position[1],width=self.divide.size[0],height=self.divide.size[1])
        self.divide.button_function["command"] = lambda: self.display_input("/")

        self.add.default_color = "#a02010"
        self.add.button_function["activebackground"] = "#ffffff"
        self.add.button_function["bg"] = "#a02010"
        self.add.button_function["borderwidth"] = "5px"
        ft = tkFont.Font(family='Helvetica',size=18)
        self.add.button_function["font"] = ft
        self.add.button_function["fg"] = "black"
        self.add.button_function["justify"] = "center"
        self.add.button_function["text"] = "+"
        self.add.button_function.place(x=self.add.position[0],y=self.add.position[1],width=self.add.size[0],height=self.add.size[1])
        self.add.button_function["command"] = lambda: self.display_input("+")

        self.subtract.default_color = "#a02010"
        self.subtract.button_function["bg"] = "#a02010"
        self.subtract.button_function["borderwidth"] = "5px"
        ft = tkFont.Font(family='Helvetica',size=18)
        self.subtract.button_function["font"] = ft
        self.subtract.button_function["fg"] = "black"
        self.subtract.button_function["justify"] = "center"
        self.subtract.button_function["text"] = "-"
        self.subtract.button_function.place(x=self.subtract.position[0],y=self.subtract.position[1],width=self.subtract.size[0],height=self.subtract.size[1])
        self.subtract.button_function["command"] = lambda: self.display_input("-")

        self.multiply.default_color = "#a02010"
        self.multiply.button_function["bg"] = "#a02010"
        self.multiply.button_function["borderwidth"] = "5px"
        ft = tkFont.Font(family='Helvetica',size=18)
        self.multiply.button_function["font"] = ft
        self.multiply.button_function["fg"] = "black"
        self.multiply.button_function["justify"] = "center"
        self.multiply.button_function["text"] = "x"
        self.multiply.button_function.place(x=self.multiply.position[0],y=self.multiply.position[1],width=self.multiply.size[0],height=self.multiply.size[1])
        self.multiply.button_function["command"] = lambda: self.display_input("*")

        # Save button positions to an array
        # self.buttons = [GButton_278, self.two.button_function, self.three.button_function, GButton_113, GButton_396, GButton_971, GButton_560, GButton_61, GButton_383, self.exit.button_function, GButton_508, self.clear.button_function, self.divide.button_function, self.add.button_function, self.subtract.button_function, self.multiply.button_function]
        
        self.main.button_function["activebackground"] = "#a02010"
        self.main.button_function["bg"] = "#78d8f1"
        self.main.button_function["borderwidth"] = "0px"
        ft = tkFont.Font(family='Helvetica', size=13)
        self.main.button_function["font"] = ft
        self.main.button_function["fg"] = "black"
        self.main.button_function["justify"] = "center"
        self.main.button_function["text"] = "Calculate"
        self.main.button_function.place(x=self.main.position[0], y=self.main.position[1], width=self.main.size[0], height=self.main.size[1])
        self.main.button_function["command"] = lambda: self.display_input("calculate")

        self.redraw_cursor(self.cursor.current_button)
        self.first_move = False
        self.second_move = False
        self.direction = -1
        # Bind arrow keys and space key
        root.bind("<Up>", self.move_cursor)
        root.bind("<Down>", self.move_cursor)
        root.bind("<Left>", self.move_cursor)
        root.bind("<Right>", self.move_cursor)
        root.bind("<space>", self.move_cursor)

    def move_cursor(self, event):
        key = event.keysym
        ##################################################################################
        if key == "Up":
            self.direction = 4
        elif key == "Down":
            self.direction = 1
        elif key == "Left":
            self.direction = 2
        elif key == "Right":
            self.direction = 3
        elif key == "space":
            self.direction = 0

        prediction = backend.GetMovement(Model, TestSignels, self.direction) 
        
        move = ""
        if prediction == 0:
            move = "Blink"
        elif prediction == 1:
            move = "Down"
        elif prediction == 2:
            move = "Left"
        elif prediction == 3:
            move = "Right"
        elif prediction == 4:
            move = "Up"        

        ##################################################################################
        if move == "Up":
            if (self.cursor.current_button == self.main):
                self.cursor.current_button = self.two
            elif self.cursor.current_button == self.zero:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.nine:
                self.cursor.current_button = self.eight
            elif self.cursor.current_button == self.eight:
                self.cursor.current_button = self.seven
            elif self.cursor.current_button == self.six:
                self.cursor.current_button = self.five
            elif self.cursor.current_button == self.five:
                self.cursor.current_button = self.four
            elif self.cursor.current_button == self.clear:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.exit:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.divide:
                self.cursor.current_button = self.zero
            elif self.cursor.current_button == self.two or self.cursor.current_button == self.three or self.cursor.current_button == self.one:
                self.cursor.current_button = self.add
        
        elif move == "Down":
            if (self.cursor.current_button == self.main):
                self.cursor.current_button = self.zero
            elif self.cursor.current_button == self.two:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.seven:
                self.cursor.current_button = self.eight
            elif self.cursor.current_button == self.eight:
                self.cursor.current_button = self.nine
            elif self.cursor.current_button == self.four:
                self.cursor.current_button = self.five
            elif self.cursor.current_button == self.five:
                self.cursor.current_button = self.six
            elif self.cursor.current_button == self.one:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.three:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.zero or self.cursor.current_button == self.clear or self.cursor.current_button == self.exit:
                self.cursor.current_button = self.divide
            elif self.cursor.current_button == self.add:
                self.cursor.current_button = self.two
        
        elif move == "Left":
            if (self.cursor.current_button == self.main):
                self.cursor.current_button = self.five
            elif self.cursor.current_button == self.two:
                self.cursor.current_button = self.one
            elif self.cursor.current_button == self.three:
                self.cursor.current_button = self.two
            elif self.cursor.current_button == self.seven:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.eight:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.nine:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.zero:
                self.cursor.current_button = self.exit
            elif self.cursor.current_button == self.clear:
                self.cursor.current_button = self.zero
            elif self.cursor.current_button == self.multiply:
                self.cursor.current_button = self.eight
            elif self.cursor.current_button == self.five or self.cursor.current_button == self.six or self.cursor.current_button == self.four:
                self.cursor.current_button = self.subtract
    
        elif move == "Right":
            if (self.cursor.current_button == self.main):
                self.cursor.current_button = self.eight
            elif self.cursor.current_button == self.two:
                self.cursor.current_button = self.three
            elif self.cursor.current_button == self.one:
                self.cursor.current_button = self.two
            elif self.cursor.current_button == self.four:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.five:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.six:
                self.cursor.current_button = self.main
            elif self.cursor.current_button == self.zero:
                self.cursor.current_button = self.clear
            elif self.cursor.current_button == self.exit:
                self.cursor.current_button = self.zero
            elif self.cursor.current_button == self.subtract:
                self.cursor.current_button = self.five
            elif self.cursor.current_button == self.eight or self.cursor.current_button == self.seven or self.cursor.current_button == self.nine:
                self.cursor.current_button = self.multiply     
        
        elif move == "Blink":
            self.toggle_selection()

        print(f"Cursor Position: X={self.cursor.current_button.position[0]}, Y={self.cursor.current_button.position[1]}")
        self.redraw_cursor(self.cursor.current_button)

    def toggle_selection(self):
        real_buttons = self.buttons + [self.main, self.subtract, self.add, self.multiply, self.divide, self.clear, self.exit]
        for button in real_buttons:
            if self.cursor.current_button == button:
                self.on_button_pressed(button)
        if (self.cursor.current_button == self.main):
            self.on_button_pressed(self.main)

        self.root.after(100, lambda: self.reset_cursor())

    def reset_cursor(self):
        self.cursor.current_button = self.main
        self.redraw_cursor(self.cursor.current_button)

    def on_button_pressed(self, button):
        self.redraw_cursor(button)
        button.button_function.invoke()
        
        # Schedule changing back to original color after 2 seconds
        self.root.after(100, lambda: self.redraw_cursor(button))

        #################################################TO BE REMOVED########################################################
        if len(self.GLineEdit_383.get()) == 3:
            equation = self.GLineEdit_383.get()
            try:
                result = eval(equation)
                self.GLineEdit_383.delete(0, tk.END)
                self.GLineEdit_383.insert(0, f"{equation} = {result}")
            except:
                self.GLineEdit_383.delete(0, tk.END)
                self.GLineEdit_383.insert(0, "Invalid equation")    
        ####################################################################################################################

    def redraw_cursor(self, the_button):
        # Remove previous cursor
        self.remove_cursor()

        # Create new cursor
        cell_size = 40
        x1 = the_button.position[0]
        y1 = the_button.position[1]
        x2 = x1 + cell_size
        y2 = y1 + cell_size
        the_button.button_function["bg"] = "white"

    def remove_cursor(self):
        real_buttons = self.buttons + [self.main, self.subtract, self.add, self.multiply, self.divide, self.clear, self.exit]
        for button in real_buttons:
            button.button_function["bg"] = button.default_color

    def display_input(self, text):
        if self.GLineEdit_383.get() == "Invalid equation":
            self.GLineEdit_383.delete(0, tk.END)
        if text == "calculate" and self.GLineEdit_383.get() != "":
            self.solve_equation()
        else:
            self.GLineEdit_383.insert(tk.END, text)

    def clear_eq(self):
        self.first_move = False
        self.second_move = False
        self.GLineEdit_383.delete(0, tk.END)

    def exit_window(self):
        self.root.destroy()    

    def solve_equation(self):
        equation = self.GLineEdit_383.get()
        print(f"Result: {equation}")
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

