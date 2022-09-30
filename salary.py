import PySimpleGUI as sg
import math

def round_nearest2(x):
    return round (round(x / 0.05) * 0.05, -int(math.floor(math.log10(0.05))))

def round_nearest2_UP(x):
    return round (math.ceil(x / 0.05) * 0.05, -int(math.floor(math.log10(0.05))))

def round_nearest2_DOWN(x):
    return round (math.floor(x / 0.05) * 0.05, -int(math.floor(math.log10(0.05))))

sg.theme("DarkAmber")

layout = [[sg.Text("Enter the hours worked")],
        [sg.InputText(key = "-INPUT-")],
        [sg.Button("Calculate"), sg.Exit()],
        [sg.Text('',key = '-OUTPUT-')],
        [sg.Text('',key = '-BRUT-', text_color = "green")],
        [sg.Text('',key = '-AVS-', text_color = "red")],
        [sg.Text('',key = '-LPCFam-', text_color = "red")],
        [sg.Text('',key = '-AC-', text_color = "red")],
        [sg.Text('',key = '-Impot_source-', text_color = "red")],
        [sg.Text('',key = '-DEDUCT-', text_color = "red")]]


window = sg.Window("FK Net Salary Calculator", layout, finalize = True)
window['-INPUT-'].bind("<Return>", "_Enter")

while True:
    event, values = window.read()
    print(event, values)

    if (event == "Calculate") or event == ("-INPUT-" + "_Enter") :
        horaire = round_nearest2(float(values["-INPUT-"]) * 27.7)
        indem = round_nearest2(horaire * 0.0833)
        total_brut = round_nearest2(horaire + indem)
        AVS = round_nearest2_UP(total_brut * 0.053)
        LPCFam = round_nearest2(total_brut * 0.0006)
        AC = round_nearest2_DOWN(total_brut * 0.0110)
        Impot_source = round_nearest2_UP(total_brut * 0.1156)
        total_net = total_brut - AVS - LPCFam - AC - Impot_source
        total_net = round_nearest2(total_net)
        deductions = AVS + LPCFam + AC + Impot_source
        window['-OUTPUT-'].update(f"NET : {str(total_net)} CHF")
        window['-BRUT-'].update(f"BRUT : {str(total_brut)} CHF")
        window['-AVS-'].update(f"AVS : {str(AVS)} CHF")
        window['-LPCFam-'].update(f"LPCFam : {str(LPCFam)} CHF")
        window['-AC-'].update(f"AC : {str(AC)} CHF")
        window['-Impot_source-'].update(f"IMPOT : {str(Impot_source)} CHF")
        window['-DEDUCT-'].update(f"DEDUCTIONS : {str(deductions)} CHF")
    elif event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
