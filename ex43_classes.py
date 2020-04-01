class Scene(object):

    def enter(self):
        pass



class Engine(object):



    def __init__(self, scene_map):

        self.m_map = scene_map

    def play(self):


        self.scene = self.m_map.opening_scene()

        while True:

            next_scene_name = self.scene.enter()

            if next_scene_name == None:
                break

            else:
                self.scene = self.m_map.next_scene(next_scene_name)



class Death(Scene):

    def enter(self):
        print("You died.")
        input("Hit return.")
        return None



class CentralCorridor(Scene):

    def enter(self):
        print("You are in the Central Corridor")
        input("Hit return.")
        return 'laser_weapon_armory'


class LaserWeaponArmory(Scene):

    def enter(self):
        print("You are in the Laser Weapon Armory.")
        input("Hit return.")
        return 'the_bridge'


class TheBridge(Scene):

    def enter(self):
        print("You are in the Bridge.")
        input("Hit return.")
        return 'escape_pod'


class EscapePod(Scene):

    def enter(self):
        print("You are in the Escape Pod.")
        input("Hit return.")
        return None


class Map(object):

    m_death = Death()
    m_central_corridor = CentralCorridor()
    m_laser_weapon_armory = LaserWeaponArmory()
    m_the_bridge = TheBridge()
    m_escape_pod = EscapePod()

    m_map = {'death': m_death, 'central_corridor': m_central_corridor,
            'laser_weapon_armory': m_laser_weapon_armory,
            'the_bridge': m_the_bridge,
            'escape_pod': m_escape_pod}



    def __init__(self, start_scene):

        self.m_opening_scene = start_scene

    def next_scene(self, scene_name):

        return Map.m_map[scene_name]

    def opening_scene(self):

        return Map.m_map[self.m_opening_scene]



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
