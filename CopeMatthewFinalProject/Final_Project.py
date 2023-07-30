#Author: Matthew Cope
#Date: 7/24/23
#Assignment: Final Project
#Description: A calculator that will  calculate your yearly and monthly income
from tkinter import *

calc = Tk()

# The introduction
calc.title('Wage calculator')
calc.geometry("360x125")
label1 = Label(calc, text = "Hello!").pack()
label2 = Label(calc, text = "Please select an option").pack()




def Yin():

    p2 = Toplevel()

    #Yearly Calculation
    def calcyin():
         hours = float(hw.get())
         rate = float(epr.get())
         mult = hours * rate
         Yincome = mult * 52
         labelresult = Label(p2, text = "Your Yearly income is: $%s " % Yincome).pack()
         Exit = Button(p2, text = "Back", command = p2.destroy).pack() 
         return

    # Defining variables        
    hw = StringVar()
    epr = StringVar()


    # Geting yearly info
    label3 = Label(p2, text = "please enter number of hours worked per week.").pack()
    rep1 = Entry(p2, textvariable = hw).pack()
    label4 = Label(p2, text = "please enter earnings per hour.").pack()
    rep2 = Entry(p2, textvariable = epr).pack()
    button3 = Button(p2, text = "Calculate", command = calcyin).pack()

button1 = Button(calc, text = "yearly", command = Yin).pack()

def Min():
    p3 = Toplevel()

    #monthly Calculation
    def calcmin():
        hours = float(hw.get())
        rate = float(epr.get())
        mult = hours * rate
        mult2 = mult * 52
        Mincome = mult2 / 12
        labelresult = Label(p3, text = "Your Monthly income is: $%s " % Mincome).pack()
        Exit = Button(p3, text = "Back", command = p3.destroy).pack()
        return

     # Defining variables        
    hw = StringVar()
    epr = StringVar()

    # Geting monthly info
    label5 = Label(p3, text = "please enter number of hours worked per week.").pack()
    rep3 = Entry(p3, textvariable = hw).pack()
    label6 = Label(p3, text = "please enter your earnings per hour.").pack()
    rep4 = Entry(p3, textvariable = epr).pack()
    button4 = Button(p3, text = "Calculate", command = calcmin).pack()






button2 = Button(calc, text = "monthly", command = Min).pack()
Exit = Button(calc, text = "Exit", command = calc.quit).pack()










calc.mainloop()
