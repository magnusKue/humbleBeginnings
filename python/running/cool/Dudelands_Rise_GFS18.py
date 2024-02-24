#                       Dudeland rise




#Code für GFS 2018
#Von Magnus Küdeli
#TEXT-ADVENTURE

from time import sleep     #Importiert das modul sleep(sekunden)



def ___ende___():
    while True:                                                                      #Definiert das Spielende
        print("""
                  ####    ##    ##  ##  ####     ###   #    #  ####  ###
                 #       #  #   ######  #       #   #   #  #   #    #   #
                 #  ##   ####   # ## #  ####    #   #   #  #   #### ####             
                 #   #   #  #   #    #  #       #   #    ##    #    #  #
                  ###    #  #   #    #  ####     ###     ##    #### #   #


                                  You finished the Game 


""")                           #Zeigt einen Text an
        sleep(7)               #macht eine pause, dass der Spieler Zeit hat den Text zu lesen dieses Modul wurde importiert
        print()                #Zeilen-umbruch
sleep(8)                       #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()                        #Zeigt einen Text an
print("                             Dudelands Rise")
sleep(5)            #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()                        #Zeilen-umbruch
print("""
      Wilkommen zu meinem kleinen Text-Adventure
      
Story: Du bist Gunter, ein Astronaut auf der Weltraumstation
es ist der Morgen des 11 Novembers und du quälst
dich schlaftrunken aus dem Bett...""")     #Zeigt einen Text an
sleep(8)                 #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()                  #Zeilen-umbruch
print("Du hast plötzlich Lust auf Caffe")
sleep(3)                   #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()                    #Zeilen-umbruch
answer = input("Willst du einen kaffee? (j/n)") #Lässt den Spieler eingeben ob er Kaffee will und setzt die Antwort in die Variable answer
if answer == "j":                               #testet ob der Spieler j also ja eingegeben hat
    sleep(3)               #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    print()
    print("Du gehst in die Eingangshalle...Du erhällst 'Kaffee'")
    sleep(3)      #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    print()
    print("'Kaffee' wurde dem Inventar hinzugefügt")
    invent = "Kaffee"    
elif answer == "n":         #testet ob de Spieler n also nein eingegeben hat
    print("Aber du hast Durst!!!!")
    sleep(3)                                 #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    print()
    print("Du könntest ihn noch brauchen!")
    sleep(3)                                    #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    print()
    print("Tya...zu spät")
    invent = "leer"
    print("Du ziehst dich an und verlässt den Schlafsal")
sleep(7)       #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()
print("""Das bist DU

               _____
               ||-||
           ____|   |____
           |           |
           |  |     |  |
           |  |     |  |
           ---|     |---
              |  |  |
              |  |  |
              |  |  |
-------------------------------------
                    """)
sleep(6)                             #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()

sleep(3)                     #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()
print("Plötzlich erstarrst du...")
sleep(3)              #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()
answer = input("Ein Alien(Kampf|oder|Reden)") #Setzt die Variable answer auf die Eingabe des Spielers
if answer == "Reden":               #testet ob di Antwort des spielers Reden war
    print("""
                   |     |
                 )---------(
                              """)
    print("Du redet mit ihm:'Hallo'sagst du,'Wie heißt du denn?")
    print("Der Alien Rülpst dir ins Gesicht.Er kommt auf dich zu und sagt 'ich bin huskulala aber ich muss jetzt los. Bye'")
    print("Der Alien Geht")
    sleep(6)          #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    print()
elif answer =="Kampf":            #testet ob die Antwort des spielers Kampf war
    print("Du ziehst den Laser und schießt...Treffer")
    sleep(5)               #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    print()

print("""Du freust dich
              _    _
              |    |
              -    -
             )\____/(
                       """)
sleep(3)            #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()
print("Doch du siehst schon die nächste Gefahr: Alien-Käfer auf dem Boden")
answer = input("Was willst du tun?  (Treten|Schießen|Verscheuchen|Kaffee)")
if answer == "Kaffee":          #testet ob di Antwort des spielers Kaffee war
    if invent == "Kaffee":            #Testet ob der Spieler einen Kaffee besitzt
        print("Du nimmst deinen ungetrunkenen Kaffee und gießt ihn über die Käfer")
        print("Du rufst 'Ha' und feierst dich selbst")
        sleep(6)                  #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    else:                            #Sollte der Spieler keinen Kaffee besitzen wird folgender Code aktiviert
        print("Kein Kaffe...Ich sagte doch den wirst du noch brauchen")
        ___ende___()
        sleep(6)        #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
elif answer == "Treten":                #Testet ob die Antwort des Spielers Treten war
    print("""Du tritst auf die Käfer...Nur haben die einen Titan-Panzer.
             Sie knabbern sich in das Schaltpult und fliehen.
             'Na prima!' Das darfst du später reparieren denkst du belidigt""")
    sleep(6)                 #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
    print()
elif answer == "Schießen":       #Testet ob die Antwort des Spielers Schießen war   
    print("""Du ziehst den Laser
              ________                           ____
              | ______| - - - - - - - - - - - - <.___>  <--Käfer
              |_|
              
               Zack-Alle Weg               """)
    print("""Du freust dich wieder
       
                       """)
    sleep(6)       #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
elif answer == "Verscheuchen":            #Testet ob die Antwort des Spielers verscheuchen war
    print("Du holst ein Feuerzeug um die Käfer zu verscheuchen.Käfer hassen Feuer")
    print("Sie springen vor Schreck in alle Richtungen und du fällst hin. ")
    print("Das Feuerzug fällt dir aus der Hand und zünde die Raumstation an")
    print("Du musst in einer rettungkapsel fliehen")
    ___ende___()
    sleep(8)          #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print("""Die Raumstation ist gerettet...
         Du holst dir ein Lustiges Taschenbuch, legst dich hin und beginnst
         zu lesen.
         Das war ein Happy-End!
         
         """)
sleep(10)               #macht eine pause, dass der Spieler Zeit hat den Text zu lesen
print()
___ende___()


#             _    _   Ende! Ich hoffe es hat dir gefallen
#             |    |   Und du versuchstdich vielleicht selbst
#             -    -   mal am Programmieren. |-|
#>>>>>>>>>>  )\____/( >>>>>>>>>>>>>>>>>>-Magnus-<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


