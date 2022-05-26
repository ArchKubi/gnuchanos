from asyncio import events
import PySimpleGUI as pg

pg.theme("DarkPurple6")

layout = [
    [
    pg.Text("Fuck This QT5 and GTK"),
    pg.InputText(),
    ],
    [

        pg.Column()
    ]
    [
    pg.Button("Fuck!"), pg.Button("ASS")
    ]



]

window = pg.Window("Form", layout)

while True:
    event, values, = window.read()
    if event == "ASS" or event == pg.WIN_CLOSED:
        break
    print(values[0])
