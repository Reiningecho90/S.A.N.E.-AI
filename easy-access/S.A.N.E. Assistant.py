# Working on: EOL Reached.
# Finished: FINAL RELEASE v2.0

# Update Description: Finishes up all features. Everything will be completed after 2.0 gets released. This will be the last update to S.A.N.E.

# Future Ideas: NEOL Reached.

# Imports
from tkinter.constants import END
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from asyncio import get_event_loop
import threading
import time
import wikipedia
import os
import random
from PyDictionary import PyDictionary
import pandas as pd
import pandas.errors as e
import json
import tkinter as tk
from googletrans import Translator, constants
from sys import exit


# Storage initialization, works along with the jawbreaker and predictor to gather user data
try:
    data_storing = pd.read_csv("S.A.N.E. Data Files\\data_storing.csv", delimiter=', ', engine='python')
    network_storage = pd.read_csv("S.A.N.E. Data Files\\network_storage.csv", delimiter=', ', engine='python')
    common_values = pd.read_csv("S.A.N.E. Data Files\\common_values.csv", delimiter=', ', engine='python')
    secondary_storage = pd.read_csv("S.A.N.E. Data Files\\secondary_storage.csv", delimiter=', ', engine='python')

    data_storing = data_storing.values.tolist()
    network_storage = network_storage.values.tolist()
    common_values = common_values.values.tolist()
    secondary_storage = secondary_storage.values.tolist()

    data_storing.clear()
    network_storage.clear()
    common_values.clear()
    secondary_storage.clear()
except e.EmptyDataError:
    pass


# Settings data loading
settings_file = open('S.A.N.E. Data Files\\settings.json', 'r')
settings_file_d = json.load(settings_file)
settings_file.close()

if settings_file_d["GENDER"] == 'MALE':
    gender = 0
elif settings_file_d["GENDER"] == 'FEMALE':
    gender = 1

if 'he' in settings_file_d["PRONOUNS"]:
    usr_gender = 'sir'

elif 'she' in settings_file_d["PRONOUNS"]:
    usr_gender = "ma'am"

elif 'they' in settings_file_d["PRONOUNS"]:
    usr_gender = ''

elif '' in settings_file_d["PRONOUNS"]:
    usr_gender = ''

# Start-up for the voice engine, used for the pyttsx3 voice API (microsoft based API)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[gender].id)

# More data dumps/storage
primary_storing, search_list, daily_donations = [], [], []

# Login initialization
logins = pd.read_csv("S.A.N.E. Data Files\\login.csv", engine='python')
logins = logins.values.tolist()

login_okay = False

username = ''
password = ''

confirm_pass = False


# Functions
def speak(speech):
    engine.say(speech)
    engine.runAndWait()


# Popup Username and Password Window
def popup_window():
    global confirm_pass
    def confirm_b():
        global confirm_pass

        username_e = p_user.get()
        password_e = p_user.get()

        if username_e == username:
            if password_e == password:
                confirm_pass = True
                popup.destroy()
            else:
                speak('Incorrect password')
        else:
            speak("Incorrect username")


    popup = tk.Tk()
    popup.title('Credentials Checkpoint')
    popup.wm_iconbitmap('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Distribution\\S.A.N.E. Icon.ico')
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


# Set Login Dialog
def login_dialog():
    def confirm_b():
        global username
        global password

        username = set_user.get()
        password = set_pass.get()

        logins.append(username)
        logins.append(password)

        speak("Thank your for registering, please confirm your login to access the AI.")
        set_login.destroy()

        popup_window()
        

    
    set_login = tk.Tk()
    set_login.title('Credentials Checkpoint')
    set_login.wm_iconbitmap('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Distribution\\S.A.N.E. Icon.ico')
    set_login.wm_attributes('-alpha', 0.95)
    set_login.configure(bg='gray20')
    setlwidth, setlheight = (set_login.winfo_screenwidth()/4), (set_login.winfo_screenheight()/4)
    set_login.geometry('%dx%d+0+0' % (setlwidth, setlheight))

    set_user = tk.Entry(bg='gray20', fg='white')
    set_user.pack()
    set_user.place(x=(setlwidth/2.5), y=0)

    set_usrlabel = tk.Label(set_login, text="Username:", bg='gray20', fg='white')
    set_usrlabel.pack()
    set_usrlabel.place(x=(setlwidth/4), y=0)

    set_pass = tk.Entry(bg='gray20', fg='white')
    set_pass.pack()
    set_pass.place(x=(setlwidth/2.5), y=(50))

    set_passlabel = tk.Label(set_login, text="Password:", bg='gray20', fg='white')
    set_passlabel.pack()
    set_passlabel.place(x=(setlwidth/4), y=50)

    set_confirm = tk.Button(set_login, text="Login", bg='gray20', fg='white', command=confirm_b)
    set_confirm.pack()
    set_confirm.place(x=(setlwidth/2.05), y=75)

    set_login.mainloop()


