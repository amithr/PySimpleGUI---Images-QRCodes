import PySimpleGUI as sg
import os

layout = [
            [sg.Image(filename='test_image_2.png')],
            [sg.Button('Exit')]
        ]

window = sg.Window("Image Viewer", layout)

while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

window.close()