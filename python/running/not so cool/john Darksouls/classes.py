from UEngine02v import *

#class Armor:
 #   def __init__(self) -> None:
  #      self.head = itemZERO;
   #     self.chest = itemZERO;
    #    self.legs = itemZERO;
     #   self.hands = itemZERO;

class john:
    def __init__(self):
        self.items = {}
        
        self.HP = 10;
        self.maxHP = 10;

        self.stamina = 10;
        self.maxStamina = 10;
#        self.armor = ArmorZERO;

        self.friction = 0.9;
        self.speed = 4,
        self.velocity = VecZERO;
        self.position = VecZERO;


class enemy:
    def __init__(self, position = VecZERO):
        self.position = position
        self.targetPlayer = False


class map:
    def __init__(self):
        pass

