# Imports
# Imports
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import threading
import time
import wikipedia
import os
import random
from PyDictionary import PyDictionary
import pandas as pd
import pandas.errors as e

# Storage initialization, works along with the jawbreaker and predictor to gather user data
try:
    data_storing = pd.read_csv("S.A.N.E. Data Files\data_storing.csv", delimiter=', ', engine='python')
    network_storage = pd.read_csv("S.A.N.E. Data Files\\network_storage.csv", delimiter=', ', engine='python')
    common_values = pd.read_csv("S.A.N.E. Data Files\common_values.csv", delimiter=', ', engine='python')
    secondary_storage = pd.read_csv("S.A.N.E. Data Files\secondary_storage.csv", delimiter=', ', engine='python')
    data_storing = data_storing.values.tolist()
    network_storage = network_storage.values.tolist()
    common_values = common_values.values.tolist()
    secondary_storage = secondary_storage.values.tolist()
except e.EmptyDataError:  # Catches empty datasets and continues the execution
    pass


# Start-up for the voice engine, used for the pyttsx3 voice API (microsoft based API)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# More data dumps/storage
primary_storing, search_list, daily_donations = [], [], []

# Login initialization
logins = pd.read_csv("S.A.N.E. Data Files\login.csv", engine='python')
logins = logins.values.tolist()

login_okay = False


# Functions
def speak(speech):
    engine.say(speech)
    engine.runAndWait()


# Next three functions initialize the entire program with a username and password
def login__init__():
    ask_user = str(input("Do you already have a login?(y/n): "))
    if 'y' in ask_user:
        returning_user_login()
    elif 'n' in ask_user:
        set_password()
    elif 'y' and 'n' not in ask_user:
        speak("Please only input 'y', or 'n'")


def returning_user_login():  # Login for returning users
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
    while 1:
        user_ret = input("Input your username here: ")
        password_ret = input("Input your password: ")
        if user_ret == username:
            speak("Username approved")
            os.system('cls' if os.name == 'nt' else 'clear')
        elif user_ret != username:
            speak("Wrong username, please retry")
            user_ret = input("Input your username here: ")
            if user_ret == username:
                speak("Username approved")
                os.system('cls' if os.name == 'nt' else 'clear')  # Clears the system so username and password is
                # hidden after the user finished the process
                return 0
            else:
                speak("Sorry, your username could not be verified properly, please reload sane and retry logging in.")
        if password_ret == password:
            speak("Password approved, welcome back")
            os.system('cls' if os.name == 'nt' else 'clear')
            return 0
        elif password_ret != password:
            speak("Please retry password")
            password_ret = input("Input your password: ")
            if password_ret == password:
                speak("Password approved")
                os.system('cls' if os.name == 'nt' else 'clear')
                return 0
            else:
                speak("Sorry, your password could not be verified properly, please reload sane and retry logging in.")


def set_password():  # Setup for the username and password process, this appends two things to the .csv, a username
    # and password
    speak("Welcome to the username and password setup, please input a password that meets the requirements into the "
          "terminal, (username first, password second):")
    user_new = input("Enter your username: ")
    p_new = input("Enter your password (preferably greater than 8 characters including capitals, numbers and "
                  "special characters for security: ")
    logins.append(user_new)
    logins.append(p_new)
    login_DF = pd.DataFrame(logins, columns=None)
    login_DF.to_csv('S.A.N.E. Data Files/login.csv', index=False, columns=None, sep=',')
    returning_user_login()


