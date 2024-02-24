from UEngine02v import *
import pygame, random
from pygame import gfxdraw

clock = pygame.time.Clock()
from pygame.locals import *
success, failures = pygame.init()

print(f'Success: {success}, failures: {failures}')
pygame.display.set_caption('Its all circles')

WINDOW_SIZE = (1200,800)
origin = Vec(WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/2)
display = pygame.display.set_mode(WINDOW_SIZE)

font = pygame.font.SysFont("Mukta-Medium.ttf", 72)
fontSmol = pygame.font.SysFont("Mukta-Medium.ttf", 30)

def circles(originCirc,originRot,speedRot, rad, numb):
    points = []
    for elem in getVertsInCircle(originCirc,numb, rad):
        points.append([elem, originRot,-speedRot])
    return points

def line(originLine, originRot, length, res, startrot, speed):
    points = []
    for x in range(0, int(length), int(res)):
        points.append([Vec(originLine.x+x, originLine.y), originRot, speed])
    return points

class Level:
    def __init__(self):
        self.spawnpoint = Vec(0,0)
        self.goal = Vec(0,0)
        self.rotatelist = []
        self.linearlist = []
        self.borderlist = []
        self.keys = []
        self.bounce = False
        self.graphlist = []
        self.wind = Vec(0,0)
        self.movementType = 0 # 0 = topdown, 1 = 1D, 2 = sideview 
        self.staticList = []

class rectObj:
    def __init__(self, pos, size):
        self.position = pos
        self.size = size
    def getVerts(self):
        return [Vec(self.position.x, self.position.y), Vec(self.position.x, self.position.y + self.size.y), Vec(self.position.x + self.size.x, self.position.y), Vec(self.position.x + self.size.x, self.position.y + self.size.y)]

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
        self.standartFrict = self.friction
        self.jumpforce = 25

