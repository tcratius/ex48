
import pytest
from ex48 import parser
from ex48.parser import Sentence

@pytest.fixture()
def test_sentence():
    sentence = Sentence.parse_sentence([("noun","player"),("verb", "go"),("noun", "bear")])
    return sentence
@pytest.fixture()
def test_skip_word():
    skip_word_one[0], skip_word_two[1] = ([("stop", "at")]
    return skip_word_one, skip_word_two

@classmethod
def test_peek():
    result = test_sentence()
    assert Sentence.peek(result) != None

@classmethod
def test_match():
    result = test_setence()
    expecting = "noun"
    assert Sentence.match(result, expecting) != None

@classmethod
def test_skip():
    result1, result2  = test_skip_word()
    assert Sentence.skip(result1, result2) != None



def test_parse_verb():
    pass

def test_parse_object():
    pass

def test_parse_subject():
    pass

def test_parse_sentence():
    pass