# Next three functions initialize the entire program with a username and password
def login__init__():
    speak('Do you have a login yet? Please say yes or no.')
    while 1:
        yes_or_no = r.listen(source)
        yes_or_no = r.recognize_google(yes_or_no)
        if 'yes' in yes_or_no:
            speak("Thank you for supporting, please input your login now.")
            returning_user_login()

        elif 'no' in yes_or_no:
            speak("Welcome, please seta  login in the window provided.")
            set_password()

        elif 'yes' and 'no' not in yes_or_no:
            speak("Please only say either yes or no")


def returning_user_login():  # Login for returning users
    global username
    global password
    global confirm_pass


    username = str(logins[0])
    username = username.replace(' nan nan nan nan', '')
    username = username.replace('[', '')
    username = username.replace("'", '')
    username = username.replace(']', '')
    username = username.replace(',', '')  # Takes out excess characters from password because they are from a .csv
    # file, like the one attached in the GitHub repo
    password = str(logins[1])
    password = password.replace(' nan nan nan nan', '')
    password = password.replace('[', '')
    password = password.replace("'", '')
    password = password.replace(']', '')
    password = password.replace(',', '')

    popup_window()

    confirm_pass = True

    if confirm_pass:
        speak("Credentials Authorized, Welcome.")
        t1 = threading.Thread(do_stuff())
        t1.start()


def set_password():  # Setup for the username and password process, this appends two things to the .csv, a username and password
    login_dialog()

    login_DF = pd.DataFrame(logins, columns=None)
    login_DF.to_csv('S.A.N.E. Data Files\\login.csv', index=False, columns=None, sep=',')

    returning_user_login()


def the_jawbreaker():
    inp_count = 0

    while True:
        for i in data_storing:
            if i not in secondary_storage:
                secondary_storage.append(i)  # Iterate over storage samples from inputs to find usable samples
            else:
                continue

        obj = random.choice(secondary_storage)

        # Choose random sample from storage container
        value = obj
        if ' ' in value:
            val_list = list(value.split(' '))  # Dissect value to refine dataframe
            word_1 = val_list[0]
            word_2 = val_list[1]

            if word_1 or word_2 in network_storage:  # Write the value to separate containers (network, common)
                network_storage.append(word_1)
                network_storage.append(word_2)

            elif word_1 or word_2 not in network_storage:
                network_storage.append(word_1)
                network_storage.append(word_2)
                common_values.append(word_1)
                common_values.append(word_2)
        else:
            if value in network_storage:  # Single value placement command
                network_storage.append(value)

            elif value not in network_storage:
                network_storage.append(value)
                common_values.append(value)

        # Prediction algorithm is a searching loop that uses reference data
        for i in network_storage:
            print(network_storage)
            
            if len(network_storage) > 0:
                suggestion = PyDictionary.synonym(i)
                print(random.choice(suggestion))


def confirm_settings():
    speak("This will shutdown, reopen to have your settings applied.")
    exit()


