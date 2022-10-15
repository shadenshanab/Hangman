import pytest
from game.hangman import *

def test_hangman_length():
    actual = len(HANGMAN)
    expected = 7
    assert actual == expected

def test_option_length(): # options must be 5 letters or over
    word = options[0]
    actual = len(word)>=5
    expected = True
    assert actual == expected

    word = options[1]
    actual = len(word)>=5
    expected = True
    assert actual == expected

    word = options[2]
    actual = len(word)>=5
    expected = True
    assert actual == expected

    word = options[4]
    actual = len(word)>=5
    expected = True
    assert actual == expected

    word = options[5]
    actual = len(word)>=5
    expected = True
    assert actual == expected


def test_invalid_letter(): #input must be one letter
    input_ = 'C'
    actual = (len(input_) >1 and input_.isalpha) and (input_.isdigit)
    expected = False
    assert actual == expected

def test_failed_attempts(): #user must have 7 attempts only
    failed_attempts = 8
    actual = failed_attempts > len(HANGMAN)
    expected = True
    assert actual == expected


