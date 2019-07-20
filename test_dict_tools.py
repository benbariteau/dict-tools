import pytest
from dict_tools import *


def test_map_keys():
    myfunc = (lambda x: x+'_suffix')
    mydict = {
        'fbi': 0,
        'open': 1,
        'up': 2,
    }
    myresult = {
        'fbi_suffix': 0,
        'open_suffix': 1,
        'up_suffix': 2,
    }
    assert map_keys(myfunc, mydict) == myresult


def test_map_values():
    myfunc = (lambda x: x+1)
    mydict = {
        'one': 0,
        'two': 1,
        'three': 2,
    }
    myresult = {
        'one': 1,
        'two': 2,
        'three': 3,
    }
    assert map_values(myfunc, mydict) == myresult


def test_map_all():
    myfunc = (lambda x: x-1)
    mydict = {
        1: 1,
        2: 2,
    }
    myresult = {
        0: 0,
        1: 1,
    }
    assert map_all(myfunc, mydict) == myresult


def test_iter_multi_values():
    mydict = {
        'ur': ('mum', 'fat'),
        'no': 'pomegranates',
    }
    myresult = [
        ('ur', 'mum'),
        ('ur', 'fat'),
        ('no', 'pomegranates'),
    ]
    assert [i for i in iter_multi_values(mydict)] == myresult


def test_swap_key_value():
    mydict = {
        'subscribe to': 'Dull Bananas',
        'hotel': 'trivago',
    }
    myresult = {
        'Dull Bananas': 'subscribe to',
        'trivago': 'hotel',
    }
    assert swap_key_value(mydict) == myresult