def settings_change():
    speak("Please enter your password to access the settings")

    def set_voice_gender():
        print(settings_file_d["GENDER"])
        if settings_file_d['GENDER'] == 'MALE':
            settings_data = {
                            "GENDER": "FEMALE",
                            "PRONOUNS": settings_file_d["PRONOUNS"]
                            }

            settings_file = open('S.A.N.E. Data Files\\settings.json', 'w')
            json.dump(settings_data, settings_file)
            speak('Gender changed')
            settings_file.close()
            exit()

        elif settings_file_d["GENDER"] == "FEMALE":
            settings_data = {
                            "GENDER": "MALE",
                            "PRONOUNS": settings_file_d["PRONOUNS"]
                            }

            settings_file = open('S.A.N.E. Data Files\\settings.json', 'w')
            json.dump(settings_data, settings_file)
            speak('Gender changed')
            settings_file.close()
            speak("Please restart the program to utilize changes.")
            exit()


    def set_pronouns():
        pronouns = PRONOUN_SELECT.get('1.0', END)
        pronouns = pronouns.replace('\n', '')

        settings_data = {
                        "GENDER": settings_file_d["GENDER"],
                        "PRONOUNS": pronouns
                        }
        
        settings_file = open('S.A.N.E. Data Files\\settings.json', 'w')
        json.dump(settings_data, settings_file)
        print(f'Prefered pronouns changed')
        settings_file.close()


    # Tkinter settings window
    
    set_win = tk.Tk()

    while 1:

        popup_window()

        if confirm_pass:
            set_win.mainloop()

    
    set_win.title('S.A.N.E. Settings Configuration')
    set_win.wm_attributes('-alpha', 0.95)
    set_win.configure(bg='gray20')
    set_win.wm_iconbitmap('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Distribution\\S.A.N.E. Icon.ico')
    root_h = (set_win.winfo_screenheight()/3)
    root_w = (set_win.winfo_screenwidth()/3)
    x = (root_w/1)
    y = (root_h/1.2)
    set_win.geometry('%dx%d+%d+%d' % (root_w, root_h, x, y))
    set_win.resizable(False, False)

    VOICE_GENDER_SELECT = tk.Button(set_win, text=f'Toggle Gender', bg='gray20', fg='white', command=set_voice_gender)
    VOICE_GENDER_SELECT.pack()

    PRONOUN_SELECT = tk.Text(set_win, bg='gray20', fg='white', width=100, height=1)
    PRONOUN_SELECT.pack()

    PRONOUN_SELECT_B = tk.Button(set_win, text=f'Confirm Pronouns', bg='gray20', fg='white', command=set_pronouns)
    PRONOUN_SELECT_B.pack()

    CONFIRM_SETTINGS = tk.Button(set_win, text=f'Confirm Settings', bg='gray20', fg='white', command=confirm_settings)
    CONFIRM_SETTINGS.pack()
    CONFIRM_SETTINGS.place(x=(root_w/2.35), y=(root_h-25))

    set_win.mainloop()


