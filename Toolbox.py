'''main menu module for projekt ITHS24
shows meny and runs scripts imported as modules
through subprocessess'''

import subprocess
import sys

def menu():
    '''funtion for showing and handling the menu'''
    menu_dict = {
        "1": "API fuzzer",
        "2": "hashTool",
        "3":"cryptool",
        "4": "Exit"
    }

    for keys,values in menu_dict.items():
        print(f"{keys}. {values}")

    choice: str = input("\nAnge val: ")
    print("---------------------------------")
    if choice == "1":
        subprocess.run(["python","apifuzz.py", "-h"], check=True)
        print("")
        args = input("commands: ").split(" ")
        print("")

        try:
            subprocess.run(["python","apifuzz.py", *args], check=True,text=True)
        except subprocess.CalledProcessError as sub_e:
            print(f"Invalid command: {sub_e}")

    elif choice == "2":
        subprocess.run(["python","hashtool.py", "-h"], check=True)
        print("")
        args = input("commands: ").split(" ")
        print("")

        try:
            subprocess.run(["python", "hashtool.py", *args], check=True, text=True)
        except subprocess.CalledProcessError as sub_e:
            print(f"Invalid command: {sub_e}")

    elif choice == "3":
        subprocess.run(["python","crypto_tool.py", "-h"], check=True)
        print("")
        args = input("commands: ").split(" ")
        print("")

        try:
            subprocess.run(["python","crypto_tool.py", *args], check=True)
        except subprocess.CalledProcessError as sub_e:
            print(f"Invalid command: {sub_e}")

    elif choice == "4":
        print("Exiting...")
        sys.exit()

    else:
        print("Ogiltigt val! Välj mellan 1-4")

menu()
