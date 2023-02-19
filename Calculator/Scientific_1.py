#importing tkinter module
import tkinter as tk
from tkinter import messagebox
LIGHT_GREY="#5F5F5F"
WHITE="#FFFFFF"
OFF_WHITE="#F8FAFF"
LIGHT_BLUE="lightblue"
LIGHT_GREEN="lightgreen"

LARGE_BUTTON_FONT=("Arial",34,"bold")
DIGIT_BUTTON_FONT=("Arial",24,"bold")
DEFAULT_BUTTON_FONT=("Arial",20,"bold")
SMALL_BUTTON_FONT=("Arial",16)

class Calculator:
    def __init__(self) -> None:

    #To Design Basic Empty Window
        self.window=tk.Tk()         # Creating GUI Window
        self.window.geometry("400x600")     #Setting Boundaries
        self.window.resizable(0,0)          #To stop resizing
        self.window.title("calculator")     #Setting Title of Window
        self.window.configure(bg=LIGHT_GREY)

        self.overall_expression=""
        self.active_expression=""  
        
    # creating frames
        self.display_frame=self.create_display_frame()
        self.buttons_frame=self.create_buttons_frame()

    #creating labels
        self.overall_label,self.active_label=self.display_labels()

    #creating digit buttons
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,1),'.':(4,2)
        }
        

    #creating operations buttons
        self.operations={

            "/":u'\u00F7' ,"*":u'\u00D7' ,"-":"-" ,"+":"+" 
        }

        #Buttons creation
        self.create_buttons()
        self.create_equal_button()
        self.create_clear_button()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

        # To fill the entire buttons frame
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)

    def bind_keys(self):
        self.window.bind("<Return>", lambda event :self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event, digit=key:self.add_expression(digit))
        for key in self.operations:
            self.window.bind(str(key),lambda event, digit=key:self.add_operations(digit))

        self.window.bind("c",lambda event:self.clear())
        self.window.bind("=",lambda event:self.evaluate())
        self.window.bind("%",lambda event:self.add_operations("%"))
        self.window.bind("^",lambda event:self.square())
        self.window.bind("r",lambda event:self.squareroot())
    def display_labels(self):
        upper_label=tk.Label(self.display_frame,text=self.overall_expression,anchor=tk.E,font=SMALL_BUTTON_FONT)
        upper_label.pack(expand=True,fill="both")
        lower_label=tk.Label(self.display_frame,text=self.active_expression,anchor=tk.E,font=LARGE_BUTTON_FONT)
        lower_label.pack(expand=False,fill="both")
        return upper_label,lower_label

    def create_display_frame(self)->None:
        frame=tk.Frame(self.window,height=20)
        frame.pack(expand=True,fill="both")
        return frame
    

    def create_buttons_frame(self)->None:
        frame=tk.Frame(self.window,height=100,bg="white",)
        frame.pack(expand=True,fill="both")
        return frame
    
    def create_buttons(self):
        for digit,grid_values in self.digits.items():
            button=tk.Button(self.buttons_frame,text=str(digit),bg="WHITE",activeforeground="black",font=DIGIT_BUTTON_FONT,borderwidth=0.5,command=lambda x=digit:self.add_expression(x),activebackground=LIGHT_GREEN)
            button.grid(row=grid_values[0],column=grid_values[1],sticky=tk.NSEW)

    def create_operator_buttons(self):
        i=0
        for operator,symbol in self.operations.items():
            button=tk.Button(self.buttons_frame,text=symbol,bg="lightblue",fg="black",font=DIGIT_BUTTON_FONT,activeforeground="black",command=lambda x=operator:self.add_operations(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def create_clear_button(self):    
        button=tk.Button(self.buttons_frame,text="C",bg=LIGHT_GREEN,font=DIGIT_BUTTON_FONT,borderwidth=0.5,command=self.clear,activeforeground="black",activebackground="red")
        button.grid(row=0,column=1,sticky=tk.NSEW)

    def create_equal_button(self):
        button=tk.Button(self.buttons_frame,text="=",bg=LIGHT_GREEN,font=DIGIT_BUTTON_FONT,borderwidth=0.5,command=self.evaluate,activeforeground="black",border=1)
        button.grid(row=4,column=3,sticky=tk.NSEW)

    def create_special_buttons(self):
        button=tk.Button(self.buttons_frame,text="%",bg="lightblue",fg="black",font=DIGIT_BUTTON_FONT,borderwidth=0.5,command=lambda x="%":self.add_operations(x))
        button.grid(row=4,column=4,sticky=tk.NSEW)
        button=tk.Button(self.buttons_frame,text="x\u00b2",bg="lightblue",fg="black",font=DIGIT_BUTTON_FONT,borderwidth=0.5,command=self.square)
        button.grid(row=0,column=2,sticky=tk.NSEW)
        button=tk.Button(self.buttons_frame,text="\u221a",bg="lightblue",fg="black",font=DIGIT_BUTTON_FONT,borderwidth=0.5,command=self.squareroot)
        button.grid(row=0,column=3,sticky=tk.NSEW)

    def create_scientific_buttons(self):
        pass
    def square(self):
        self.active_expression=str(eval(f"{self.active_expression}**2"))
        self.update_label()
    def squareroot(self):
        self.active_expression=str(eval(f"{self.active_expression}**0.5"))
        self.update_label()

    def evaluate(self):
        self.overall_expression+=self.active_expression
        self.update_total_label()
        try:
            self.active_expression=str(eval(self.overall_expression))
        except Exception as e:
            self.active_expression="Error"
        finally:
            self.overall_expression=""
            self.update_total_label
            self.update_label()
        

    def clear(self):
        self.active_expression=""
        self.overall_expression=""
        self.update_label()
        self.update_total_label()

    def add_expression(self,digit):
        self.active_expression+=str(digit)
        self.update_label()

    def add_operations(self,operator):
        self.active_expression+=operator
        self.overall_expression+=self.active_expression
        self.active_expression=""
        self.update_label()
        self.update_total_label()

    def update_label(self):
        self.active_label.config(text=self.active_expression[:16])

    def update_total_label(self):
        self.overall_label.config(text=self.overall_expression)

    #scientific 
   

    def run(self)->None:
        self.window.mainloop()   #To Make the Window run again and agian(to make active) untill we close it
        

cl=Calculator()
cl.run()
    
