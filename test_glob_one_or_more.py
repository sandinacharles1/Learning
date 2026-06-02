import pytest
from glob_one_or_more import OneOrMore
from glob_lit import Lit

def test_one_or_more_empty(): #requires at least one character
    pattern = OneOrMore(Lit(""))
    assert not pattern.match("")

def test_one_or_more_matches_entire_string(): #nothing required to match
    pattern = OneOrMore(Lit(""))
    assert pattern.match("abc")

def test_one_or_more_matches_as_prefix(): #nothing needed in front but then glob_lit goes to the rest and it works
    pattern = OneOrMore(Lit("def"))
    assert pattern.match("abcdef")


def test_one_or_more_matches_as_suffix():#nothing needed in back 
    pattern = Lit("abc", OneOrMore(Lit("")))
    assert pattern.match("abcdef")

def test_one_or_more_matches_interior(): #noothing needed inside
    pattern = Lit("a", OneOrMore(Lit("c")))
    assert pattern.match("abc")