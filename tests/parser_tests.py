
import pytest
from ex48 import parser
from ex48.parser import Sentence


def test_sentence():
    sentence = Sentence(("noun","player"),("verb", "go"), ("direction", "north"))
    assert_equal(sentence('noun', 'player'))
    assert_equal(sentence('verb', 'go'))
    assert_equal(sentence('direction', 'north'))

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
