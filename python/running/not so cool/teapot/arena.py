import random
import copy
from settingsAndGeneralFunctions import *

class Arena:
    def __init__(self):
        self.enemys = []
        self.enemyQueue = []

        self.bullets = []
        self.spawnSpeed = 250
        self.minValue = 15
        self.round = 1
        self.roundTimer = self.round * 80
    
    def updateEnemys(self):
        pass

    def handleEnemyCount(self, allEnemys, gameWindowSize):
        totalValue = 0
        for enemy in list(self.enemys) + list(self.enemyQueue):
            totalValue += enemy.value
        if totalValue < self.minValue:

            newEnemy = random.choice(copy.deepcopy(allEnemys))
            newEnemy.position = [random.randint(0,gameWindowSize[0]),random.randint(0,gameWindowSize[1])]
            newEnemy.targetOffset = [random.randint(-30,30), random.randint(-30,30)]
            newEnemy.offsetVecLength = getLength(newEnemy.targetOffset)

            self.enemyQueue.append(newEnemy)

        if random.randint(0, self.spawnSpeed) == 5 and len(self.enemyQueue):
            self.enemys.append(self.enemyQueue.pop(0))
            print("shifted")