class directions:
    def __init__(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False

class Particle:
    def __init__(self, pos, col = (240,240,240), thick = 1, typep=0):  # type0=movement, type1 = death
        self.position = pos
        self.size = 5
        self.startsize = self.size
        self.lifetime = random.randint(55,70)
        self.born = self.lifetime
        self.color = col
        self.thick = thick
        self.type=typep
    def update(self):
        self.lifetime -= 1
        self.size = (self.lifetime/self.born) * self.startsize


player = Player(10,20)

levels = {}
#             spawn,   rotatingBulletllists, goal, linear[origin, speed, range, axis(1=x,0=y), radius, verzögerung], borders[rect(),rect()]

levels[1] = Level()
levels[1].spawnpoint = Vec(422, 321)
levels[1].goal = origin
levels[1].rotatelist = [circles(origin, origin, -5, 100, 2),circles(origin, origin, -2, 50, 3),circles(origin, origin, 100, 350, 300)]
levels[1].linearlist = []
levels[1].keylist = []
levels[1].friction = player.standartFrict

levels[2] = Level()
levels[2].spawnpoint = Vec(9,9)
levels[2].goal = Vec(50,50)
levels[2].rotatelist = [circles(subVec(origin,Vec(200,100)), subVec(origin,Vec(200,100)), -.8, 200, 9),circles(subVec(origin,Vec(200,100)), subVec(origin,Vec(200,100)), -.8, 150, 6), circles(Vec(782, 461), Vec(782, 461), 2, 100, 8),circles(Vec(796, 163), Vec(796, 163), 2, 100, 5)]
levels[2].linearlist = []
levels[2].keylist = [[subVec(origin,Vec(200,100)), False], [Vec(782, 461), False], [Vec(796, 163), False]] 
levels[2].friction = player.standartFrict

levels[3] = Level()
levels[3].spawnpoint = Vec(10,10)
levels[3].goal = origin
levels[3].rotatelist = [ circles(origin, origin, -0.1, 300, 24),circles(origin, origin, -2.1, 100, 5),circles(origin, origin, 1.5, 200, 12)]
levels[3].linearlist= [[origin, 0.01, 200, 1, 10,0],[origin, 0.01, 200, 0, 10,0],[origin, -0.01, 200, 0, 10,0],[origin, -0.01, 200, 1, 10,0]]
levels[3].keylist = [[Vec(484, 303),False], [Vec(715, 493),False]]
levels[3].friction = player.standartFrict

levels[4] = Level()
levels[4].spawnpoint = Vec(425, 589)
levels[4].goal = origin
levels[4].rotatelist = [ circles(origin, addVec(origin,Vec(100,0)), -5, 100, 100),circles(origin, origin, -2.1, 100, 5),circles(origin, origin, 100, 350, 300)]
levels[4].linearlist= [[origin, -0.01, 200, 1, 10,0]]
levels[4].keylist = [[Vec(484, 303),False], [Vec(715, 493),False]]
levels[4].friction = player.standartFrict


levels[5] = Level()
levels[5].spawnpoint = Vec(40, WINDOW_SIZE[1]/2)
levels[5].goal = Vec(WINDOW_SIZE[0]-50, WINDOW_SIZE[1]/2)
levels[5].rotatelist = [circles(origin, origin, -2, WINDOW_SIZE[1]/2, 160)[30:]]
levels[5].linearlist= [
[Vec(WINDOW_SIZE[0]/7*1,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 40,0],
[Vec(WINDOW_SIZE[0]/7*2,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 40,1],
[Vec(WINDOW_SIZE[0]/7*3,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 40,2],
[Vec(WINDOW_SIZE[0]/7*4,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 40,3],
[Vec(WINDOW_SIZE[0]/7*5,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 40,4],
[Vec(WINDOW_SIZE[0]/7*6,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 40,5]
]
levels[5].keylist = [[Vec(934, 384),False], [Vec(491, 52),False],[Vec(491, WINDOW_SIZE[1]-52),False]]
levels[5].friction = player.standartFrict

levels[6] = Level()
levels[6].spawnpoint = Vec(425, 589)
levels[6].goal = origin
levels[6].rotatelist = [circles(Vec(959, 123),Vec(959, 123),-5,6,3),circles(Vec(317, 482),Vec(317, 482),-5,6,3)]
levels[6].linearlist= []
levels[6].keylist = [[Vec(300, 200),False], [Vec(600, 700),False]]
levels[6].friction = .98
levels[6].bounce = True

levels[7] = Level()
levels[7].spawnpoint = Vec(167, 746)
levels[7].goal = Vec(1200-167, 746)
levels[7].rotatelist = [circles(Vec(600, 246),Vec(600, 246),-1.9, 145, 100)[30:],circles(Vec(600, 246),Vec(600, 246),1.2, 20, 3)]
levels[7].linearlist= []
levels[7].keylist = []
levels[7].graphlist = [["posy = (","/19.1)**2-300",True],["posy = (","/20)**2",True]]#,["s = -(","/4)**2+5*2",False]]
levels[7].friction = .8
levels[7].wind = Vec(1,0)

levels[8] = Level()
levels[8].spawnpoint = Vec(167, WINDOW_SIZE[1]/2)
levels[8].goal = Vec(1200-167, WINDOW_SIZE[1]/2)
levels[8].rotatelist = [circles(Vec(600, WINDOW_SIZE[1]/2),Vec(600, WINDOW_SIZE[1]/2),-1.9, 145, 100)[7:]]
levels[8].linearlist= [
[Vec(WINDOW_SIZE[0]/4*1,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 10,0],
[Vec(WINDOW_SIZE[0]/4*2,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 10,1],
[Vec(WINDOW_SIZE[0]/4*3,WINDOW_SIZE[1]/2), -0.1, WINDOW_SIZE[1]/2, 0, 10,2]]
levels[8].keylist = []
levels[8].friction = player.standartFrict
levels[8].wind = Vec(0,0)
levels[8].movementType = 1

levels[9] = Level()
levels[9].spawnpoint = Vec(30, WINDOW_SIZE[1]/4*3)
levels[9].goal = Vec(1200-167, WINDOW_SIZE[1]/4*3)
levels[9].rotatelist = [circles(Vec(500,WINDOW_SIZE[1]/4*3),Vec(500,WINDOW_SIZE[1]/4*3-10),-1.9, 80, 25)[12:],circles(Vec(200,WINDOW_SIZE[1]/4*3),Vec(300,WINDOW_SIZE[1]/4*3),-1.9, 80, 25)[12:]]
levels[9].linearlist= []
levels[9].graphlist = [["posy = (","/5)**2+10",True],["posy = (","/30)**2-400",True]]#,["s = -(","/4)**2+5*2",False]]
levels[9].keylist = []
levels[9].friction = player.standartFrict
levels[9].wind = Vec(0,1.4)
levels[9].movementType = 2
levels[9].staticList = [
[Vec(WINDOW_SIZE[0]/4*3-110,WINDOW_SIZE[1]/4*3), 190, 0, 12],
[Vec(WINDOW_SIZE[0]/4*3-15,WINDOW_SIZE[1]/4*3-180), 100, 1, 6],
[Vec(2,WINDOW_SIZE[1]/4*3+15), WINDOW_SIZE[0], 0, 200]]

levels[10] = Level()
levels[10].spawnpoint = Vec(422, 321)
levels[10].goal = Vec(origin.x,origin.y-30)
levels[10].rotatelist = [circles(origin, origin,-1, 80, 25)[:2],line(Vec(-600,WINDOW_SIZE[1]/2), origin, WINDOW_SIZE[0]*2, 10, 0, .9)]
levels[10].linearlist = []
levels[10].keylist = [[Vec(300, 300),False], [Vec(WINDOW_SIZE[0]-300, WINDOW_SIZE[1]-300),False]]
levels[10].friction = .98
levels[10].bounce = True
levels[10].movementType = 3

levels[11] = Level()
levels[11].spawnpoint = Vec(WINDOW_SIZE[0]/2,130)
levels[11].goal = origin
levels[11].rotatelist = [circles(origin, origin, -.8, 200, 4),circles(origin, origin, .8, 100, 6),circles(origin, origin, -.8, 50, 6)]
levels[11].linearlist = [[origin, -0.01, 200, 1, 10,0],[origin, -0.01, 200, 0, 10,0]]
levels[11].keylist = [[Vec(WINDOW_SIZE[0]-200,WINDOW_SIZE[1]-200), False],[Vec(200,WINDOW_SIZE[1]-200), False],[Vec(WINDOW_SIZE[0]-200,200), False],[Vec(200,200), False]]
levels[11].friction = player.standartFrict

levels[12] = Level()
levels[12].spawnpoint = Vec(WINDOW_SIZE[0]/2-500 ,WINDOW_SIZE[1]/2)
levels[12].goal = origin
levels[12].rotatelist = []
levels[12].linearlist = []
levels[12].keylist = []         # ["""origin""", """size""", """speed""", """shift"""]
levels[12].graphlist = []
levels[12].friction = player.standartFrict

def loadLevel(lev):
    points = levels[lev].rotatelist
    spawn = levels[lev].spawnpoint
    goal = levels[lev].goal
    linearMotions = levels[lev].linearlist
    borders = levels[lev].borderlist
    keylist = levels[lev].keylist
    frict = levels[lev].friction
    bounce = levels[lev].bounce
    graphlist = levels[lev].graphlist
    wind = levels[lev].wind
    movementType = levels[lev].movementType
    staticLists = levels[lev].staticList
    return points, spawn, goal, linearMotions, keylist, frict, bounce, graphlist, wind, movementType, staticLists

running = True
time = 1
grounded = False
moving = directions()
movmentAllowed = True
particles = []
level = 1
time = 1
start = Vec(0,0)
end = Vec(0,0)
points, player.spawnpoint, goal, linearMotions, keylist, player.friction, bounce, graphlist, wind, movementType, staticLists = loadLevel(level)
player.position = player.spawnpoint
won = False

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
                if movementType == 2 and grounded:
                    player.velocity.y -= player.jumpforce
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
        if event.type == pygame.MOUSEBUTTONUP:
            if movementType == 3:
                print("end set")
                pVec(start)
                pVec(end)
                mx,my = pygame.mouse.get_pos()
                end = Vec(mx,my)
                direc = getDirectionVec(start, end)#.normalize()
                length = math.sqrt(direc.x**2+direc.y**2)
                if length >=1:
                    direc.x = direc.x/length
                    direc.y = direc.y/length
                    player.velocity = Vec(direc.x*24, direc.y*24)
                else:
                    player.velocity = Vec(0,0)
                start = Vec(0,0)
                end = Vec(0,0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if movementType == 3:
                print("start set")
                mx,my = pygame.mouse.get_pos()
                start = Vec(mx,my)
    if not won:
        if movmentAllowed:
            if movementType == 0:
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

                player.velocity.x += wind.x
                player.velocity.y += wind.y
                player.velocity.x *= player.friction
                player.velocity.y *= player.friction

                player.position = addVec(player.position, player.velocity)
                
                if bounce:
                    if player.position.x >= WINDOW_SIZE[0] or player.position.x <= 0:
                        player.velocity.x *= -1
                    if player.position.y >= WINDOW_SIZE[1] or player.position.y <= 0:
                        player.velocity.y *= -1
                player.position.x = clamp(player.position.x,0+player.radius, WINDOW_SIZE[0]-player.radius)
                player.position.y = clamp(player.position.y,0+player.radius, WINDOW_SIZE[1]-player.radius)
            
            elif movementType == 1:
                if moving.right:
                    player.velocity.x += player.speed
                    if player.isDashing:
                        player.velocity.x += player.speed/2
                if moving.left:
                    player.velocity.x -= player.speed
                    if player.isDashing:
                        player.velocity.x -= player.speed/2
                player.velocity.x += wind.x
                player.velocity.y += wind.y
                player.velocity.x *= player.friction
                player.velocity.y *= player.friction

                player.position = addVec(player.position, player.velocity)
                player.position.x = clamp(player.position.x,0+player.radius, WINDOW_SIZE[0]-player.radius)
                player.position.y = clamp(player.position.y,0+player.radius, WINDOW_SIZE[1]-player.radius)

            elif movementType == 2:
                if moving.right:
                    player.velocity.x += player.speed
                    if player.isDashing:
                        player.velocity.x += player.speed/2
                if moving.left:
                    player.velocity.x -= player.speed
                    if player.isDashing:
                        player.velocity.x -= player.speed/2


                player.velocity.x += wind.x
                player.velocity.y += wind.y
                player.velocity.x *= player.friction
                #player.velocity.y *= player.friction

                player.position = addVec(player.position, player.velocity)
                grounded = False
                player.position.x = clamp(player.position.x,0+player.radius, WINDOW_SIZE[0]-player.radius)

                valu = player.position.y
                if valu < 0+player.radius:
                    valu = 0+player.radius
                elif valu > WINDOW_SIZE[1]/4*3-player.radius:
                    valu = WINDOW_SIZE[1]/4*3-player.radius
                    grounded = True
                player.position.y = valu
                if grounded: 
                    player.velocity.y = 0

            elif movementType == 3:
                player.velocity.x += wind.x
                player.velocity.y += wind.y
                player.velocity.x *= player.friction
                player.velocity.y *= player.friction

                mx,my = pygame.mouse.get_pos()

                player.position = addVec(player.position, player.velocity)
                
                if bounce:
                    if player.position.x >= WINDOW_SIZE[0] or player.position.x <= 0:
                        player.velocity.x *= -1
                    if player.position.y >= WINDOW_SIZE[1] or player.position.y <= 0:
                        player.velocity.y *= -1
                player.position.x = clamp(player.position.x,0+player.radius, WINDOW_SIZE[0]-player.radius)
                player.position.y = clamp(player.position.y,0+player.radius, WINDOW_SIZE[1]-player.radius)
        #print(points)
        particles.append(Particle(player.position))
        for part in range(len(particles) -1, -1, -1):
            particles[part].update()
            par = Vec(particles[part].position.x,particles[part].position.y)
            dis = getDistance(par, player.position)*-1+255
            if particles[part].lifetime <= 0:
                particles.pop(part)
            if particles[part].type == 0 and player.isDashing:    
                pygame.gfxdraw.aacircle(display, int(particles[part].position.x),  int(particles[part].position.y), int(particles[part].size*2), (int(clamp(dis+30,0,255)),0,0))
                #pygame.draw.circle(display, (clamp(dis+30,0,255),0,0), (particles[part].position.x,particles[part].position.y), particles[part].size*2,particles[part].thick)
            else:
                pygame.gfxdraw.aacircle(display, int(particles[part].position.x),  int(particles[part].position.y), int(particles[part].size*2), particles[part].color)
                #pygame.draw.circle(display, particles[part].color, (particles[part].position.x,particles[part].position.y), particles[part].size*2,particles[part].thick)
        text = font.render(str(level), True, (200, 200, 200))
        display.blit(text,(WINDOW_SIZE[0] -10- (text.get_width()), 0))
        
        mx, my = pygame.mouse.get_pos()
        #print(mx,my)

        for graph in graphlist: #[["s = -(","/4)**2",True],["s = -(","/4)**2+5",False]]
            if graph[2]:
                for x in range(int(-(WINDOW_SIZE[0]/2)),int((WINDOW_SIZE[0]/2)),8):
                    posx = x
                    exec( str(graph[0])+str(posx)+str(graph[1]))
                    posx += WINDOW_SIZE[0]/2
                    posy += WINDOW_SIZE[1]/2
                    #pygame.draw.circle(display, (255,0,0), (posx, posy),10,1)
                    pygame.gfxdraw.aacircle(display, int(posx), int(posy), 10, (255,0,0))
                    if circleCol(Circle(player.position, player.radius), Circle(Vec(posx,posy), 10)):
                        player.position = player.spawnpoint
                        player.velocity = Vec(0,0)
                        l = Particle(origin, (40,40,40), 3,1)
                        l.lifetime = 500
                        particles.append(l)
                        for key in range(len(keylist)):
                            keylist[key][1] = False
            else:
                stats = graph[3] # ["""origin""", """size""", """speed""", """shift"""]
                shift = stats[3]
                speed = stats[2]
                size = stats[1]
                org = stats[0]
                posx = (math.sin(time*speed+shift)*size)
                exec( str(graph[0])+str(posx)+str(graph[1]))
                posy += org.y
                posx += org.x
                pygame.gfxdraw.aacircle(display, int(posx), int(posy), 10, (255,0,0))
                #pygame.draw.circle(display, (255,0,0), (posx, posy),10,1)
                if circleCol(Circle(player.position, player.radius), Circle(Vec(posx,posy), 10)):
                        player.position = player.spawnpoint
                        player.velocity = Vec(0,0)
                        l = Particle(origin, (40,40,40), 3,1)
                        l.lifetime = 500
                        particles.append(l)
                        for key in range(len(keylist)):
                            keylist[key][1] = False

        for slist in staticLists: # 0 = hochkant        [Vec(WINDOW_SIZE[0]/4*3-20,WINDOW_SIZE[1]/4*3), 20, 0, 5]
            for x in range(0, slist[1], int(slist[1]/slist[3])):

                if slist[2] == 0:
                    pygame.gfxdraw.aacircle(display, int(slist[0].x+x), int(slist[0].y), 10, (255,0,0))
                    #pygame.draw.circle(display, (255,0,0), (slist[0].x+x, slist[0].y),10,1)
                    
                    if circleCol(Circle(player.position, player.radius), Circle(Vec(slist[0].x+x, slist[0].y), 10)):
                        player.position = player.spawnpoint
                        player.velocity = Vec(0,0)
                        l = Particle(origin, (40,40,40), 3,1)
                        l.lifetime = 500
                        particles.append(l)
                        for key in range(len(keylist)):
                            keylist[key][1] = False 
                elif slist[2] == 1:
                    pygame.gfxdraw.aacircle(display, int(slist[0].x), int(slist[0].y+x), 10, (255,0,0))
                    #pygame.draw.circle(display, (255,0,0), (slist[0].x, slist[0].y+x),10,1)

                    if circleCol(Circle(player.position, player.radius), Circle(Vec(slist[0].x, slist[0].y+x), 10)):
                        player.position = player.spawnpoint
                        player.velocity = Vec(0,0)
                        l = Particle(origin, (40,40,40), 3,1)
                        l.lifetime = 500
                        particles.append(l)
                        for key in range(len(keylist)):
                            keylist[key][1] = False 

        for x in range(len(points)):
            #liste voll listen von 
            #verschiedene bullet typen (lv1:2)
            for y in range(len(points[x])):
                #bullet (punkt, originRot, speed)
                if circleCol(Circle(player.position, player.radius), Circle(points[x][y][0], 10)):
                    player.position = player.spawnpoint
                    player.velocity = Vec(0,0)
                    l = Particle(origin, (40,40,40), 3,1)
                    l.lifetime = 500
                    particles.append(l)
                    for key in range(len(keylist)):
                        keylist[key][1] = False 

                points[x][y][0] = rotate(points[x][y][1], points[x][y][0], points[x][y][2])
                pygame.gfxdraw.aacircle(display, int(points[x][y][0].x), int(points[x][y][0].y), 10, (255,0,0))
                #pygame.draw.circle(display, (255,0,0), (points[x][y][0].x, points[x][y][0].y),10,1)

        for key in range(len(keylist)):
            if circleCol(Circle(player.position, player.radius), Circle(keylist[key][0], 10)) and not keylist[key][1]:
                keylist[key][1] = True
                print("key collected")

            if keylist[key][1]:
                keycol = (50,20,50)
            else:
                keycol = (0,40,255)
            pygame.gfxdraw.aacircle(display, int(keylist[key][0].x), int(keylist[key][0].y), 10, keycol)
            #pygame.draw.circle(display, keycol, (keylist[key][0].x, keylist[key][0].y),10,1)
        
        for linear in range(len(linearMotions)):
            #lv1: 2
            if linearMotions[linear][3] == 0:
                coord = Vec(linearMotions[linear][0].x, linearMotions[linear][0].y + math.sin(time * linearMotions[linear][1]+linearMotions[linear][5])*linearMotions[linear][2])
            elif linearMotions[linear][3] == 1:
                coord = Vec( linearMotions[linear][0].x + math.sin(time * linearMotions[linear][1]+ linearMotions[linear][5])*linearMotions[linear][2], linearMotions[linear][0].y)
            pygame.gfxdraw.aacircle(display, int(coord.x), int(coord.y), int(linearMotions[linear][4]), (255,0,0))
            #pygame.draw.circle(display, (255,0,0), (coord.x, coord.y),linearMotions[linear][4],1)

            if circleCol(Circle(player.position, player.radius), Circle(coord, linearMotions[linear][4])):
                player.position = player.spawnpoint
                player.velocity = Vec(0,0)
                l = Particle(origin, (40,40,40), 3,1)
                l.lifetime = 500
                particles.append(l)
                for key in range(len(keylist)):
                    keylist[key][1] = False 

        if movementType == 3:
            pygame.gfxdraw.aacircle(display, int(start.x), int(start.y), 2, (255,255,255))
            #pygame.draw.circle(display, (255,255,255), (start.x, start.y),2,2)
            if start != Vec(0,0):
                pygame.gfxdraw.aacircle(display, int(mx), int(my), 2, (255,255,255))
                #pygame.draw.circle(display, (255,255,255), (mx, my),2,2)
        
        pygame.gfxdraw.aacircle(display, int(goal.x), int(goal.y), 10, (100,255,100))
        #pygame.draw.circle(display, (100,255,100), (goal.x, goal.y),10,1)
        pygame.gfxdraw.aacircle(display, int(player.position.x), int(player.position.y), int(player.radius), player.color)
        #pygame.draw.circle(display, player.color, (player.position.x, player.position.y),player.radius,1)

        #goal collision
        if circleCol(Circle(player.position, player.radius), Circle(goal, 10)):
            allkeys = True
            for key in keylist:
                if key[1] == False:
                    allkeys = False
            if allkeys:
                level +=1
                if level > len(levels):
                    level = len(levels)
                    print("win")
                    won = True
                points, player.spawnpoint, goal, linearMotions, keylist, player.friction, bounce, graphlist, wind, movementType, staticLists = loadLevel(level)
                player.velocity = Vec(0,0)
                player.position = player.spawnpoint
    else:
        print(125+math.sin(time*0.01)*125)
        text = font.render(str("victory!"), True, (125+math.sin(time*0.04+200)*125, 125+math.sin(time*0.02+100)*125, 125+math.sin(time*0.07+50)*125))
        display.blit(text,(WINDOW_SIZE[0]/2 - (text.get_width()/2), WINDOW_SIZE[1]/2 - (text.get_height()/2)))

        text = fontSmol.render(str("thanks for playing my little game!"), True, (200, 200, 200))
        text2 = fontSmol.render(str("Made by Magnus K."), True, (200, 200, 200))
        display.blit(text,(WINDOW_SIZE[0]/2 - (text.get_width()/2), WINDOW_SIZE[1]/2 + 200 - (text.get_height()/2)))
        display.blit(text2,(WINDOW_SIZE[0]/2 - (text.get_width()/2), WINDOW_SIZE[1]/2 + 230 - (text.get_height()/2)))
        for x in getVertsInCircle(origin, 50,150,time):
            pygame.gfxdraw.aacircle(display, int(x.x), int(x.y), 10, (125+math.sin(time*0.045+200)*125, 125+math.sin(time*0.025+100)*125, 125+math.sin(time*0.075+50)*125))
            #pygame.draw.circle(display, (125+math.sin(time*0.045+200)*125, 125+math.sin(time*0.025+100)*125, 125+math.sin(time*0.075+50)*125), (x.x,x.y), 10, 3)
    pygame.display.flip()
    display.fill((5,9,5))
    time+=1
    deltatime = clock.tick(60)
pygame.quit()