def the_jawbreaker():
    print('Running the jawbreaker')  # Print statements used for confirmation across functions
    for i in data_storing:
        if i not in secondary_storage:
            secondary_storage.append(i)  # Iterate over storage samples from inputs to find usable samples
            print(secondary_storage)
        else:
            continue

    obj = random.choice(secondary_storage)

    # Choose random sample from storage container
    value = obj
    if ' ' in value:
        val_list = list(value.split(' '))  # Dissect value to refine dataframe
        word_1 = val_list[0]
        word_2 = val_list[1]
        if word_1 or word_2 not in network_storage:  # Write the value to separate containers (network, common)
            network_storage.append(word_1)
            network_storage.append(word_2)
        elif word_1 or word_2 in network_storage:
            network_storage.append(word_1)
            network_storage.append(word_2)
            common_values.append(word_1)
            common_values.append(word_2)
    else:
        if value not in network_storage:  # Single value placement command
            network_storage.append(value)
        elif value in network_storage:
            network_storage.append(value)
            common_values.append(value)

    print("Running the predictor")  # Prediction algorithm is a searching loop that uses reference data
    for i in common_values:
        print("Searching for an item")
        item_count = common_values.count(i)
        print("search done")
        print(i)
        if i != "['default 2']":
            if item_count > 1:
                # Idle count statement (number can be adjusted)
                best_value = i
                speak(f"You have been idle, do you want to look further into {best_value}")
                break
            else:
                continue
        else:
            break


