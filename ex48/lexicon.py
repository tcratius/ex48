class Lexicon(object):

    def __init__(self):
        self.sentence = []
        # List of directions
        self.dl = ['north', 'south', 'east', 'west', 'up', 'down', 'left', 'right' ]
        # List of verbs
        self.vl = ['go', 'kill', 'eat', 'search', 'stop', 'shoot', 'attack']
        # List of stop words
        self.sl = ['the', 'in', 'of', 'from', 'at', 'it']
        # List of nouns
        self.nl = ['door', 'cabinet', 'bear', 'princess']

    #@staticmethod
    def scan(self, value):
        # take sentence, make it lower case and split it
        self.sentence = value.lower().split()
        # sets up a place to hold the list of words scanned in from lexicon_tests.py
        self.list = []
        for word in self.sentence:
            if self.dl.count(word) != 0:
                self.list.append(('direction', word))
            elif self.vl.count(word) != 0:
                self.list.append(('verb', word))
            elif self.sl.count(word) != 0:
                self.list.append(('stop', word))
            elif self.nl.count(word) != 0:
                self.list.append(('noun', word))
            elif test_numbers(word) != None:
                self.list.append(('number', number_check))
            else:
                self.list.append(('error', word))
        return self.list

# if returns None than is a digit
def test_numbers(word):
    try:
        return int(word)
    except ValueError:
        return None

def number_check2(word):
    if word.isdigit():
        return int(word)
    else:
        return None