def speak_with_user():  # Speak with user is the conversational algorithm, with limited functions, although it
    # eventually re-roots itself into the main algorithm
    speak("Sane friendly mode is in beta, if any features should be included or any bugs are prominent please report "
          "to the developer of Sane.")
    speak("How is your day today?")
    response = r.listen(source)
    response = r.recognize_google(response)
    response = response.lower()

    while 1:
        if 'good' or 'great' or 'amazing' or 'really good' in response:
            responses = ['What makes your day good?', 'Did you do anything cool?', 'What fun activities did you do '
                                                                                   'today?']
            speak(random.choice(responses))
            response = r.listen(source)
            response = r.recognize_google(response)
            primary_storing.append(response)
            speak("That's great, do you have any other plans today?")
            response = r.listen(source)
            response = r.recognize_google(response)

            if 'no' or 'nah' in response:
                speak("Fair enough I'll be here in case you need me.")
                while 1:
                    yes_or_no = r.listen(source)
                    yes_or_no = r.recognize_google(yes_or_no)
                    if 'yes' in yes_or_no:
                        exit(do_stuff())
                    else:
                        continue

            elif 'yes' in response:
                speak("Nice, although if you said what you are doing I'm not sure I heard")
                response = r.listen(source)
                response = r.recognize_google(response)
                primary_storing.append(response)
                time.sleep(0.5)
                speak("Nice do you want any help with that?")
                response = r.listen(source)
                response = r.recognize_google(response)
                if 'yes' or 'ok' in response:
                    speak("would you like me to define a word, Wiki search or anything?")
                    response = r.listen(source)
                    response = r.recognize_google(response)

                    if 'wiki' in response:
                        speak('What would you like to search?')
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        speak("Your results are being processed now.")
                        answer = wikipedia.summary(audio, sentences=5)
                        speak(answer)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'define' in response:
                        speak("What is your word?")
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        word_def = PyDictionary.meaning(f"{audio}")
                        speak(word_def)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                elif 'no' in response:
                    speak("Okay, I'll be here if you need any help later.")

        elif 'bad' or 'not great' or 'pretty bad' or 'not that good' in response:
            responses = ['Why is your day not that great?', 'What makes your day sub par?', 'Did anything happen or '
                                                                                            'are '
                                                                                            'you just in a down mood?']
            speak(random.choice(responses))
            response = r.listen(source)
            response = r.recognize_google(response)
            primary_storing.add(response)
            speak("That's not that great, what about later today? Any plans then?")
            response = r.listen(source)
            response = r.recognize_google(response)
            if 'no' in response:
                speak("Okay I'll be here if you need me for anything")
                while 1:
                    yes_or_no = r.listen(source)
                    yes_or_no = r.recognize_google(yes_or_no)
                    if 'yes' in yes_or_no:
                        exit(do_stuff())
                    else:
                        continue

            if 'yes' in response:
                speak("Nice, although if you said what you are doing I'm not sure I heard")
                response = r.listen(source)
                response = r.recognize_google(response)
                primary_storing.add(response)
                speak("Okay, would you like help with that or should I stay quiet?")
                response = r.listen(source)
                response = r.recognize_google(response)

                if 'help' in response:
                    speak("How would you like me to help?")
                    response = r.listen(source)
                    response = r.recognize_google(response)

                    if 'wiki' in response:
                        speak('What would you like to search?')
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        search_list.add(audio)
                        speak("Your results are being processed now, .")
                        answer = wikipedia.summary(audio, sentences=5)
                        speak(answer)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'define' in response:
                        speak("What is your word?")
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        word_def = PyDictionary.meaning(f"{audio}")
                        speak(word_def)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'synonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        word_syn = PyDictionary.synonym(f"{audio}")
                        speak(word_syn)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'antonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        word_ants = PyDictionary.synonym(f"{audio}")
                        speak(word_ants)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'translate' in response:
                        translator = Translator()
                        speak("What is a word or phrase to translate?")
                        words = r.listen(source)
                        words = r.recognize_google(words)
                        speak('What language would you like to have the words translated to (two letters, codes '
                              'can be '
                              'found in terminal)')
                        print("Spanish: es, English: en, french: fr, German: de, Italian: it, Japanese: ja, Korean: ko "
                              "(others can be found here: https://cloud.google.com/translate/docs/languages)")
                        language = r.listen(source)
                        language = r.recognize_google(language)
                        lower_lang = language.lower()
                        translated = translator.translate(words, dest=f'{lower_lang}')

                        speak(translated.text)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'no' in response:
                        speak("Alright, I'll be on standby just in case")
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

        elif 'ok' or 'alright' or 'fine':
            responses = ['Why is your day just fine?', 'Did you do anything today?', 'How did you go about your day '
                                                                                     'today?']
            speak(random.choice(responses))
            response = r.listen(source)
            response = r.recognize_google(response)
            primary_storing.append(response)
            speak("That's alright")
            speak("Are you working on any projects, work, school work I can help you with?")
            response = r.listen(source)
            response = r.recognize_google(response)

            if 'yes' in response:
                speak("Nice, although if you said what you are doing I'm not sure I heard")
                response = r.listen(source)
                response = r.recognize_google(response)
                primary_storing.append(response)
                speak("Okay, would you like help with that or should I stay quiet?")
                response = r.listen(source)
                response = r.recognize_google(response)

                if 'help' in response:
                    speak("How would you like me to help?")
                    response = r.listen(source)
                    response = r.recognize_google(response)
                    if 'wiki' in response:
                        speak('What would you like to search?')
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        search_list.append(audio)
                        speak("Your results are being processed now, .")
                        answer = wikipedia.summary(audio, sentences=5)
                        speak(answer)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'define' in response:
                        speak("What is your word?")
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        word_def = PyDictionary.meaning(f"{audio}")
                        speak(word_def)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'synonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        word_syn = PyDictionary.synonym(f"{audio}")
                        speak(word_syn)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'antonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source)
                        audio = r.recognize_google(audio)
                        word_ants = PyDictionary.synonym(f"{audio}")
                        speak(word_ants)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                    elif 'translate' in response:
                        translator = Translator()
                        speak("What is a word or phrase to translate?")
                        words = r.listen(source)
                        words = r.recognize_google(words)
                        speak('What language would you like to have the words translated to (two letters, codes '
                              'can be '
                              'found in terminal)')
                        print("Spanish: es, English: en, french: fr, German: de, Italian: it, Japanese: ja, Korean: ko "
                              "(others can be found here: https://cloud.google.com/translate/docs/languages)")
                        language = r.listen(source)
                        language = r.recognize_google(language)
                        lower_lang = language.lower()
                        translated = translator.translate(words, dest=f'{lower_lang}')

                        speak(translated.text)
                        while 1:
                            yes_or_no = r.listen(source)
                            yes_or_no = r.recognize_google(yes_or_no)
                            if 'yes' in yes_or_no:
                                exit(do_stuff())
                            else:
                                continue

                elif 'no' in response:
                    speak("Alright, I'll be on standby just in case")
                    while 1:
                        yes_or_no = r.listen(source)
                        yes_or_no = r.recognize_google(yes_or_no)
                        if 'yes' in yes_or_no:
                            exit(do_stuff())
                        else:
                            continue
            elif 'no' or 'not' in response:
                speak("Okay I'll be here to help if you need me")
                while 1:
                    yes_or_no = r.listen(source)
                    yes_or_no = r.recognize_google(yes_or_no)
                    if 'yes' in yes_or_no:
                        exit(do_stuff())
                    else:
                        continue


