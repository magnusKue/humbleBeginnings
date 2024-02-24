from random import randint
name = input('Wie hei&t du?')
print('Hallo', name)
aw = input('Start? (j/n)')
if aw == 'j':
    print('Start')
    print('Geister game')
    Du_hast_mut = True
    score = 0
    while Du_hast_mut:
        geistertuer = randint(1, 3)
        print('Vor dir sind drei Türen.')
        print('Hinter einer ist ein Geist.')
        print('Welche Türe wählst du?')
        tuer = input('1, 2 oder 3')
        tuer_nummer = int(tuer)
        if tuer_nummer == geistertuer:
            print('Verloren!!!')
            print('Vor dir ist ein geist.')
            print('Er hat hunger...')
            Du_hast_mut = False
        else:
            print('Kein geist!')
            print('Du bist ein Zimmer weiter!')
            score = score + 1
    print('Du wurdest gefressen!')
    print('Deine Punkte:', score) 
elif aw == 'n':
    print('Bye')
elif aw == 'save user':
        print('Geheimcode wurde erkannt!')
        print('Wilkommen!')
        name = 'Boss'
        print('Ihr status wurde auf boss geändert!')
        hp = input('Hallo Boss')
        if hp == 'Hi':
            hdgdl = input('Wie geht es ihnen?')
            if hdgdl == 'gut':
                print('Das ist schön!')
                pups = input('Wollen sie spielen, Boss?')
                if pups == 'Ja':
                    print('Start')
                    print('Geister game')
                    Du_hast_mut = True
                    score = 0
                    while Du_hast_mut:
                        geistertuer = randint(1, 3)
                        print('Vor dir sind drei Türen.')
                        print('Hinter einer ist ein Geist.')
                        print('Welche Türe wählst du?')
                        tuer = input('1, 2 oder 3')
                        tuer_nummer = int(tuer)
                        if tuer_nummer == geistertuer:
                           print('Verloren!!!')
                           print('Vor dir ist ein geist.')
                           print('Er hat hunger...')
                           Du_hast_mut = False
                        else:
                            print('Kein geist!')
                            print('Du bist ein Zimmer weiter!')
                            score = score + 1
                            print('Du wurdest gefressen!')
                            print('Deine Punkte:', score)
                elif pups == 'nein':
                    print('OK!Bye!')                
else:
    print('Geben sie bitte eine korekte Antwort!')

