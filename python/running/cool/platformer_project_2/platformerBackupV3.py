import pygame, sys, os, random
from engine import *

clock = pygame.time.Clock()

from pygame.locals import *
success, failures = pygame.init() # initiates pygame
print(f'Success: {success}, failures: {failures}')

pygame.display.set_caption('Pygame Platformer')

WINDOW_SIZE = (600,400)
monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]

screen = pygame.display.set_mode(WINDOW_SIZE,pygame.RESIZABLE) # initiate the window

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

moving_right = False
moving_left = Falseair_timer = 0

vertical_momentum = 0
jumpHeight = 4.5

true_scroll = [-1000,1000]

def load_map(path):
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
        #print(list(row))

    return game_map

global animation_frames
animation_frames = {}

maxJumps = 2
jumps = 0

def load_animation(path,frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 0
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        # player_animations/idle/idle_0.png
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255,255,255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame
        

animation_database = {}

animation_database['run'] = load_animation('player_animations/run',[7,7])
animation_database['idle'] = load_animation('player_animations/idle',[7,7,40])

game_map = load_map('map')

grass_img = pygame.image.load('grass.png')
dirt_img = pygame.image.load('dirt.png')

player_action = 'idle'
player_frame = 0
player_flip = False
spawn = [100, 100]
y = 0
for layer in game_map:
    x = 0
    for tile in layer:
        if tile == 'S':
            spawn[0]= x*16
            spawn[1]= y*16
        
        x += 1
    y += 1
        
print(spawn)
player_rect = pygame.Rect(spawn[0],spawn[1],5,13) #pygame.Rect(100,100,5,13)

background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types
particles = []
air_timer = 0
collisions = {'top':False,'bottom':False,'right':False,'left':False}
while True: # game loop
    display.fill((146,244,255)) # clear screen by filling it with blue

    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
    #print(true_scroll)
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    pygame.draw.rect(display,(7,80,75),pygame.Rect(0,120,300,80))
    for background_object in background_objects:
        obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
        if background_object[0] == 0.5:
            pygame.draw.rect(display,(14,222,150),obj_rect)
        else:
            pygame.draw.rect(display,(9,91,85),obj_rect)

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
            if tile != '0' and tile != 'S':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1

    player_movement = [0,0] 
    if moving_right == True:
        player_movement[0] += 2
    if moving_left == True:
        player_movement[0] -= 2
    if not collisions['right'] and not collisions['left']:
        player_movement[1] += vertical_momentum
    else: 
        player_movement[1] += vertical_momentum*.7
        if vertical_momentum > 0:
            for x in range(0,5):
                posit = (player_rect.x + 5 - scroll[0] + random.randint(-3,3), player_rect.y + (13/2) - scroll[1] + random.randint(-1,1))
                pt = Particle(posit, random.randint(0,2), scroll, (180,180,180))
                particles.append(pt)


    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3

    if player_movement[0] == 0:
        player_action,player_frame = change_action(player_action,player_frame,'idle')
    if player_movement[0] > 0:
        player_flip = False
        player_action,player_frame = change_action(player_action,player_frame,'run')
    if player_movement[0] < 0:
        player_flip = True
        player_action,player_frame = change_action(player_action,player_frame,'run')
    if air_timer > 10:
        player_action,player_frame = change_action(player_action,player_frame,'idle')

    player_rect,collisions = move(player_rect,player_movement,tile_rects)

    if collisions['bottom'] == True:
        air_timer = 0
        vertical_momentum = 0
        jumps = 0
    else:
        air_timer += 1
    if collisions['top']:
        vertical_momentum = 0
        for x in range(0,10):
            #print(player_rect.x)
            posit = (player_rect.x - scroll[0] + random.randint(-3,3), player_rect.y - scroll[1] + random.randint(-2,2))
            particle = Particle(posit, random.randint(0,3), scroll, (230,230,230))
            particles.append(particle)

    #print(particles)
    player_frame += 1
    if player_frame >= len(animation_database[player_action]):
        player_frame = 0  
    player_img_id = animation_database[player_action][player_frame]
    player_img = animation_frames[player_img_id]
    display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))


    for par in particles:   ### Rendering of the particles
        par.Update()
        renderpos = (int(par.pos[0]) - ((par.scroll[0]-scroll[0]) * -1),  int(par.pos[1])- ((par.scroll[1]-scroll[1])*-1))
        pygame.draw.circle(display, par.color, renderpos, par.lifetime * 1, 0)
        #print(par.pos[0], par.pos[1], renderpos)

    for event in pygame.event.get(): # event loop
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_d:
                moving_right = True
            if event.key == K_a:
                moving_left = True
            if event.key == K_SPACE:
                if air_timer < 6 or jumps < maxJumps or collisions['left'] or collisions['right']:
                    if collisions['right']:
                        pass
                    jumps += 1
                    vertical_momentum = -jumpHeight
                    
                    for x in range(0,10):
                        posit = (player_rect.x + 5 - scroll[0] + random.randint(-3,3), player_rect.y + 13 - scroll[1] + random.randint(-3,3))
                        if jumps == 1: pt = Particle(posit, random.randint(0,4), scroll, (148,223,180))
                        else: pt = Particle(posit, random.randint(0,4), scroll, (255,255,255))
                        particles.append(pt)
        
        print(jumps)
        if event.type == KEYUP:
            if event.key == K_d:
                moving_right = False
            if event.key == K_a:
                moving_left = False

    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(60)
