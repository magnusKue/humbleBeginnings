from tkinter import *
from time import sleep
window = Tk()
window.title('Name')
c = Canvas(window, width=600, height=350, bg='black')
c.pack()
text = c.create_text(249,0, text='Ein Baum ist ein Baum', fill='green', font=(120))
window.update()
def hole_koords(ID):
    pos = c.coords(ID)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y
while True:
    c.move(text, 0, 5)
    sleep(0.4)
    window.update()
    
