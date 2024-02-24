from tkinter import *
from time import sleep
from random import randint, choice
from math import sqrt

window = Tk()
window.title('LeagueOfGods')
c = Canvas(window, width=800, height=600, bg='green')
c.pack()
Player = c.create_oval(0, 0, 30, 30, fill='black', state=HIDDEN)
c.move(Player, 225, 90)
Run = c.create_text(240, 130, text='LeagueOfGods', fill='black', font=('Helvetica', 30))
window.update()
sleep(3)
c.itemconfig(Player, state=NORMAL)
c.itemconfig(Run, state=HIDDEN)
window.update()
sd = 5
def Walk(event):
    key =event.keysym
    if key == 'Up':
        c.move(Player, 0, -sd)
    elif key == 'Down':
        c.move(Player, 0, sd)
    elif key == 'Left':
        c.move(Player, -sd, 0)
    elif key == 'Right':
        c.move(Player, sd, 0)
c.bind_all('<Key>', Walk)
def hol_koort(figur):
    pos = c.coords(figur)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[4])/2
    return x, y
randomC = 100
points = list()
def new_point():
    xR = randint(0, 750)
    yR = randint(0, 550)
    dR = randint(5, 60)
    col = choice(['green'])
    c.create_oval(xR, yR, xR + dR, yR + dR, fill=col, outline='black')
    window.update()
    
def del_Point(z):
    del points[z]
    c.delete(z)
    
def entf_p():
    for p in points:
        del_Points(p)
        new_point

def distance(fig1, fig2):
    x1, y1 = hol_koort(fig1)
    x2, y2 = hol_koort(fig2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def ende():
    for o in points:
        del_Point(o)
        c.itemconfig(Run, state=NORMAL, text='Ende', font=('Helvetica', 50))
        c.itemconfig(Player, state=HIDDEN)
        c.itemconfig(Canvas, bg='red')
def inside():
    ortY, ortX = hol_koort(Player)
    if ortX < 0 or ortY < 0:
        c.move(Player, 8, 8)
        
while True:
    if randint(1, 100) ==16:
        new_point()
        window.update()
        for s in points:
            if not distance(str(o), Player) > 0:
                print('[]')
    window.update()
    sleep(0.001)
    
