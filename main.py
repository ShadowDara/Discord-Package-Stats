# This script is written by ShadowDara

# Github: https://github.com/ShadowDara

# Version 1.0.0

# GitHub Repository: https://github.com/ShadowDara/Discord-Package-Stats

import os
import pickle

skript_verzeichnis = os.path.dirname(os.path.abspath(__file__))
settings_file = "settings"
full_path = os.path.join(skript_verzeichnis, settings_file)

def startmenu():
    choice = input("""Welcome to Discord Package Stats

0. Press 0 to exit the Programm.
1. Press 1 to open the settings.
2.

Your Choice: 
""")
    if choice == '0':
        pass # The Programm closes
    elif choice == '1':
        settings_msg()
    elif choice == '2':
        pass
    else:
        print("\n Invalid Input.! Please try again!")
        startmenu()

# suche nach settings file, wenn settings file nicht gefunden wird erstelle ein neues
def check_settings_file():
    try:
        with open("settings", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line.startswith("//") or not line:
                    continue

                print(line)

    except:
        create_settings_file()

def create_settings_file():
    with open('settings', 'w') as file:
        write_default_settings()


def write_default_settings():
    pass

def settings_msg():
    pass

if __name__ == '__main__':
    """
    print("Folder path:", skript_verzeichnis,
          "\n\nLaunching Version 1.0.0 of Discord Package Stats by Shadowdara\n")
    check_settings_file()
    basic_settings()
    startmenu()
    """
    create_settings_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
