# This script is literally because normal calculators don't do exponents without a hassle

# Imports
import time
import tkinter as tk

expression = ""
 

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set(" error ")
        expression = ""
 

def clear():
    global expression
    expression = ""
    equation.set("")


# Tkinter GUI
root = tk.Tk()
root.wm_attributes('-alpha', 0.9)
root.wm_title("Calculator")
root.configure(bg='gray20', height=273, width=180)
root.wm_iconbitmap('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Distribution\\S.A.N.E. Icon.ico')
root.resizable(False, False)

equation = tk.StringVar()

inp_1 = tk.Button(root, text="1", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(1))
inp_1.pack()
inp_1.place(x=0, y=30)
inp_2 = tk.Button(root, text="2", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(2))
inp_2.pack()
inp_2.place(x=45, y=30)
inp_3 = tk.Button(root, text="3", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(3))
inp_3.pack()
inp_3.place(x=90, y=30)
inp_4 = tk.Button(root, text="4", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(4))
inp_4.pack()
inp_4.place(x=0, y=71)
inp_5 = tk.Button(root, text="5", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(5))
inp_5.pack()
inp_5.place(x=45, y=71)
inp_6 = tk.Button(root, text="6", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(6))
inp_6.pack()
inp_6.place(x=90, y=71)
inp_7 = tk.Button(root, text="7", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(7))
inp_7.pack()
inp_7.place(x=0, y=112)
inp_8 = tk.Button(root, text="8", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(8))
inp_8.pack()
inp_8.place(x=45, y=112)
inp_9 = tk.Button(root, text="9", bg='deep sky blue', fg='black', width=5, height=2, command=lambda: press(9))
inp_9.pack()
inp_9.place(x=90, y=112)
inp_0 = tk.Button(root, text="0", bg='gray29', fg='black', width=18, height=2, command=lambda: press(0))
inp_0.pack()
inp_0.place(x=0, y=153)

# Function Buttons
add_nums = tk.Button(root, text='+', bg='gray29', fg='black', width=5, height=2, command=lambda: press('+'))
add_nums.pack()
add_nums.place(x=135, y=30)
subt_nums = tk.Button(root, text='-', bg='gray29', fg='black', width=5, height=2, command=lambda: press('-'))
subt_nums.pack()
subt_nums.place(x=135, y=71)
mult_nums = tk.Button(root, text='*', bg='gray29', fg='black', width=5, height=2, command=lambda: press('*'))
mult_nums.pack()
mult_nums.place(x=135, y=112)
divd_nums = tk.Button(root, text='/', bg='gray29', fg='black', width=5, height=2, command=lambda: press('/'))
divd_nums.pack()
divd_nums.place(x=135, y=153)
divd_nums = tk.Button(root, text='^', bg='gray29', fg='black', width=5, height=2, command=lambda: press('**'))
divd_nums.pack()
divd_nums.place(x=135, y=194)
output_num = tk.Button(root, text='=', bg='gray29', fg='black', width=25, height=2, command=equalpress)
output_num.pack()
output_num.place(x=0, y=235)


expression_field = tk.Entry(root, textvariable=equation, bg='gray22', fg='black', font=('Helvetica', 14))
expression_field.pack()
expression_field.place(x=0, y=0)
expression_field.size()

clear_all = tk.Button(root, text='CLEAR', bg='gray29', fg='black', width=18, height=2, command=clear)
clear_all.pack()
clear_all.place(x=0, y=194)

root.mainloop()