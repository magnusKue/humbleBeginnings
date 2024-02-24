from tkinter import *
from turtle import *
from time import sleep
import subprocess
#Kennwort
b = False
window = Tk()
window.title('GreenLay')
c = Canvas(window, width=700, height=500, bg='black')
c.pack()
window.update()
key= 'greenSkull'
txt = 'Bitte geben sie ihr Passwort ein'
screen = getscreen()
while True:
    t_programm = screen.textinput('Passwort', txt)
    print(t_programm)
    if t_programm == key:
        b = True
        print('Passwort korekt eingegeben')
    if b == True:
        break
name1  = c.create_text(240, 130, fill='green', text='GreenLay', font=('Helvetica', 20))
name2  = c.create_text(240, 160, fill='white', text='Made by GreenSkull', font=('Helvetica', 12))
window.update()
subprocess.Popen(['omxplayer', 'illuminati song - Anonymous (Lyrics).mp3'])
print('Login-erfolgreich')
sleep(4)
c.itemconfig(name1, state=HIDDEN)
sleep(1)
window.update()
sleep(1)
c.itemconfig(name2, state=HIDDEN)
window.update()
sleep(4)
window.config(bg='blue')
from time import *
d = localtime()
Tag = d.tm_mday
Std = d.tm_hour
minute = d.tm_

