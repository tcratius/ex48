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
        self.nl = ['door', 'cabinet']

    #@staticmethod
    def scan(self, value):
        # take sentence, make it lower case and split it
        self.sentence = value.lower().split()
        # sets up a place to hold the list of words scanned in from lexicon_tests.py
        self.list = []

        for word in self.sentence:
            if self.dl.count(word) != 0:
                self.list.append(('direction', word))
            if self.vl.count(word) != 0:
                self.list.append(('verb', word))
            if self.sl.count(word) != 0:
                self.list.append(('noun', word))

        return self.list


"""
    #def test_numbers(self):


    # Tests for numbers, if number than returns none which can be used to tell
    # user that the input is not valid rawinput() to continue playing game
    def convert_number(s):
        try:
            return int(s)
        except ValueError:
            return None


d = Lexicon()
d.scan("north south east")
"""
