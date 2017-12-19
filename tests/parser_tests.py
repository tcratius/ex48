
import pytest
from ex48 import parser
from ex48.parser import Sentence

# test parse_sentence
@pytest.fixture()
def test_sentence():
    sentence = Sentence.parse_sentence([("noun","player"),("verb", "go"),("noun", "bear")])
    return sentence

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
    word_list_one = ([("stop", "at")])
    word_list_two = ([("stop", "the")])
    word_type = "stop"
    assert skip(word_list_one, word_type) != None
    assert skip(word_list_two, word_type) != None

@classmethod
def test_parse_verb():
    word_list_one = ([("verb", "hit")])
    word_list_two = ([("verb", "run")])
    word_list_three = ([("stop", "in")])
    word_list_four = ([("number", "1234")])
    assert parse_verb(word_list_one) != None
    assert parse_verb(word_list_two) != None
    assert parse_verb(word_list_three) != None
    with pytest.raises(ParserError) as excinfo:
        parse_verb(word_list_four)
    assert str(excinfo.value) == "Expected a verb next. Received number "

@classmethod
def test_parse_object():
    word_list_one = ([("direction", "north")])
    word_list_two = ([("noun", "bear")])
    word_list_three = ([("stop", "on")])
    word_list_four = ([("error", "four21")])
    assert parse_object(word_list_one) != None
    assert parse_object(word_list_two) != None
    assert parse_object(word_list_three) != None
    with pytest.raises(ParserError) as excinfo:
        parse_object(word_list_four)
    assert str(excinfo.value) == "Expected a noun or direction next. Received error "

@classmethod
def test_parse_subject():
    word_list_one = ([("noun", "conrad")])
    # (player) hits conrad
    word_list_two = ([("verb", "hits")])
    word_list_three = ([("error", "run1")])
    with pytest.raises(ParserError) as excinfo:
        parse_subject(word_list_three)
    assert str(excinfo.value) == "Expected a verb next."
