import rooms
import creatures




class Map(object):

    __num_rows = 3
    __num_cols = 3

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

    __room_linkage1 = {
                       'A1' : {'s':'B1', 'e':'A2'},
                       'A2' : {'s':'B2', 'e':'A3', 'w':'A1'},
                       'A3' : {'s':'B3', 'w':'A2'},
                       'B1' : {'n':'A1', 's':'C1', 'e':'B2'},
                       'B2' : {'n':'A2', 's':'C2', 'e':'B3', 'w':'B1'},
                       'B3' : {'n':'A3', 's':'C3', 'w':'B2'},
                       'C1' : {'n':'B1', 'e':'C2'},
                       'C2' : {'n':'B2', 'e':'C3', 'w':'C1'},
                       'C3' : {'n':'B3', 'w':'C2'}
                      }

    __at_start = True
    __cur_room = None

    def __init__(self):
        self.room_set = {}
        for r in range(self.__num_rows):
            for c in range(self.__num_cols):
                room_name = chr(65 + r) + str(c + 1)
                self.room_set[room_name] = rooms.Room(room_name)

        for r, l in self.__room_linkage1.items():
            for k, i in l.items():
                l[k] = self.room_set[i]

        for k in self.room_set:
            self.room_set[k].add_paths(self.__room_linkage1[k])




        self.__cur_room = self.room_set['A1']
        # print(self.__cur_room.paths)





    def getNextRoom(self):
        if (self.__at_start):
            self.__at_start = False
            return self.__cur_room
        else:
            while (True):
                direction = input('Enter a direction n, s, e, w: ')
                while direction.lower() not in ['n', 's', 'e', 'w']:
                        direction = input('Invalid direction try again: ')

                if  self.__cur_room.go(direction) != None:
                    break
                print("Can't go that way from here sry.")

            self.__cur_room = self.__cur_room.go(direction)
            return self.__cur_room







class Engine(object):

    def __init__(self):
        self.__map = Map()
        self.__player = creatures.Player(input('Enter character name: '))

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
