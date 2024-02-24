import pygame
import random

class rect: # rect object
    def __init__(self, position=(0,0), size=(50,50)):
        self.position = pygame.Vector2(position)
        self.size = pygame.Vector2(size)

class rectLayout: # store data
    def __init__(self, layoutSize):
        self.rects =  {"base":rect((0,0), layoutSize)}

    def cutRight(self, rectName, length, newName):
        if length < self.rects[rectName].size.x or length <= 0:
            newRect = rect()
            newRect.size.y = self.rects[rectName].size.y
            newRect.size.x = length

            newRect.position.x = self.rects[rectName].position.x+self.rects[rectName].size.x-length
            newRect.position.y = self.rects[rectName].position.y

            self.rects[rectName].size.x -= length
            self.rects[newName] = newRect
        else: print("invalid length")

    def cutLeft(self, rectName, length, newName):
        if length < self.rects[rectName].size.x or length <= 0:
            newRect = rect()
            newRect.size.y = self.rects[rectName].size.y
            newRect.size.x = length

            newRect.position.x = self.rects[rectName].position.x
            newRect.position.y = self.rects[rectName].position.y

            self.rects[rectName].position.x += length
            self.rects[rectName].size.x -= length
            self.rects[newName] = newRect
        else: print("invalid length")

    def cutBottom(self, rectName, length, newName):
        if length < self.rects[rectName].size.y or length <= 0:
            newRect = rect()
            newRect.size.y = length
            newRect.size.x = self.rects[rectName].size.x

            newRect.position.x = self.rects[rectName].position.x
            newRect.position.y = self.rects[rectName].position.y + self.rects[rectName].size.y - length

            self.rects[rectName].size.y -= length
            self.rects[newName] = newRect
        else: print("invalid length")

    def cutTop(self, rectName, length, newName):
        if length < self.rects[rectName].size.y or length <= 0:
            newRect = rect()
            newRect.size.y = length
            newRect.size.x = self.rects[rectName].size.x

            newRect.position.x = self.rects[rectName].position.x
            newRect.position.y = self.rects[rectName].position.y

            self.rects[rectName].position.y += length
            self.rects[rectName].size.y -= length
            self.rects[newName] = newRect
        else: print("invalid length")

class rectcutRenderer: # render with pygame
    def __init__(self):
        pass

    def render(self, display, rectLayout):
        for rect in rectLayout.rects:
            rectData = rectLayout.rects[rect]
            color = (min(255, rectData.size.x),min(255, rectData.size.y),min(255, rectData.size.x*.35))
            pygame.draw.rect(display, color, pygame.Rect(rectData.position.x, rectData.position.y, rectData.size.x, rectData.size.y))


class rectcutManager: # render it
    def __init__(self, layoutSize):
        self.rectLayout = rectLayout(layoutSize)
        self.renderer = rectcutRenderer()

    def render(self, display):
        self.renderer.render(display, self.rectLayout)