def speak_with_user():  # Speak with user is the conversational algorithm, with limited functions, althoughit
    # eventually re-roots itself into the main algorithm
    speak("Sane friendly mode is in beta, if any features should be included or any bugs are prominent please report "
          "to the developer of Sane.")
    speak("How is your day today?")
    response = r.listen(source, timeout=3)
    response = r.recognize_google(response)

    while 1:
        if 'good' or 'great' or 'amazing' or 'really good' in response:
            responses = ['What makes your day good?', 'Did you do anything cool?', 'What fun activities did you do '
                                                                                   'today?']
            speak(random.choice(responses))
            response = r.listen(source, timeout=3)
            response = r.recognize_google(response)
            primary_storing.add(response)
            speak("That's great, do you have any other plans today?")
            response = r.listen(source, timeout=3)
            response = r.recognize_google(response)

            if 'no' or 'nah' in response:
                speak("Fair enough I'll be here in case you need me.")
                while 1:
                    y_n = input("Exit Friendly Mode?: ")
                    if y_n == 'y':
                        exit(do_stuff())
                    else:
                        continue

            elif 'yes' in response:
                speak("Nice, although if you said what you are doing I'm not sure I heard")
                response = r.listen(source, timeout=3)
                response = r.recognize_google(response)
                primary_storing.add(response)
                time.sleep(0.5)
                speak("Nice do you want any help with that?")
                response = r.listen(source, timeout=3)
                response = r.recognize_google(response)
                if 'yes' or 'ok' in response:
                    speak("would you like me to define a word, Wiki search or anything?")
                    response = r.listen(source, timeout=3)
                    response = r.recognize_google(response)

                    if 'Wiki' in response:
                        speak('What would you like to search?')
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        speak("Your results are being processed now.")
                        answer = wikipedia.summary(audio, sentences=5)
                        speak(answer)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'Define' in response:
                        speak("What is your word?")
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        word_def = PyDictionary.meaning(f"{audio}")
                        speak(word_def)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
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
            response = r.listen(source, timeout=3)
            response = r.recognize_google(response)
            primary_storing.add(response)
            speak("That's not that great, what about later today? Any plans then?")
            response = r.listen(source, timeout=3)
            response = r.recognize_google(response)
            if 'no' in response:
                speak("Okay I'll be here if you need me for anything")
                while 1:
                    y_n = input("Exit Friendly Mode?: ")
                    if y_n == 'y':
                        exit(do_stuff())
                    else:
                        continue

            if 'yes' in response:
                speak("Nice, although if you said what you are doing I'm not sure I heard")
                response = r.listen(source, timeout=3)
                response = r.recognize_google(response)
                primary_storing.add(response)
                speak("Okay, would you like help with that or should I stay quiet?")
                response = r.listen(source, timeout=3)
                response = r.recognize_google(response)

                if 'help' in response:
                    speak("How would you like me to help?")
                    response = r.listen(source, timeout=3)
                    response = r.recognize_google(response)

                    if 'Wiki' in response:
                        speak('What would you like to search?')
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        search_list.add(audio)
                        speak("Your results are being processed now, .")
                        answer = wikipedia.summary(audio, sentences=5)
                        speak(answer)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'Define' in response:
                        speak("What is your word?")
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        word_def = PyDictionary.meaning(f"{audio}")
                        speak(word_def)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'synonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        word_syn = PyDictionary.synonym(f"{audio}")
                        speak(word_syn)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'antonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        word_ants = PyDictionary.synonym(f"{audio}")
                        speak(word_ants)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'translate' in response:
                        speak("What is a word to translate?")
                        word = r.listen(source, timeout=3)
                        word = r.recognize_google(word)
                        speak('What language would you like to have the words translated to (two letters and codes '
                              'can be '
                              'found in terminal)')
                        print("Spanish: es, English: en, french: fr, German: de, Italian: it, Japanese: ja, Korean: ko "
                              "(others can be found here: https://cloud.google.com/translate/docs/languages)")
                        language = r.listen(source, timeout=3)
                        language = r.recognize_google(language)
                        lower_lang = language.lower()
                        translated = PyDictionary.translate(word, lower_lang)
                        speak(translated)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'no' in response:
                        speak("Alright, I'll be on standby just in case")
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

        elif 'ok' or 'alright' or 'fine':
            responses = ['Why is your day just fine?', 'Did you do anything today?', 'How did you go about your day '
                                                                                     'today?']
            speak(random.choice(responses))
            response = r.listen(source, timeout=3)
            response = r.recognize_google(response)
            primary_storing.add(response)
            speak("That's alright")
            speak("Are you working on any projects, work, school work I can help you with?")
            response = r.listen(source, timeout=3)
            response = r.recognize_google(response)

            if 'yes' in response:
                speak("Nice, although if you said what you are doing I'm not sure I heard")
                response = r.listen(source, timeout=3)
                response = r.recognize_google(response)
                primary_storing.add(response)
                speak("Okay, would you like help with that or should I stay quiet?")
                response = r.listen(source, timeout=3)
                response = r.recognize_google(response)

                if 'help' in response:
                    speak("How would you like me to help?")
                    response = r.listen(source, timeout=3)
                    response = r.recognize_google(response)
                    if 'Wiki' in response:
                        speak('What would you like to search?')
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        search_list.add(audio)
                        speak("Your results are being processed now, .")
                        answer = wikipedia.summary(audio, sentences=5)
                        speak(answer)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'Define' in response:
                        speak("What is your word?")
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        word_def = PyDictionary.meaning(f"{audio}")
                        speak(word_def)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'synonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        word_syn = PyDictionary.synonym(f"{audio}")
                        speak(word_syn)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'antonym' in response:
                        speak("What is your word?")
                        audio = r.listen(source, timeout=3)
                        audio = r.recognize_google(audio)
                        word_ants = PyDictionary.synonym(f"{audio}")
                        speak(word_ants)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                    elif 'translate' in response:
                        speak("What is a word to translate?")
                        word = r.listen(source, timeout=3)
                        word = r.recognize_google(word)
                        speak('What language would you like to have the words translated to (two letters, codes '
                              'can be '
                              'found in terminal)')
                        print("Spanish: es, English: en, french: fr, German: de, Italian: it, Japanese: ja, Korean: ko "
                              "(others can be found here: https://cloud.google.com/translate/docs/languages)")
                        language = r.listen(source, timeout=3)
                        language = r.recognize_google(language)
                        lower_lang = language.lower()
                        translated = PyDictionary.translate(word, lower_lang)
                        speak(translated)
                        while 1:
                            y_n = input("Exit Friendly Mode?: ")
                            if y_n == 'y':
                                exit(do_stuff())
                            else:
                                continue

                elif 'no' in response:
                    speak("Alright, I'll be on standby just in case")
                    while 1:
                        y_n = input("Exit Friendly Mode?: ")
                        if y_n == 'y':
                            exit(do_stuff())
                        else:
                            continue
            elif 'no' or 'not' in response:
                speak("Okay I'll be here to help if you need me")
                while 1:
                    y_n = input("Exit Friendly Mode?(y/n): ")
                    if y_n == 'y':
                        exit(do_stuff())
                    else:
                        continue


