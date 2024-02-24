from UEngine02v import *
import pygame

clock = pygame.time.Clock()
from pygame.locals import *
success, failures = pygame.init()

print(f'Success: {success}, failures: {failures}')
pygame.display.set_caption('Points')

WINDOW_SIZE = (1200,800)
origin = Vec(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)
display = pygame.display.set_mode(WINDOW_SIZE)

def circles(originCirc,originRot,speedRot, rad, numb):
    points = []
    for elem in getVertsInCircle(originCirc,numb, rad):
        points.append([elem, originRot,-speedRot])
    return points

levels = {}
#             spawn,   rotatingBulletllists, goal, linear[origin, speed, range, axis(1=x,0=y), radius, verzögerung], borders[rect(),rect()]
levels[1] = [Vec(8,8), [ circles(origin, origin, -0.1, 300, 24),circles(origin, origin, -2.1, 100, 5),circles(origin, origin, 1.5, 200, 12)] ,origin, [[origin, 0.01, 200, 1, 10,0],[origin, 0.01, 200, 0, 10,0],[origin, -0.01, 200, 0, 10,0],[origin, -0.01, 200, 1, 10,0]]]
levels[2] = [Vec(300,300),[circles(Vec(200,100), Vec(200,100), -5, 100, 2),circles(Vec(200,300), Vec(200,300), -8, 50, 5)],Vec(200,100), []]

def loadLevel(lev):
    points = levels[lev][1]
    spawn = levels[lev][0]
    goal = levels[lev][2]
    linearMotions = levels[lev][3]
    return points, spawn, goal, linearMotions

running = True
time = 1
class Player:
    def __init__(self,rad,speed):
        self.position = Vec(20,20)
        self.velocity = Vec(0,0)
        self.radius = rad
        self.color = (0,255,255)
        self.speed = 2
        self.friction = .7
        self.isDashing = False
        self.spawnpoint = self.position
player = Player(10,20)
class directions:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
moving = directions()
movmentAllowed = True
level = 1
time = 1
points, player.spawnpoint, goal, linearMotions = loadLevel(level)
#print(points)
while running:
    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_w:
                moving.up = True
            if event.key == K_s:
                moving.down = True
            if event.key == K_a:
                moving.left = True
            if event.key == K_d:
                moving.right = True
            if event.key == K_LSHIFT:
                player.isDashing = True
        if event.type == KEYUP:
            if event.key == K_w:
                moving.up = False
            if event.key == K_s:
                moving.down = False
            if event.key == K_a:
                moving.left = False
            if event.key == K_d:
                moving.right = False
            if event.key == K_LSHIFT:
                player.isDashing = False

    if movmentAllowed:
        if moving.right:
            player.velocity.x += player.speed
            if player.isDashing:
                player.velocity.x += player.speed/2
        if moving.left:
            player.velocity.x -= player.speed
            if player.isDashing:
                player.velocity.x -= player.speed/2
        if moving.up:
            player.velocity.y -= player.speed
            if player.isDashing:
                player.velocity.y -= player.speed/2
        if moving.down:
            player.velocity.y += player.speed
            if player.isDashing:
                player.velocity.y += player.speed/2

        player.velocity.x *= player.friction
        player.velocity.y *= player.friction
        player.position = addVec(player.position, player.velocity)
        player.position.x = clamp(player.position.x,0+player.radius, WINDOW_SIZE[0]-player.radius)
        player.position.y = clamp(player.position.y,0+player.radius, WINDOW_SIZE[1]-player.radius)
        


    for x in range(len(points)):
        #liste voll listen von 
        #verschiedene bullet typen (lv1:2)
        for y in range(len(points[x])):
            #bullet (punkt, originRot, speed)
            if circleCol(Circle(player.position, player.radius), Circle(points[x][y][0], 10)):
                player.position = player.spawnpoint
                break

            points[x][y][0] = rotate(points[x][y][1], points[x][y][0], points[x][y][2])
            pygame.draw.circle(display, (255,0,0), (points[x][y][0].x, points[x][y][0].y),10,1)

    pygame.draw.circle(display, (100,255,100), (goal.x, goal.y),10,1)
    pygame.draw.circle(display, player.color, (player.position.x, player.position.y),player.radius,1)


    for linear in range(len(linearMotions)):
        #lv1: 2
        print(linearMotions[linear])
        if linearMotions[linear][3] == 0:
            coord = Vec(linearMotions[linear][0].x, linearMotions[linear][0].y + math.sin(time * linearMotions[linear][1]+linearMotions[linear][5])*linearMotions[linear][2])
        elif linearMotions[linear][3] == 1:
            coord = Vec( linearMotions[linear][0].x + math.sin(time * linearMotions[linear][1]+ linearMotions[linear][5])*linearMotions[linear][2], linearMotions[linear][0].y)
        pygame.draw.circle(display, (255,0,0), (coord.x, coord.y),linearMotions[linear][4],1)

        if circleCol(Circle(player.position, player.radius), Circle(coord, linearMotions[linear][1])):
                player.position = player.spawnpoint
                break
#goal collision
    if circleCol(Circle(player.position, player.radius), Circle(goal, 10)):
        level +=1
        if level > len(levels):
            level = len(levels)
            print("win")
            #win()
        points, player.spawnpoint, goal, linearMotions = loadLevel(level)
        player.position = player.spawnpoint
   
    pygame.display.flip()
    display.fill((0,0,0))
    time+=1
    print(time)
    deltatime = clock.tick(60)
pygame.quit()