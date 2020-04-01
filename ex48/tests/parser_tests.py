from nose.tools import *
from ex48.parser import *


def test_direction_object():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal((x.verb, x.object), ('run', 'north'))
    print(x.verb, x.object)

def test_no_subject():
    x = parse_sentence([('stop', 'from'), ('stop', 'to'), ('verb', 'hit'), ('noun', 'bear')])
    assert_equal((x.subject, x.verb, x.object), ('player', 'hit', 'bear'))

def test_noun_object():
    x = parse_sentence([('noun', 'cat'), ('verb', 'hit'), ('noun', 'dog')])
    assert_equal((x.subject, x.verb, x.object), ('cat', 'hit', 'dog'))

def test_double_verb():

    assert_raises(ParserError, parse_sentence, [('verb', 'run'), ('verb', 'go'), ('direction', 'north')])

    try:
        x = parse_sentence([('verb', 'run'), ('verb', 'go'), ('direction', 'north')])

    except Exception as e:
        print(e)
