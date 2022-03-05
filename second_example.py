import io
import os
import PySimpleGUI as sg
from PIL import Image

file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
layout = [
    [sg.Image(key="-IMAGE-")],
    [
        sg.Text("Image File"),
        sg.Input(size=(25, 1), key="-FILE-"),
        sg.FileBrowse(file_types=file_types),
        sg.Button("Load Image"),
    ],
]

window = sg.Window("Image Viewer", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Load Image":
        filename = values["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            image.thumbnail((400, 400))
            bio = io.BytesIO()
            # Actually store the image in memory in binary 
            image.save(bio, format="PNG")
            # Use that image data in order to 
            window["-IMAGE-"].update(data=bio.getvalue())

window.close()