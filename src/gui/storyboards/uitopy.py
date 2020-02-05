'''
PICK Tool: Team6 - Team404

Program Purpose:
        - Converts all .ui files in a directory to .py files

Date:
        - February 2020

Dependencies:
        - pyqt5
        - tkinter

NOTES:

'''

import os
from tkinter import filedialog
from tkinter import *

def get_directory():
    """GUI for user to select directories"""
    # SYSTEM DISPLAYS GUI FOR USER TO LOCATE DIRECTORY
    root = tkinter.Tk()
    root.withdraw()
    try:
        ui_folder = filedialog.askdirectory(initialdir="/",
                                            title=header_message,
                                            )
    except FileNotFoundError:
        pass

    if not root:
        pass
    return ui_folder


def convert_files():
    location = "/Users/mmedina-a/Desktop/ui"
    for file in os.listdir(location):
        if file.endswith(".ui"):
            filename = location+"/"+str(file)
            print(filename)
            new_filename = (filename[:-2]+"py")
            os.system("pyuic5 -x %s -o %s" % (filename, new_filename))


def main():
    convert_files()

main()