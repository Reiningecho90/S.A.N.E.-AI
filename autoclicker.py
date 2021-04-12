# Imports
from pynput.mouse import Button, Controller
import keyboard
import tkinter
import time


# Defining a variable again because I might decide to expand
def run(clicks=0):
    count = click_count.get()
    mouse = Controller()
    while 1:
        if keyboard.is_pressed('-'):
            for i in range(int(count)):
                mouse.click(Button.left)
                time.sleep(0.1)
                if 1:
                    print(f"clicks: {clicks + 1}")
                    clicks += 1


# Tkinter window
window = tkinter.Tk()
button = tkinter.Button(text='INITIATE HACK', width=25, height=5, bg='gray', fg='white', command=run)
button.pack()
click_count = tkinter.Entry(width=25, bg='white', fg='black')
click_count.pack()
window.mainloop()
