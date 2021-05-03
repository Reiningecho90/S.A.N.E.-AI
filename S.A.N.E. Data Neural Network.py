# Imports
import speech_recognition as sr
import threading
import random
import pandas as pd
from pandas import errors as e
import pyttsx3
import enchant

dictionary = enchant.Dict("en_US")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Storage Systems
try:
    data_storing = pd.read_csv("S.A.N.EProject\S.A.N.E. Data Files\data_storing.csv", delimiter=', ', engine='python')
    network_storage = pd.read_csv("S.A.N.EProject\S.A.N.E. Data Files\\network_storage.csv", delimiter=', ', engine='python')
    common_values = pd.read_csv("S.A.N.EProject\S.A.N.E. Data Files\common_values.csv", delimiter=', ', engine='python')
    secondary_storage = pd.read_csv("S.A.N.EProject\S.A.N.E. Data Files\secondary_storage.csv", delimiter=', ', engine='python')
    print('read files')
    data_storing = data_storing.values.tolist()
    network_storage = network_storage.values.tolist()
    common_values = common_values.values.tolist()
    secondary_storage = secondary_storage.values.tolist()
    print(data_storing, network_storage, secondary_storage, common_values, sep='\n')
    print('listed files')
    data_storing.clear()
    network_storage.clear()
    common_values.clear()
    secondary_storage.clear()
    print(data_storing, network_storage, secondary_storage, common_values, sep='\n')
except e.EmptyDataError:
    pass


# Functions
def speak(speech):
    engine.say(speech)
    engine.runAndWait()


def the_jawbreaker():
    inp_count = 0
    while True:
        val = input("What would you like to search: ")
        data_storing.append(val)
        inp_count += 1
        print(inp_count)
        if inp_count > 5:
            inp_count = 0
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

            print("Running the predictor")  # Prediction algorithm is a searching loop that uses reference data
            print(network_storage)
            for i in network_storage:
                item_count = network_storage.count()
                print("Searching for an item")
                print("search done")
                
                if count > 2:
                    print(i)
                    suggestion = dictionary.suggest(i)
                    print(random.choice(suggestion))


# Completely disregard this entire section, copied from the main script and has no effect besides threading in the
# first loop and notifying  the dev of initialization

r = sr.Recognizer()  # Set recognizer
mic = sr.Microphone(device_index=1)  # Microphone set to headphones for best quality

with mic as source:
    print("Starting thread")
    t1 = threading.Thread(the_jawbreaker())  # Here's the thread for the main script
    t1.start()
