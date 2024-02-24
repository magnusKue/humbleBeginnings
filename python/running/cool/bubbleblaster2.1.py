from tkinter import *
import sys
HEIGHT = 800
WIDTH = 1500
playercol='red'
window = Tk()
window.title('Bubble Blaster')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg= 'darkblue')
c.pack()
ship_id =c.create_polygon(20,5,20,85,90,45, fill=playercol)
ship_id2=c.create_oval(0,0,90,90,outline=playercol)
SHIP_R = 45
MID_X = WIDTH / 2
MID_Y = HEIGHT / 2
col = 'red'
c.move (ship_id, MID_X, MID_Y)
c.move (ship_id2, MID_X, MID_Y)
SHIP_SPEED = 10
gamestate='on'

def get_coords(id_num):
    pos = c.coords(id_num)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y

def move_ship (event):
    xp, yp = get_coords(ship_id2)
    if gamestate == 'on':
        if event.keysym == 'w' and yp > 25:
            c.move (ship_id, 0,-SHIP_SPEED)
            c.move (ship_id2, 0,-SHIP_SPEED)
        elif event.keysym == 's' and yp < (HEIGHT-25):
            c.move (ship_id, 0,SHIP_SPEED)
            c.move (ship_id2, 0,SHIP_SPEED)
        elif event.keysym == 'a' and xp > 25:
            c.move (ship_id,-SHIP_SPEED, 0)
            c.move (ship_id2,-SHIP_SPEED, 0)
        elif event.keysym == 'd' and xp < (WIDTH-25):
            c.move (ship_id, SHIP_SPEED, 0)
            c.move (ship_id2, SHIP_SPEED, 0)
c.bind_all('<Key>', move_ship)

from random import randint

bub_id = list()
bub_r = list()
bub_speed = list()
bub_type = list()
MIN_BUB_R = 10
MAX_BUB_R = 40
MAX_BUB_SPD = 7
GAP = 100

def create_bubble():
    chance = randint(1, 16)
    if chance < 9:
        btype='b'
        col = 'white'
    elif chance >= 9 and chance <14:
        btype='k'
        col = 'red'
    elif chance >= 14:
        btype='b'
        col = 'yellow'
    x = WIDTH + GAP
    y = randint (0,HEIGHT)
    r = randint (MIN_BUB_R, MAX_BUB_R)
    id1 = c.create_oval(x - r, y - r, x + r, y + r, outline = col, fill = col)
    bub_id.append(id1)
    bub_r.append(r)
    bub_speed.append(randint(1, MAX_BUB_SPD))
    bub_type.append(btype)

def move_bubbles():
    for i in range(len(bub_id)):
        c.move(bub_id[i], -bub_speed[i],0)
        
def gameover():
    gamestate='off'
    c.create_text(MID_X, MID_Y,\
    text ='GAME OVER', fill='red', font=('Helvetica' ,50))
    c.create_text(MID_X, MID_Y + 30, \
    text= 'Score: '+ str(score), fill='white')
    c.create_text(MID_X, MID_Y + 45, \
    text ='Bonus time:  '+ str(bonus*TIME_LIMIT), fill='white') 
    sys.exit()

def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    del bub_type[i]
    c.delete(bub_id[i])
    del bub_id[i]
    
def clean_up_bubs ():
    for i in range (len(bub_id)-1,-1,-1):
        x,y = get_coords(bub_id[i])
        if x < -GAP:
            del_bubble(i)
from math import sqrt

def distance (id1,id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords (id2)
    return sqrt ((x2-x1)**2+(y2-y1)**2)

def collision():
    points = 0
    for bub in range (len(bub_id)-1,-1,-1):
        if distance (ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            if bub_type[bub] == 'b':
                points += (bub_r[bub] + bub_speed[bub])
                del_bubble(bub)
            elif bub_type[bub] == 'p':
                points += (bub_r[bub] + (bub_speed[bub]*2))
                del_bubble(bub)
            elif bub_type[bub] == 'k':
                gameover()
    return points

c.create_text (50, 30, text='TIME', fill='white')
c.create_text (150, 30, text='SCORE', fill='white')
time_text = c.create_text(50, 50, fill='white')
score_text = c.create_text(150, 50, fill='white')
def show_score(score):
    c.itemconfig(score_text, text=str(score))
def show_time(time_left):
    c.itemconfig(time_text, text=str(time_left))


from time import sleep, time
BUB_CHANCE = 15
TIME_LIMIT = 30
BONUS_SCORE = 1000
score = 0
bonus = 0
end = time() + TIME_LIMIT

#MAIN GAME LOOP
while time() < end:
    if randint(1, BUB_CHANCE) == 1:
        create_bubble()
    move_bubbles()
    clean_up_bubs()
    score += collision()
    if (int(score / BONUS_SCORE)) > bonus:
        bonus += 1
        end += TIME_LIMIT
    show_score(score)
    show_time(int(end - time()))
    window.update()
    sleep(0.01)

