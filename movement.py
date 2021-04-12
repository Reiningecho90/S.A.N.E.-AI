# Imports
import keyboard
import tkinter
import time


# Defining a variable if i decide to expand the program
def walk():
    while 1:
        time.sleep(1)
        keyboard.press('w')
        time.sleep(0.5)
        keyboard.release('w')
        time.sleep(1)
        keyboard.press('d')
        time.sleep(0.5)
        keyboard.release('d')
        time.sleep(1)
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')
        time.sleep(1)
        keyboard.press('a')
        time.sleep(0.5)
        keyboard.release('a')


# Tkinter window because why not
window = tkinter.Tk()
window.title('Hack Database')
window.configure(bg='black')
icon = tkinter.PhotoImage(file='photo.jpg')
window.iconphoto(False, icon)
button = tkinter.Button(text='INITIATE HACK', width=25, height=5, bg='black', fg='green', command=walk)
button.pack()
window.mainloop()
