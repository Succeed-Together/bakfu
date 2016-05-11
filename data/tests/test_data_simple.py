# -*- coding: utf-8 -*-

import pytest

from bakfu.core import Chain


def test_data_simple():
    
    data=((0,'data test 1'),
          (1,'Data test 2'),
          (2,'other data test 3.')
          )
    test_subject = Chain().load('data.simple',data)
    data = test_subject.data['base_data']

    assert test_subject.data['base_data']==test_subject.data['main_data']
    assert data.get_data() == ['data test 1', 'Data test 2', 'other data test 3.']
    assert data.get_uids() == [0, 1, 2]
