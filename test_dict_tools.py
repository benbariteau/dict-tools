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


def test_flattened_items():
    mydict = {
        'ur': ('mum', 'fat'),
        'no': ('pomegranates',),
    }
    myresult = [
        ('ur', 'mum'),
        ('ur', 'fat'),
        ('no', 'pomegranates'),
    ]
    assert [i for i in flattened_items(mydict)] == myresult


def test_invert_dict():
    mydict = {
        'subscribe to': 'Dull Bananas',
        'hotel': 'trivago',
    }
    myresult = {
        'Dull Bananas': 'subscribe to',
        'trivago': 'hotel',
    }
    assert invert_dict(mydict) == myresult

def test_group_by():
    assert group_by(
        [
            ('foo', 420),
            ('bar', 666),
            ('foo', 69),
            ('bar', 42),
        ],
        key=lambda value: value[0],
    ) == {
        'foo': [('foo', 420), ('foo', 69)],
        'bar': [('bar', 666), ('bar', 42)],
    }
