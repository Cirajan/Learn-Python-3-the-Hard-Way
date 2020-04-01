from random import randint




class Creature(object):

    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    def getDamage(self):
        return self.__damage

    def reduceHealth(self, amount):
        self.__health -= amount

    def isDead(self):
        return (self.__health <= 0)




class Player(Creature):

    def __init__(self, name, health = 20, damage = 4):
        super(Player, self).__init__(name, health, damage)


    





class Monster(Creature):

    __monsterData = [
                    {'name' : 'Goblin', 'health' : 6, 'damage' : 2},
                    {'name' : 'Orc', 'health' : 8, 'damage' : 3},
                    {'name' : 'Slime', 'health' : 5, 'damage' : 2}
                    ]

    def __init__(self, type):
        super(Monster, self).__init__(Monster.__monsterData[type]['name'],
                                      Monster.__monsterData[type]['health'],
                                      Monster.__monsterData[type]['damage']
                                      )

    @classmethod
    def generateMonster(cls):
        m = cls(randint(0, len(Monster.__monsterData) - 1))
        return m
