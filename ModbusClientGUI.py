import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Select Modbus Protocol',size=(20,1)),sg.InputText('TCP',size=(10,1))],
            [sg.Text('Starting Register',size=(20,1)), sg.InputText('1',size=(10,1))],
            [sg.Text('Number of Register',size=(20,1)), sg.InputText('4',size=(10,1))],
            [sg.Text('Slave Id',size=(20,1)), sg.InputText('2',size=(10,1))],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('TCP/RTU Client', layout, auto_size_text=False,auto_size_buttons=False, resizable=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    for i in range(0,4):
        print('You entered ', values[i])