def release_the_hounds():
    thread = threading.Thread(speak_with_user())
    thread.start()


def calc():
    speak('Opening the calculator')
    exec(open('calculator.py').read())


def afk_move():
    speak('Opening the AFK database')
    exec(open('movement.py').read())


def auto_click():
    speak('Opening the autoclicker')
    exec(open('autoclicker.py').read())


def bluetooth_feedback():
    speak("We are now testing bluetooth headphones mode, do you have wireless headphones/mic connected?")
    audio = r.listen(source)
    audio = r.recognize_google(audio)
    if 'yes' or 'yeah' in audio:
        speak('We would like to know how the experience is with bluetooth.')
        response = r.listen(source)
        response = r.recognize_google(response)
        if str(response.lower()) == 'yes':
            speak('I will ask for your feedback after this session, thank you.')
            return True
        else:
            speak('Okay, thank you for considering!')
            exit()


def do_stuff():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    dictionary = PyDictionary()
    unknown_count = 0


    # Main Window and UI Elements
    def exit():
        root.destroy()


    def update_main():
        root.update()


    root = tk.Tk()
    root.title("S.A.N.E. CEO Edition")
    root.wm_iconbitmap('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Distribution\\S.A.N.E. Icon.ico')
    root.wm_attributes('-alpha', 0.95)
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

    settings_func = tk.Button(root, text='Settings', width=10, height=2, bg='gray20', fg='white', font=('Helvetica', 12), command=settings_change) 
    settings_func.pack()
    settings_func.place(x=5, y=100)

    exit_b = tk.Button(root, text=('Log Off'), width=10, height=2, bg='gray20', fg='red', font=('Helvetica', 12), command=exit)
    exit_b.pack()
    exit_b.place(x=(width-100), y=(height-100))

    while 1:
        
        # there will be plenty of root updating commands throughout to keep the GUI runing as smoothly as the client allows

        try:
            t5 = threading.Thread(update_main())
            t5.start()

            audio = r.listen(source)  # Initially listening to the source mic
            audio = r.recognize_google(audio)  # Initially Recognizing the given string values
            audio = audio.lower()

            root.update()

            if 'you there' in audio:  # All of these functions are self explanatory
                speak(f"At your service {usr_gender}")
                
            root.update()

            if 'friendly mode' in audio: # See lines 170-476 for the script
                t3 = threading.Thread(release_the_hounds())
                t3.start()
            
            root.update()

            if 'open a new' in audio:
                speak("What would you like to open?")
                audio = r.listen(source)
                audio = r.recognize_google(audio)
                webbrowser.get(chrome_path).open(audio + ".com")
                speak("Tab opened ")
            
            root.update()

            if 'time' in audio:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            
            root.update()

            if 'sicko mode' in audio:
                speak("Astro, yeah Sun is down, freezing' cold, That's how we already know, winter's here, "
                      "My dog would "
                      "probably do it for a Louis belt, "
                      "That's just all he know, he don't know nothin' else, "
                      "I tried to "
                      "show 'em, yeah, I tried to show 'em, yeah, yeah, Yeah, yea yeah, Gone on you with the pick and "
                      "roll Yeah Sane, he in sicko mode")
            
            root.update()

            if 'user manual' in audio:
                speak("I am Sane, "
                      "the semi-artificial neural environment, "
                      "your friendly, self aware virtual assistant! I have been programmed to,"
                      "open tabs, search Wiki, check the time, sing horribly etc.")
                speak("Any further questions?")
                audio = r.listen(source)
                audio = r.recognize_google(audio)
                if 'no' in audio:
                    speak("Okay")
                elif 'explain' in audio:
                    speak("I can not explain a single function but the extended manual is on your screen now, "
                          "would you like me to read it for you?.")
                    audio = r.listen(source)
                    audio = r.recognize_google(audio)

                    if 'no' in audio:
                        os.open('/S.A.N.E. User Guide Extended', flags=0)
                    elif 'yes' in audio:
                        os.open('/S.A.N.E. User Guide Extended', flags=0)
                        speak("""S.A.N.E. Keywords
                                *********************************************************************************************
                                About keywords: You can talk to S.A.N.E. how you normally would although he will only recognize keywords meaning that he will only recognize part of the scentence but will acknowledge the rest.
                                *********************************************************************************************
                                Commands and Functions:
                                Conversation/Friendly Mode: 'friendly mode'
                                Open a New Tab: 'open a new' then when asked say a .com site to open (google, youtube, etc.)
                                Get the Time: 'time'
                                Sing Horribly: 'sicko mode'
                                Read the User Manual: 'user manual'
                                Search Wiki: 'wiki' then when asked give the subject
                                Define a Word: 'define' then when asked say the word
                                Find Synonyms/Antonyms for a Word: 'synonyms' and 'antonyms' then when asked say the word
                                Translate a Word: 'translate' then when asked say the word and type in the two letter language code (provided in window)
                                Open the Five Function Calculator in the Window: 'calculator' then enter a operation (^ for exponent, * for multiply, / for divide and +/- for add and subtract respectively.)
                                50/50 Chance Command (Coin Flip): 'flip'
                                Power Off: 'power off' then when S.A.N.E. says no say 'do it'
                                Mute S.A.N.E. for a Number of Seconds: 'hibernate' then when S.A.N.E. prompts you for the second count say the number without any other words. (i.e. '60' for one minute and so on)
                                Custom Autoclicker: The first text box is the number of clicks and the second box is the frequncy so entering 100 and 0.01 will click 100 times and one click every millisecond, add extra clicks for redundancy as you are clicking into the program.
                                AFK Movement Program: 'movement' all you have to do is click the initiate button and it will start the movement loop.
                                *********************************************************************************************
                                NOTES:
                                It is reccomended that you use headphones with a built in mic because the program 1. is programmed for mic optimization and 2 gets better quality with a nearer mic.
                                USE SIMPLE WORDING, THE MORE WORDS YOU USE THE LONGER IT TAKES TO RUN(test this out, I founc that with other programs running the best word count for S.A.N.E. was about 3-5 words and response time was about 2-3 seconds, if you only use the keywords it will be super short)
                                Sane will ask if you need help after a matter of minutes without talking due to how he is programmed. If you do not want this to happen calculate the number of seconds to hibernate for, although if he is hibernating he can not recieve commands. You can say 'yes' or 'no' to most of the questions he asks and get a relevant answer or prefrom a relevant action based on your answer.
                                Remember, S.A.N.E. is in beta, he will be optimized later so you can preform more actions quicker, and more!""")
            
            root.update()

            if 'wiki' in audio:
                speak('What would you like to search?')
                audio = r.listen(source)
                audio = r.recognize_google(audio)
                search_list.append(audio)
                try:
                    speak(f"Your results are being processed now, {usr_gender}.")
                    answer = wikipedia.summary(audio, sentences=5)
                    speak(answer)
                except wikipedia.exceptions.PageError:
                    try:
                        speak('We could not find that page, please retry speaking your search.')
                        answer = r.listen(source)
                        answer = r.recognize_google(answer)

                        answer = wikipedia.summary(answer, sentences = 5)
                        speak('Sorry for the inconvinience.')
                    except wikipedia.exceptions.PageError:
                        speak("I'm sorry it appears the database does not include information on that subject, or the audio was not clear.")
            
            root.update()

            if 'define' in audio:
                speak("What is your word?")
                audio = r.listen(source)
                audio = r.recognize_google(audio)
                word_def = dictionary.meaning(f"{audio}")
                speak(word_def)
            
            root.update()

            if 'synonym' in audio:
                speak("What is your word?")
                audio = r.listen(source)
                audio = r.recognize_google(audio)
                word_syn = dictionary.synonym(f"{audio}")
                speak(word_syn)
            
            root.update()

            if 'antonym' in audio:
                speak("What is your word?")
                audio = r.listen(source)
                audio = r.recognize_google(audio)
                word_ants = dictionary.synonym(f"{audio}")
                speak(word_ants)
            
            root.update()

            if 'calculator' in audio:
                speak("Opening the calculator in one second...")

                t2 = threading.Thread(calc())
                t2.start()
            
            root.update()

            if 'flip' in audio:
                speak("Flipping the coin now.")
                nums = [1, 2]
                choice = random.choice(nums)
                if choice == 1:
                    speak("The outcome is tails.")
                elif choice == 2:
                    speak("The outcome is heads.")
            
            root.update()

            if 'power off' in audio:
                if bluetooth_feedback():
                    speak("It appears its your lucky day, you had a one in 400 chance of being asked the question you "
                          "were asked at the beginning of the session, and because you answered yes we are opening "
                          "the terminal to input on bluetooth compatibility before you leave!")
                    speak("Would you like to leave a review?")
                    yes_or_no = r.listen(source)
                    yes_or_no = r.recognize_google(yes_or_no)
                    if 'yes' in yes_or_no:
                        speak("Okay, you can speak your review now.")
                        review = r.listen(source)
                        review = r.recognize_google(review)
                        primary_storing.append(review)

                else:
                    exit()

                speak("Powering off, have a good day.")
                exit()
            
            root.update()

            if 'hibernate' in audio:
                speak('Would you like me to sleep for seconds, minutes or hours?')
                choice_time = r.listen(source)
                choice_time = r.recognize_google(choice_time)
                if 'seconds' in choice_time:
                    speak("Okay how many seconds should I sleep?")
                    audio = r.listen(source)
                    audio = r.recognize_google(audio)
                    speak(f"going down for {audio} seconds.")
                    time.sleep(int(audio))
                    speak("I'm back .")
                
                elif 'minutes' in choice_time:
                    speak("Okay how many minutes should I sleep?")
                    audio = r.listen(source)
                    audio = r.recognize_google(audio)
                    speak(f"going down for {audio} minutes.")
                    time.sleep(int(audio*60))
                    speak("I'm back .")
                
                elif 'hours' in choice_time:
                    speak("Okay how many hours should I sleep?")
                    audio = r.listen(source)
                    audio = r.recognize_google(audio)
                    speak(f"going down for {audio} hours.")
                    time.sleep(int((audio*3600)))
                    speak("I'm back.")

            root.update()

            if 'settings' in audio:
                speak('Opening the settings.')
                settings_change()
            
            root.update()

            if 'translate' or 'Translate' in audio:
                translator = Translator()
                speak("What is a word or phrase to translate?")
                words = r.listen(source)
                words = r.recognize_google(words)
                speak('What language would you like to have the words translated to (two letters, codes '
                        'can be '
                        'found in terminal)')
                print("Spanish: es, English: en, french: fr, German: de, Italian: it, Japanese: ja, Korean: ko "
                        "(others can be found here: https://cloud.google.com/translate/docs/languages)")
                language = r.listen(source)
                language = r.recognize_google(language)
                lower_lang = language.lower()
                translated = translator.translate(words, dest=f'{lower_lang}')

                speak(translated.text)

            root.update()
        
        # Built-in errors for the speech-recognition library, as well as NN initialization
        except sr.UnknownValueError: 
            unknown_count = unknown_count + 1
            if unknown_count == 50:
                t4 = threading.Thread(the_jawbreaker())  
                t4.start()

        except sr.RequestError:
            unknown_count = unknown_count + 1
            if unknown_count == 50:
                t4 = threading.Thread(the_jawbreaker())
                t4.start()


r = sr.Recognizer()  # Set recognizer
mic = sr.Microphone(device_index=1)  # Microphone set to headphones for best quality

with mic as source:  # Kinda like a main program but super short, most of the good stuff is above

    r.adjust_for_ambient_noise(source)

    hit1 = random.uniform(0, 20)
    hit2 = random.uniform(0, 20)  # This is for users with bluetooth headphones that they use while with S.A.N.E.
    if hit1 == hit2:
        bluetooth_feedback()

    speak("Hello, welcome to sane.")
    if not login_okay:
        login__init__()  # Initializes the login process
