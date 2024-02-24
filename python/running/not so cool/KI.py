print('Wilkommen! Ich bin Lisa, eine lernende KI')
print('Rede! (Bitte keine Satzzeichen verwenden)')
no = ['Ich verstehe nicht', 'Kp XD', '...', 'ähhhh...', 'Tja...das muss ich noch lernen', 'Äh', 'Kp Dude', 'Nö ; )', 'HALT STOP! JETZT REDE ICH']
from random import choice
while True:
    answers=list()
    answer=input('>   ')
    answers1=answer.lower()
    answers=answers1.split()
    if 'hunger' in answers:
        if 'keinen' in answers:
            print('Ich habe auch keinen Hunger')
        else:
            print('Ich habe auch Hunger')
    elif 'durst' in answers:
        if 'keinen' in answers:
            print('Ich habe auch keinen Durst')
        else:
            print('Ich habe auch Durst')
    elif 'mag' in answers:
        if 'ich' in answers:
            if 'keine' in answer or 'kein' in answer:
                print('Das mag ich auch nicht!')
            else:
                print('Ich mag das auch!')
    elif'hasse' in answers:
        if 'nicht' in answers or 'keine' in answers or 'kein' in answers:
            print('Ich auch nicht')
        else:
            print('Ich auch!')
    elif 'hi' in answers or 'hallo' in answers:
        print('Hi')
    elif 'witz' in answers:
        print('''gehen zwei PIs im Wald spazieren. Sagt der
eine zum Anderen: "Komm! Lass Beeren sammeln"

HaHaHa''')
    elif 'kunst' in answers or 'bild' in answers:
        print('''Ich bin künstlerisch begabt:
             ###      ####
              ###    ###
               ###  ###
                ######
              ##########
            ##############
            ##############
            ##############
             ############
              ##########
                 ####''')
    
    else:
        print(choice(no))
    if 'lol' in answers:
        print('XD')
