###  Inventar

codes = list()
data = list()

def new():
    print('Unter welchem Code soll abgespeichert werden?')
    ic = input('>   ')
    if not ic in codes:
        codes.append(ic)
        print('gespeichert')
    print('Welche Datei soll darunter abgespeichert werden?')
    ii = input('>   ')
    if not ii in data:
        data.append(ii)
        print('gespeichert')
    
def delt():
    print('Welche Datei soll gelöscht werden?')
    id = input('>   ')

def beende():
    print()



print('''
1)Objekt hinzufügen
2)Objekt löschen
3)Liste anzeigen
4)Inventar beenden''')
inp = input('>   ')
if inp == 1:
    new()
elif inp == 2:
    delt()
elif inp == 3:
    print(codes,   data)
elif inp == 4:
    beende()
