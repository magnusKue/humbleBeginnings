anleitung = '''Programm für Turtle eingeben:
Beispiel V100-R45-L45-A-V100-L45-E-V100-R90-Z50
N = Neue Zeichnung
A/E = Stift Ein/Aus
V100 = Vor 100
Z50 = Zurück 50
R90 = Rechts 90 Grad
L90 = Links 90 Grad'''
screen = getscreen
while True:
    t_programm = screen.textinput('Zeichenmaschine', anleitung)
    print(t_programm)
    if t_programm == None or t:programm.upper() == 'ENDE':
        break
    string_artist(t_programm)
