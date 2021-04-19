# Imports
import pyttsx3
import pandas as pd
import sys

logins = pd.read_csv("S.A.N.E. Data Files\login.csv", engine='python')
logins = logins.values.tolist()

print(logins)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# Functions
def speak(speech):
    engine.say(speech)
    engine.runAndWait()

# Comments for this login can be found in the main script, as the code here is the same due to this being the current version
def returning_user_login():
    username = str(logins[0])
    username = username.replace('[', '')
    username = username.replace("'", '')
    username = username.replace("'", '')
    username = username.replace(']', '')
    print(username)
    password = str(logins[1])
    password = password.replace('[', '')
    password = password.replace("'", '')
    password = password.replace("'", '')
    password = password.replace(']', '')
    print(password)
    sec_key = 1
    while sec_key:
        user_ret = input("Input your username here: ")
        password_ret = input("Input your password: ")
        if user_ret == username:
            speak("Username approved")
        elif user_ret != username:
            speak("Wrong username, please retry")
            user_ret = input("Input your username here: ")
            if user_ret == username:
                speak("Username approved")
                exec(open('S.A.N.E. Assistant.py').read())
                sys.exit(0)
            else:
                speak("Sorry, your username could not be verified properly, please reload sane and retry logging in.")
        if password_ret == password:
            speak("Password approved, welcome back")
            exec(open('S.A.N.E. Assistant.py').read())
            sys.exit(0)
        elif password_ret != password:
            speak("Please retry password")
            password_ret = input("Input your password: ")
            if password_ret == password:
                speak("Password approved")
                exec(open('S.A.N.E. Assistant.py').read())
                sys.exit(0)
            else:
                speak("Sorry, your password could not be verified properly, please reload sane and retry logging in.")


def set_password():
    speak("Welcome to the username and password setup, please input a password that meets the requirements into the "
          "terminal, (username first, password second):")
    user_new = input("Enter your username: ")
    p_new = input("Enter your password (preferably greater than 8 characters including capitals, numbers and "
                  "special characters for security: ")
    logins.append(user_new)
    logins.append(p_new)
    print(logins)
    login_DF = pd.DataFrame([sub.split(",") for sub in logins])
    print(login_DF)
    login_DF.to_csv('S.A.N.E. Data Files/login.csv', index=False, columns=None, sep=',')


while 1:
    ask_user = str(input("Do you already have a login?(y/n): "))
    if 'y' in ask_user:
        returning_user_login()
    elif 'n' in ask_user:
        set_password()
    elif 'y' and 'n' not in ask_user:
        speak("Please only input 'y', or 'n'")
