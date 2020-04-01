from ex45Game.rooms import *




class Map(object):

    __num_rows = 3
    __num_cols = 3
    __map = {}
    __room_linkage = {
                       'A1' : {'n':'', 's':'B1', 'e':'A2', 'w':''},
                       'A2' : {'n':'', 's':'B2', 'e':'A3', 'w':'A1'},
                       'A3' : {'n':'', 's':'B3', 'e':'', 'w':'A2'},
                       'B1' : {'n':'A1', 's':'C1', 'e':'B2', 'w':''},
                       'B2' : {'n':'A2', 's':'C2', 'e':'B3', 'w':'B1'},
                       'B3' : {'n':'A3', 's':'C3', 'e':'', 'w':'B2'},
                       'C1' : {'n':'B1', 's':'', 'e':'C2', 'w':''},
                       'C2' : {'n':'B2', 's':'', 'e':'C3', 'w':'C1'},
                       'C3' : {'n':'B3', 's':'', 'e':'', 'w':'C2'}
                      }
    __at_start = True
    __cur_room = 'A1'

    def __init__(self):
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                room_name = chr(65 + r) + str(c + 1)
                self.__map[room_name] = ex45Game.rooms.Room(room_name)


    def getNextRoom(self):
        if (self.__at_start):
            self.__at_start = False
            return self.__map[self.__cur_room]
        else:
            while (True):
                direction = input('Enter a direction n, s, e, w: ')
                while direction.lower() not in ['n', 's', 'e', 'w']:
                        direction = input('Invalid direction try again: ')

                if  self.__room_linkage[self.__cur_room][direction] != '':
                    break
                print("Can't go that way from here sry.")

            self.__cur_room = self.__room_linkage[self.__cur_room][direction]
            return self.__map[self.__cur_room]







class Engine(object):

    def __init__(self):
        self.__map = Map()
        self.__player = ex45Game.creatures.Player(input('Enter character name: '))

    def play(self):
        print('Game started')
        print('Try to get to room C3.')
        room = self.__map.getNextRoom()
        while room.name != 'C3':
            room.enter(self.__player)
            room = self.__map.getNextRoom()
        print('Map cleared. Game finished')


e = Engine()
e.play()
