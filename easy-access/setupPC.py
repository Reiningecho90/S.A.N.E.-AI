from cx_Freeze import setup, Executable

base = "Win32GUI"

executables = [Executable("S.A.N.E. Assistant.py", base=base)]

packages = ["idna", "keyboard", "pynput", "tkinter", "time", "speech_recognition", "pyttsx3", "webbrowser", "datetime",
            "threading", "wikipedia", "os", "random", "PyDictionary", "googlesearch"]
options = {
    'build_exe': {
        'packages': packages,
        'build_exe': './/S.A.N.E. DEV BUILD'
    },
}

setup(
    name="S.A.N.E.",
    options=options,
    version="0.1",
    description='Virtual Assistant',
    executables=executables,
    icon='S.A.N.E Icon.ico'
)

# Run: 'python setupPC.py build' to build the directory when new update is finished