def release_the_hounds():
    thread = threading.Thread(speak_with_user())
    thread.start()


def calc():
    exec(open('calculator.py').read())


def afk_move():
    exec(open('movement.py').read())


def auto_click():
    exec(open('autoclicker.py').read())


def bluetooth_feedback():
    speak("We are now testing bluetooth headphones mode, do you have wireless headphones/mic connected?")
    audio = r.listen(source)
    audio = r.recognize_google(audio)
    if 'yes' or 'yeah' in audio:
        speak('We would like to know how the experience is with bluetooth.')
        response = input('Would you like to give user input later?')
        if str(response.lower()) == 'yes':
            speak('I will ask for your feedback after this session, thank you.')
            return True
        else:
            speak('Okay, thank you for considering!')
            return False


def do_stuff():  # I can have fun too
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    dictionary = PyDictionary()
    unknown_count = 0

    while 1:

        try:
            audio = r.listen(source)  # Initially listening to the source mic
            audio = r.recognize_google(audio)  # Initially Recognizing the given string values

            if 'you there' in audio:  # All of these functions are self explanatory
                speak("At your service ")

            elif 'friendly mode' in audio:
                t3 = threading.Thread(release_the_hounds())
                t3.start()

            elif 'open a new' in audio:
                speak("What would you like to open?")
                audio = r.listen(source, timeout=3)
                audio = r.recognize_google(audio)
                webbrowser.get(chrome_path).open(audio + ".com")
                speak("Tab opened ")

            elif 'time' in audio:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f", the time is {strTime}")

            elif 'sicko mode' in audio:
                speak("Astro, yeah Sun is down, freezing' cold, That's how we already know, winter's here, "
                      "My dog would "
                      "probably do it for a Louis belt, "
                      "That's just all he know, he don't know nothin' else, "
                      "I tried to "
                      "show 'em, yeah, I tried to show 'em, yeah, yeah, Yeah, yea yeah, Gone on you with the pick and "
                      "roll Yeah Sane, he in sicko mode")

            elif 'user manual' in audio:
                speak("I am Sane, "
                      "the semi-artificial nerd environment, "
                      "your friendly, self aware virtual assistant! I have been programmed to,"
                      "open tabs, search Wiki, check the time, sing horribly etc.")
                speak("Any further questions?")
                audio = r.listen(source, timeout=3)
                audio = r.recognize_google(audio)
                if 'no' in audio:
                    speak("Okay")
                elif 'explain' in audio:
                    speak("I can not explain a single function but the extended manual is on your screen now, "
                          "would you like me to read it for you?.")
                    audio = r.listen(source, timeout=3)
                    audio = r.recognize_google(audio)

                    if 'no' in audio:
                        os.open('/S.A.N.E. User Guide Extended', flags=0)
                    elif 'yes' in audio:
                        os.open('/S.A.N.E. User Guide Extended', flags=0)
                        speak("S.A.N.E. Extended User Guide: Because You Can't Properly Read the Code"
                              "Calculator: Opens the calculator that can be found in this same folder/directory. The "
                              "calculator is basic, with five functions (+, -, /, *, ^). "
                              "New Tab: Opens a new tab in google chrome, user can tell S.A.N.E. what to open through "
                              "the prompted speech time (about five seconds). "
                              "Time Check: S.A.N.E. gives the time of day for wherever your computer is located."
                              "Sicko Mode: S.A.N.E. attempts to sing the popular song sicko mode by 'jucewrld' and "
                              "horribly fails. "
                              "User Manual: S.A.N.E.'s user manual, this is the way you got here so you should know "
                              "all this command has to offer. "
                              "Wiki: Searches Wikipedia for anything you tell S.A.N.E. to search after the prompt."
                              "Power Off: S.A.N.E. refuses to power off unless you give him a death threat, "
                              "which then causes him to cripple into an exit code. "
                              "Hibernate: S.A.N.E. powers off for a given amount of seconds, "
                              "if you can not calculate the number of seconds ask S.A.N.E. for minutes and he will do "
                              "the calculation. "
                              "Auto Click: Starts the auto-clicker for any game that requires cheating."
                              "Movement: Starts the simple movement algorithm for any game that requires cheating. "
                              "Coin Flip: Flips a coin for a 50/50 heads tails outcome. "
                              "Define: Defines a word that you are prompted to tell S.A.N.E."
                              "Thank you for being patient with S.A.N.E, he's about as slow as it gets..."
                              "Hey, that last part isn't true!")

            elif 'Wiki' in audio:
                speak('What would you like to search?')
                audio = r.listen(source, timeout=3)
                audio = r.recognize_google(audio)
                search_list.append(audio)
                speak("Your results are being processed now, .")
                answer = wikipedia.summary(audio, sentences=5)
                speak(answer)

            elif 'Define' in audio:
                speak("What is your word?")
                audio = r.listen(source, timeout=3)
                audio = r.recognize_google(audio)
                word_def = dictionary.meaning(f"{audio}")
                speak(word_def)

            elif 'synonym' in audio:
                speak("What is your word?")
                audio = r.listen(source, timeout=3)
                audio = r.recognize_google(audio)
                word_syn = dictionary.synonym(f"{audio}")
                speak(word_syn)

            elif 'antonym' in audio:
                speak("What is your word?")
                audio = r.listen(source, timeout=3)
                audio = r.recognize_google(audio)
                word_ants = dictionary.synonym(f"{audio}")
                speak(word_ants)

            elif 'translate' in audio:
                speak("What is a word to translate?")
                words = r.listen(source, timeout=3)
                words = r.recognize_google(words)
                speak('What language would you like to have the words translated to (two letters and codes can be '
                      'found in terminal)')
                print("Spanish: es, English: en, french: fr, German: de, Italian: it, Japanese: ja, Korean: ko "
                      "(others can be found here: https://cloud.google.com/translate/docs/languages)")
                language = r.listen(source, timeout=3)
                language = r.recognize_google(language)
                lower_lang = language.lower()
                translated = dictionary.translate(f"{words}", f"{lower_lang}")
                speak(translated)

            elif 'calculator' in audio:
                speak("Opening the calculator in one second...")

                t2 = threading.Thread(calc())
                t2.start()

            elif 'flip' in audio:
                speak("Flipping the coin now.")
                nums = [1, 2]
                choice = random.choice(nums)
                if choice == 1:
                    speak("The outcome is tails.")

                elif choice == 2:
                    speak("The outcome is heads.")

            elif 'power off' in audio:
                if bluetooth_feedback():
                    speak("It appears its your lucky day, you had a one in 400 chance of being asked the question you "
                          "were asked at the beginning of the session, and because you answered yes we are opening "
                          "the terminal to input on bluetooth compatibility before you leave!")
                else:
                    continue

                speak("Powering off, have a good day.")
                exit()

            elif 'hibernate' in audio:
                speak("Okay how many seconds should I sleep?")
                audio = r.listen(source, timeout=3)
                audio = r.recognize_google(audio)
                speak(f"going down for {audio} seconds.")
                time.sleep(int(audio))
                speak("I'm back .")

            elif 'auto click' in audio:
                speak("Please set up the auto-clicker yourself as I can not do that.")
                auto_click()
                t2 = threading.Thread(auto_click())
                t2.start()

            elif 'movement' in audio:
                speak("Please initiate the algorithm yourself as I can not do that")
                t2 = threading.Thread(afk_move())
                t2.start()

        except sr.UnknownValueError:
            unknown_count = unknown_count + 1
            if unknown_count == 50:
                t4 = threading.Thread(the_jawbreaker())  # Built-in errors for the speech-recognition library,
                # as well as NN initialization
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

    t1 = threading.Thread(do_stuff())
    t1.start()