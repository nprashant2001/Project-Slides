#make sure to import rpy2, pysimpleGUI, pillow

import PySimpleGUI as sg
import os.path
from tkinter import *

sg.theme('BlueMono')

# This creates the widgets for the left column
file_list_column = [
    [
        #creating your image browsing button
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        #dropdown list to see the image files to choose from
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
    [sg.Button('Click counter')],
]

# This creats the text that is displayed above the image
image_viewer_column = [
    [sg.Text("Choose an image from list on left:")],
    [sg.Text(size=(100, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

# Segmenting the program into different sections
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),

    ]
]

# Creating the window, naming it, and adding our layout to the window
window = sg.Window("Image Viewer", layout).Finalize()
window.Maximize()

# Event loop
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED: #if they wanna exit this lets them do that
        break

    if event == "Click counter":
        class clickCount:

            def clicks(self, event):
                # clicks = 0
                global count
                count += 1
                return count

            def main(self, h, w):
                root = Tk()
                root.minsize(h, w)
                root.attributes('-alpha', 0.25)
                root.bind("<Button-1>", self.clicks)
                root.mainloop()
                return count


        count = 0
        height, width = 700, 500  # sample window/image size
        total = clickCount()
        print(total.main(height, width))

    # If the folder button function is called, make a list of files in the folder
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
               and f.lower().endswith((".png", ".jpg")) #this is the file types that our progam will accept
        ]
        window["-FILE LIST-"].update(fnames) #This will be updating the file list

    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

