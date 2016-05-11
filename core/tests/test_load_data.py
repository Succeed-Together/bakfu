# -*- coding: utf-8 -*-

import os
import sys

import pytest

from bakfu.core import Chain

@pytest.mark.skipif(sys.version_info >= (3,0),
                    reason="does not support python 3")
def test_core_load_json():
    '''
    Load a chain from a json file.
    '''

    baf = Chain.load_json(path=
            os.path.join(os.path.dirname(__file__), "data1.json")
            )

    assert baf.data['lang'] == 'fr'
    assert  baf.data_sources[-1].data == [
            (1, [u'ceci', u'\xeatre', u'un', u'test', u'.']), 
            (2, [u'cette', u'phrase', u'\xeatre', u'un', u'autre', u'test', u'.'])
            ]

@pytest.mark.skipif(sys.version_info >= (3,0),
                    reason="does not support python 3")
def test_core_load_yaml():
    '''
    Load a chain from a yaml file.
    '''

    baf = Chain.load_yaml(path=
            os.path.join(os.path.dirname(__file__), "data2.yaml")
            )

    assert baf.data['lang'] == 'en'
    print(baf.data_sources[-1].data )
    assert  baf.data_sources[-1].data == [
            (1, [u'this', u'be', u'a', u'test', u'.']), 
            (2, [u'another', u'test', u'sentence', u'.']), 
            (3, [u'yet', u'another', u'sentence', u'.']), 
            (4, [u'two', u'sentence', u'this', u'time', u'.'])
            ]


