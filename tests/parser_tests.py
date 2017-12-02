import pytest
from ex48.parser import Sentence


@pytest.fixture()
def test_sentence():
    sentence = Sentence.parse_sentence([("noun","player"),("verb", "go"),("noun", "bear")])
    return sentence

@classmethod
def test_peek():
    result = test_sentence()
    assert Sentence.peek(result) != None


def test_match():
    pass

def test_skip():
    pass

def test_parse_verb():
    pass

def test_parse_object():
    pass

def test_parse_subject():
    pass

def test_parse_sentence():
    pass
