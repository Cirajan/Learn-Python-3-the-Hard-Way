from nose.tools import *
from ex47Game import text_game

def setup():
    print("SETUP!")


def teardown():
    print("TEAR DOWN!")


def test_game():
    # m = text_game.Map()

    e = text_game.Engine()
    e.play()

    print('test entered')
