import pytest

from ex48.parser import *

@pytest.fixture()
def test_sentence():
    sentence = Sentence(("noun","player"),("verb", "go"),("noun", "bear"))
    assert_equal(sentence.subj, 'player')
    assert_equal(sentence.verb, 'go')
    assert_equal(sentence.obj, 'north')

def test_peek():
    pass

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
