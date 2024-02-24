from tkinter import *
from time import sleep, time
window = Tk()
window.title('Alien')
c = Canvas(window, height=300, width=400)
c.pack()
Körper = c.create_oval(100, 150, 300, 250, fill='green')
auge = c.create_oval(170, 70, 230, 130, fill='white')
pupille = c.create_oval(190, 90, 210, 110, fill='black')
mund = c.create_oval(150, 220, 250, 240, fill='red')
hals = c.create_line(200, 150, 200, 130)
hut = c.create_polygon(180, 75, 220, 75, 200, 20, fill='blue')
def mund_auf():
    c.itemconfig(mund, fill='black')
def mund_zu():
    c.itemconfig(mund, fill='black')
def lid_zu():
    c.itemconfig(auge, fill='green')
    c.itemconfig(pupille, state=HIDDEN)
def lid_auf():
    c.itemconfig(auge, fill='white')
    c.itemconfig(pupille, state=NORMAL)
worte = c.create_text(200, 280, text='Ich bin ein Alien!')
def hut_weg():
    c.itemconfig(hut, state=HIDDEN)
    c.itemconfig(worte, text='Gib den Hut zurück!')
window.attributes('-topmost', 1)
def rülps (event):
    mund_auf()
c.itemconfig(worte, text='Rülps!')
c.bind_all('<Button-1>', rülps)
def lid_zu2(event):
    c.itemconfig(auge, fill='green')
    c.itemconfig(pupille, state=HIDDEN)
def lid_auf2(event):
    c.itemconfig(auge, fill='white')
    c.itemconfig(pupille, state=NORMAL)
c.bind_all('<KeyPresst-a>', lid_zu())
c.bind_all('<KeyPresst-z>', lid_auf())
