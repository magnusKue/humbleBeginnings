from tkinter import *
from time import sleep

window = Tk()
ball = 'off'
c = Canvas(window, width=500, height=320, bg='green')
def Ball():
    c.pack()
    ball1 = c.create_oval(0, 0, 10, 10, fill='red', outline='black')
    c.move(ball1, 150, 80)
    ball = 'True'
def oval():
    c.pack()
    ball = 'False'
    oval = c.create_oval(100, 100, 300, 200, fill='red', outline='black')
butB = Button(window, text='Kreis', command=Ball)
butO = Button(window, text='Oval', command=oval)
butB.pack()
butO.pack()
sleep(1)
window.update()

