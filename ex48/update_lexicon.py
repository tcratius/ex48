import pickle
# update pickle files holding dictionary values to be in lexicon
def save_lexicon():
    lexicon = {'north': 'direction',
              'south': 'direction',
              'east': 'direction',
              'west': 'direction',
              'down':'direction',
              'up':'direction',
              'left':'direction',
              'right':'direction',
              'go': 'verb',
              'kill': 'verb',
              'eat': 'verb',
              'the': 'stop',
              'in': 'stop',
              'of': 'stop',
              'door':'noun',
              'bear': 'noun',
              'princess': 'noun',
              'dollar': 'money',
              'pound': 'money',
              'kronor': 'money',
              'miles': 'distance',
              'km': 'distance',
              'meter': 'distance',
              }
    pickle.dump(lexicon, open("lexicon_words.p", "wb"))
