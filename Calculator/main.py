from tkinter import *


calc = Tk()
calc.title("Calculator")
calc.call('wm', 'iconphoto', calc._w, PhotoImage(file='icon.gif'))
calc.tk_setPalette(background='gray20')

operator = ''
text_input = StringVar()

# functions
def button_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def button_clear_display():
    global operator
    operator = ''
    text_input.set('')


def button_eql_inp():
    global operator
    total = str(eval(operator))
    text_input.set(total)
    operator = ''


# calculator
txt_display = Entry(calc, font=('Source Code Pro', 20), textvar=text_input, bd=20, fg='black', insertwidth=4,
                    bg='DarkOliveGreen4', justify='right')
txt_display.grid(columnspan=4)

button7 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='7', bg='RoyalBlue4',
                 command=lambda: button_click(7)).grid(row=2, column=0)
button8 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='8', bg='RoyalBlue4',
                 command=lambda: button_click(8)).grid(row=2, column=1)
button9 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='9', bg='RoyalBlue4',
                 command=lambda: button_click(9)).grid(row=2, column=2)
addition = Button(calc, padx=16, pady=16, bd=8, fg='black', font=('calibri', 20, 'bold'), text='+', bg='light grey',
                  command=lambda: button_click('+')).grid(row=2, column=3)
# ----------------------------------------------------------------------------------------------------------------------
button4 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='4', bg='RoyalBlue4',
                 command=lambda: button_click(4)).grid(row=3, column=0)
button5 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='5', bg='RoyalBlue4',
                 command=lambda: button_click(5)).grid(row=3, column=1)
button6 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='6', bg='RoyalBlue4',
                 command=lambda: button_click(6)).grid(row=3, column=2)
subtraction = Button(calc, padx=16, pady=16, bd=8, fg='black', font=('calibri', 20, 'bold'), text='- ', bg='light grey',
                     command=lambda: button_click('-')).grid(row=3, column=3)
# ----------------------------------------------------------------------------------------------------------------------
button1 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='1', bg='RoyalBlue4',
                 command=lambda: button_click(1)).grid(row=4, column=0)
button2 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='2', bg='RoyalBlue4',
                 command=lambda: button_click(2)).grid(row=4, column=1)
button3 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='3', bg='RoyalBlue4',
                 command=lambda: button_click(3)).grid(row=4, column=2)
multiplication = Button(calc, padx=16, pady=16, bd=8, fg='black', font=('calibri', 20, 'bold'), text='*', bg='light grey',
                        command=lambda: button_click('*')).grid(row=4, column=3)
# ----------------------------------------------------------------------------------------------------------------------
button0 = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='0', bg='RoyalBlue4',
                 command=lambda: button_click(0)).grid(row=5, column=0)
clear = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='C', bg='DodgerBlue3',
               command=lambda: button_clear_display()).grid(row=5, column=1)
equal = Button(calc, padx=16, pady=16, bd=8, fg='white', font=('calibri', 20, 'bold'), text='=', bg='DodgerBlue3',
               command=lambda: button_eql_inp()).grid(row=5, column=2)
division = Button(calc, padx=16, pady=16, bd=8, fg='black', font=('calibri', 20, 'bold'), text='/', bg='light grey',
                  command=lambda: button_click('/')).grid(row=5, column=3)


calc.mainloop()
