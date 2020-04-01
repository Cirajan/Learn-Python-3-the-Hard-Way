import creatures



class Room(object):

    def __init__(self, name):
        self.name = name
        self.monster = creatures.Monster.generateMonster()
        self.paths = {}

    def enter(self, player):
        print(f'You are in room {self.name}.')

        if self.monster.isDead():
            print(f'You see a dead {self.monster.getName()}.')
        else:
            print(f'You see a {self.monster.getName()}.')
            while not (self.monster.isDead()):
                    self.monster.reduceHealth(player.getDamage())
                    print(f'You hit the {self.monster.getName()} for {player.getDamage()}.')
            print(self.monster.getName() + ' is dead.')


    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)

    def getMonster(self):
        return self.monster
