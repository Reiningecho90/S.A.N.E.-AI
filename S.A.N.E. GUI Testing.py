import tkinter as tk

req_user = 'admin'
req_pass = 'admin'

confirm_pass = False

def cal_FUNC():
    calendar_UI = tk.Label(root, text='', bg='gray20', fg='white', font=('Helvetica', 12))
    calendar_UI.pack()

def confirm_b():
    global confirm_pass

    username = p_user.get()
    password = p_user.get()

    if username == req_user:
        print('good')
        if password == req_pass:
            confirm_pass = True
            popup.destroy()
        else:
            print('incorrect password')
    else:
        print("incorrect uername")

def exit():
    root.destroy()

    

# Popup Password Dialog
popup = tk.Tk()
popup.title('Credentials Checkpoint')
popup.wm_iconbitmap('S.A.N.EProject\S.A.N.E. Icon.ico')
popup.wm_attributes('-alpha', 0.95)
popup.configure(bg='gray20')
popwidth, popheight = (popup.winfo_screenwidth()/4), (popup.winfo_screenheight()/4)
popup.geometry('%dx%d+0+0' % (popwidth, popheight))

p_user = tk.Entry(bg='gray20', fg='white')
p_user.pack()
p_user.place(x=(popwidth/2.5), y=0)

p_usrlabel = tk.Label(popup, text="Username:", bg='gray20', fg='white')
p_usrlabel.pack()
p_usrlabel.place(x=(popwidth/4), y=0)

p_pass = tk.Entry(bg='gray20', fg='white')
p_pass.pack()
p_pass.place(x=(popwidth/2.5), y=(50))

p_passlabel = tk.Label(popup, text="Password:", bg='gray20', fg='white')
p_passlabel.pack()
p_passlabel.place(x=(popwidth/4), y=50)

p_confirm = tk.Button(popup, text="Login", bg='gray20', fg='white', command=confirm_b)
p_confirm.pack()
p_confirm.place(x=(popwidth/2.05), y=75)


popup.mainloop()

# Main Window and UI Elements
root = tk.Tk()
root.title("S.A.N.E., Your Open-Source Personal Assistant")
root.wm_iconbitmap('S.A.N.EProject\S.A.N.E. Icon.ico')
root.wm_attributes('-alpha', 0.95)
root.wm_attributes('-fullscreen', True)
root.configure(bg='gray20')
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))

logo = tk.PhotoImage(file='C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\sanelogo.png')
logo_labl = tk.Label(root, image=logo, bg='gray20')
logo_labl.pack()
logo_labl.place(x=(width/2.5), y=(height/5))

welcome_SC = tk.Label(root, text='Hello, Welcome to S.A.N.E.', width=25, height=3, bg='gray20', fg='white', font=('Helvetica', 14))
welcome_SC.pack()
welcome_SC.place(x=(width/2.35), y=0)

funcs = tk.Label(root, text='Functions with Push Command:', width=25, height=3, bg='gray20', fg='white', font=('Helvetica', 14))
funcs.pack()
funcs.place(x=0, y=40)

settings_func = tk.Button(root, text='Calendar', width=10, height=2, bg='gray20', fg='white', font=('Helvetica', 12), command=None) 
settings_func.pack()
settings_func.place(x=5, y=100)

exit_b = tk.Button(root, text=('Log Off'), width=10, height=2, bg='gray20', fg='red', font=('Helvetica', 12), command=exit)
exit_b.pack()
exit_b.place(x=(width-100), y=(height-5))

if confirm_pass:
    root.mainloop()

# Set Login Dialog
set_login = tk.Tk()
set_login.title('Credentials Checkpoint')
set_login.wm_iconbitmap('S.A.N.EProject\S.A.N.E. Icon.ico')
set_login.wm_attributes('-alpha', 0.95)
set_login.configure(bg='gray20')
setlwidth, setlheight = (set_login.winfo_screenwidth()/4), (set_login.winfo_screenheight()/4)
set_login.geometry('%dx%d+0+0' % (setlwidth, setlheight))

set_user = tk.Entry(bg='gray20', fg='white')
set_user.pack()
set_user.place(x=(popwidth/2.5), y=0)

set_usrlabel = tk.Label(popup, text="Username:", bg='gray20', fg='white')
set_usrlabel.pack()
set_usrlabel.place(x=(popwidth/4), y=0)

set_pass = tk.Entry(bg='gray20', fg='white')
set_pass.pack()
set_pass.place(x=(popwidth/2.5), y=(50))

set_passlabel = tk.Label(popup, text="Password:", bg='gray20', fg='white')
set_passlabel.pack()
set_passlabel.place(x=(popwidth/4), y=50)

set_confirm = tk.Button(popup, text="Login", bg='gray20', fg='white', command=confirm_b)
set_confirm.pack()
set_confirm.place(x=(popwidth/2.05), y=75)

set_login.mainloop()


