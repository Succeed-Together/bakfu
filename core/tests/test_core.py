# -*- coding: utf-8 -*-

import pytest

from bakfu.core import Chain


def test_core_chain():
    '''
    Create a processor and test if
    .get on processor will propagate the call
    '''
    data=((0,'0'), (1,'1'), )
    test_subject = Chain()

    with pytest.raises(KeyError) as excinfo:
        assert test_subject.get('test') == 'ok'

    test_subject.data['test'] = 'ok'

    assert test_subject.get('test') == 'ok'

    test_subject.load('data.simple',data)

    # get data from the main class through the chain
    assert test_subject.chain[-1].get('base_data').data == data
    assert test_subject.get_chain('base_data').data == data

    # get data from the chain
    test_subject.chain[-1]._data['last_data'] = 'last_data'
    assert test_subject.get_chain('last_data') == 'last_data'



def test_core_data():
    '''
    Load dummy data and verify it.
    '''
    data=((0,'0'), (1,'1'), )
    test_subject = Chain()    
    test_subject.load('data.simple',data)
    assert test_subject.get('base_data').data == data



def test_core_data_chain():
    '''
    When overriding data the last data should be used.
    '''
    data = ((0,'0'), (1,'1'), )
    data_new = ((0,"new"),(1,"new"))

    test_subject = Chain()
    test_subject.load('data.simple',data)
    assert test_subject.get_chain('data_source').data == data
    test_subject.load('data.simple',data_new)
    assert test_subject.get_chain('data_source').data == data_new





