import PySimpleGUI as sg
import qrcode
import os


layout = [
    [sg.Image(key="-IMAGE-", size=(300,300))],
    [sg.Input(size=(25, 1), key="-WEB_ADDRESS-")],
    [sg.Button("Generate QR Code")]
]

window = sg.Window("Image Viewer", layout)

def generate_qr_code(link):
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    file_name = "qr_code"+ ".png"
    path = os.path.join(os.getcwd(), file_name)
    img.save(path)
    return path

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Generate QR Code":
        web_address = values["-WEB_ADDRESS-"]
        qr_code_image_path = generate_qr_code(web_address)
        window["-IMAGE-"].update(filename=qr_code_image_path)

window.close()