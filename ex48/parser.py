class ParserError(Exception):
    pass


class Sentence(object):
    # need a object to put results in i.e. results
    def __init__(self, subj, verb, obj):
        # remember we take ('noun', 'princess') tuples and convert
        self.subj = subj(1)
        self.verb = verb(1)
        self.obj = obj(1)


    def peek(word_list):
        if word_list:
            word = word_list[0]
            return word[0]
        else:
            return None

    def match(word_list, expecting):
        if word_list:
            word = word_list.pop(0)

            if word[0] == expecting:
                return word
            else:
                return None
        else:
            return None

    def skip(word_list, word_type):
        while peek(word_list) == word_type:
            match(word_list, word_type)



    def parse_verb(word_list):
        skip(word_list, 'stop')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next. Received %s ") % word_list


    def parse_object(word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            return match(self.word_list, 'noun')
        elif next_word == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParseError("Expected a noun or direction next. Received %s ") % wordlist

    def parse_subject(word_list, subject):
        self.verb = parse_verb(word_list)
        self.object = parse_object(word_list)

        return Sentence(subject, verb, object)


    def parse_sentence(self, word_list):
        skip(word_list, 'stop')
        next_word = peek(word_list)

        if next_word == 'noun':
            subj = match(word_list, 'noun')
            return parse_subject(word_list, subj)
        elif next_word == 'verb':
            # assume the subject is the player then
            return parse_subject(word_list, ('noun', 'player'))
        else:
            raise ParserError("Must start with subject, object, or verb not: %s.") % word_list
