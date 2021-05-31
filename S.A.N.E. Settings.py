import json
import tkinter as tk

root = tk.Tk()
root.title('S.A.N.E. Settings Configuration')
root.wm_iconbitmap('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Icon.ico')


def set_voice_gender():
    print('Run')
    print(settings_file_d["GENDER"])
    if settings_file_d['GENDER'] == 'MALE':
        settings_data = {
                        "GENDER": "FEMALE"
                        }

        settings_file = open('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\settings.json', 'w')
        json.dump(settings_data, settings_file)
        print(f'Gender changed')
        settings_file.close()
        exit()

    elif settings_file_d["GENDER"] == "FEMALE":
        settings_data = {
                        "GENDER": "MALE"
                        }

        settings_file = open('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\settings.json', 'w')
        json.dump(settings_data, settings_file)
        print(f'Gender changed')
        settings_file.close()
        exit()


settings_file = open('C:\\Users\\Reinier\\PycharmProjects\\GitHub Projects\\S.A.N.EProject\\S.A.N.E. Data Files\\settings.json', 'r')
settings_file_d = json.load(settings_file)
settings_file.close()

GENDER_SELECT = tk.Button(root, text=f'Toggle Gender', bg='white', fg='black', command=set_voice_gender)
GENDER_SELECT.pack()

root.mainloop()
