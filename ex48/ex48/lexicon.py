lexicon =  [('direction', 'north'),
            ('direction', 'south'),
            ('direction', 'east'),
            ('direction', 'west'),
            ('direction', 'up'),
            ('direction', 'down'),
            ('direction', 'back'),
            ('verb', 'go'),
            ('verb', 'stop'),
            ('verb', 'kill'),
            ('verb', 'eat'),
            ('stop', 'the'),
            ('stop', 'in'),
            ('stop', 'of'),
            ('stop', 'from'),
            ('stop', 'at'),
            ('stop', 'it'),
            ('noun', 'door'),
            ('noun', 'bear'),
            ('noun', 'princess'),
            ('noun', 'cabinet')]



def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(input):
    words = input.split()
    word_list = []
    for w in words:

        result = [l for l in lexicon if l[1] == w]
        if result:
            word_list.append(result[0])

        elif convert_number(w) is not None:
            word_list.append(('number', convert_number(w)))

        else:
            word_list.append(('error', w))

    return word_list
