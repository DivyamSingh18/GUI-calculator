# --------------------------------------------------------------library---------------------------------------------------------------------------
from tkinter import *

# Creating object of class Tk / creating tk window
main = Tk()

# Title of program
main.title("Divyam's Calculator")
main.maxsize(width="410",height="565")
main.minsize(width="410",height="565")
main.iconbitmap('cal.ico')

# ------------------------------------------------------------Variables-------------------------------------------------------------------------
tex = StringVar()
operator = ""

# ------------------------------------------------------------functions-------------------------------------------------------------------------
# for printing result on calc
def result():
    global operator
    if operator=="":
        tex.set("Enter a valid input plz")
    else:    
        try: 
            result= eval(operator)   #   <-  All calculation is done here 
            operator = str(result)
            tex.set(operator)
        except ZeroDivisionError:
            tex.set("can't divide by zero")   
        except Exception:
            tex.set("ERROR")

# for clearing the data on calc
def clear_all():
    global operator
    operator = ""
    tex.set(operator)

# for using the virtual numpad of calc
def click(num):
    global operator
    operator+= str(num)
    tex.set(operator)


#------------------------------------------------------------ Entry Bar--------------------------------------------------------------------------
entry1 = Entry(main,bg="aquamarine2",font=('arial',27,"bold",),justify='right',bd=5, textvariable=tex)
entry1.grid(row=0,column=0,columnspan=4)

# _____________________________________________________________Buttons (GUI)_______________________________________________________________________
# 7
btn7 = Button(main, activebackground="grey", text="7", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(7))
btn7.grid(row=1, column=0)
# 8
btn8 = Button(main, text="8",activebackground="grey", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(8))
btn8.grid(row=1, column=1)
# 9
btn9 = Button(main, text="9", activebackground="grey", bg="light grey", font=("arial", 20,'bold'), padx="28", pady='25', bd="3", command=lambda:click(9))
btn9.grid(row=1, column=2)
# +
btn_add = Button(main, text="+",activebackground="grey", bg="mistyrose2", font=("arial",20,'bold'), padx="28", pady='25', bd="3", command=lambda:click('+'))
btn_add.grid(row=1, column=3)
# 4
btn7 = Button(main, text="4", activebackground="grey", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(4))
btn7.grid(row=2, column=0, pady=(3, 3))
# 5
btn8 = Button(main, text="5", activebackground="grey", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(5))
btn8.grid(row=2, column=1)
# 6
btn9 = Button(main, text="6", activebackground="grey", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(6))
btn9.grid(row=2, column=2)
# -
btn_sub = Button(main, text="-", activebackground="grey", bg="mistyrose2", font=("arial", 20, 'bold'),padx="31", pady='25', bd="3", command=lambda:click('-'))
btn_sub.grid(row=2, column=3)
# 1
btn1 = Button(main,text="1", activebackground="grey", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(1))
btn1.grid(row=3, column=0, pady=(2,2))
# 2
btn2 = Button(main, text="2", activebackground="grey", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(2))
btn2.grid(row=3, column=1)
# 3
btn3 = Button(main, text="3", activebackground="grey", bg="light grey", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click(3))
btn3.grid(row=3, column=2)
# *
btn_mul = Button(main, text="x", activebackground="grey", bg="mistyrose2", font=("arial", 20, 'bold'), padx="28", pady='25', bd="3", command=lambda:click('*'))
btn_mul.grid(row=3, column=3)
# 0
btn0 = Button(main, text="0", activebackground="grey", bg="light grey", font=("arial",20,'bold'), padx="28", pady='25', bd="3", command=lambda:click(0))
btn0.grid(row=4, column=0, pady=(2,2))
# =
btn8 = Button(main, text="=", activebackground="grey", bg="mistyrose2", font=("arial", 20, 'bold'), padx="80", pady='25', bd="3", command=result)
btn8.grid(row=4, column=1, columnspan=2)
# /
btn_div = Button(main, text="/",activebackground="grey", bg="mistyrose2", font=("arial", 20, 'bold'), padx="31", pady='25', bd="3", command=lambda:click('/'))
btn_div.grid(row=4, column=3)
# .
btn0 = Button(main, text=".", activebackground="grey", bg="light grey", font=("arial" ,20 ,'bold'), padx="32", pady='5', bd="3", command=lambda:click("."))
btn0.grid(row=5, column=0, pady=(2,2))
# clear all
btn_div = Button(main, text="clear all", activebackground="orange red", bg="orange", font=("arial", 20,'bold'), padx="86", pady='5', bd="3", command=clear_all)
btn_div.grid(row=5, column=1, columnspan=3)
# ________________________________________________________________________________________________________________________________________________________
# execution
main.mainloop()