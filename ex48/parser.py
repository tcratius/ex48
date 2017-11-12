class ParserError(Exception):
    pass


class Sentence(object):
    # need a object to put results in i.e. results
    def __init__(self, subj, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert

        self.subj = subj(1)
        self.verb = verb(1)
        self.obj = obj(1)
        self.word = []
        self.word_list = []

    def peek(self, word_list):
        if self.word_list:
            self.word = self.word_list[0]
            return self.word[0]
        else:
            return None

    def match(self, word_list, expecting):
        if self.word_list:
            self.word = self.word_list.pop(0)

            if self.word[0] == self.expecting:
                return self.word
            else:
                return None
        else:
            return None

    def skip(self, word_list, word_type):
        while peek(self.word_list) == self.word_type:
            match(self.word_list, self.word_type)



    def parse_verb(self, word_list):
        skip(self.word_list, 'stop')

        if peek(self.word_list) == 'verb':
            return match(self.word_list, 'verb')
        else:
            raise ParserError("Expected a verb next.")


    def parse_object(self, word_list):
        skip(self.word_list, 'stop')
        self.next_word = peek(self.word_list)

        if self.next_word == 'noun':
            return match(self.word_list, 'noun')
        elif next_word == 'direction':
            return match(self.word_list, 'direction')
        else:
            raise ParseError("Expected a noun or direction next.")



    def parse_subject(self, word_list):
        skip(self.word_list, 'stop')
        self.next_word = peek(self.word_list)

        if self.next_word == 'noun':
            return match(self.word_list, 'noun')
        elif self.next_word == 'verb':
            return ('noun', 'player')
        else:
            raise ParserError("Expected a verb next.")

    def parse_sentence(self, word_list):
        self.subject = parse_subject(self.word_list)
        self.verb = parse_verb(self.word_list)
        self.object = parse_object(self.word_list)

        return Sentence(self.subject, self.verb, self.object)
