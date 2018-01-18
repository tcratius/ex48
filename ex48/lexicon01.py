import pickle

# open file and populate dictionary with lexicon values
def load_lexicon():
    lexicon = pickle.load(open("lexicon_words.p", "r"))
    return lexicon

lexicon = load_lexicon()

def scan(usr_input):
    result = []
    usr_input = usr_input.split()
    for word in usr_input:
        wordtype = lexicon.get(word, 'error')
        pair = (wordtype, word)
        print pair
        if word in lexicon:
            result.append(pair)
        elif word not in lexicon:
            number = convert_number(word)
            if number:
                pair = ('number', number)
            elif word not in lexicon and not number:
                pair = (wordtype, word)
    print result
    return result

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

if __name__ == '__main__':
    sentence = raw_input("Please enter your choice: -> ")
    sentence = sentence.lower()
    scan(sentence)
