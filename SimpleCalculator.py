from tkinter import *

#button press action
def button(num):
    global eq_text
    eq_text = eq_text + str(num)
    equationLabel.set(eq_text)
#equal sign button press action
def equals():
    global eq_text
    try:
        total = str(eval(eq_text)) 
        equationLabel.set(total)
        eq_text = total
    except SyntaxError :
        equationLabel.set("Syntax Error")
        eq_text=""
    except ZeroDivisionError:
        equationLabel.set("Zero Divivsion Error")
        eq_text =""

#clear button press action
def clear():
    global eq_text
    equationLabel.set("")
    eq_text = ""

#### Main Program ####
#declare window
window = Tk()
window.title("Basic Calculator")
window.geometry("500x500")
#Equation label declare
eq_text =""
equationLabel = StringVar()
label = Label(window, textvariable=equationLabel, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()
#Generate buttons
button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

window.mainloop()