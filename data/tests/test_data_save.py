# -*- coding: utf-8 -*-

import os
import tempfile

import six
import pytest

import bakfu
from bakfu.core import Chain
print(bakfu.routes.list_modules())


def test_data_save_load():

    data=((0,'data test 1'),
          (1,'Data test 2'),
          (2,'other data test 3.')
          )
    test_subject = Chain().load('data.simple',data)
    data = test_subject.data['base_data']
    test_subject.process("vectorize.sklearn")

    with tempfile.TemporaryDirectory() as tmpdirname:
        save_path = os.path.join(tmpdirname,'save.pkl')
        test_subject.process('pickle.save', save_path)
        load_test = Chain().load('pickle.load', save_path)

        assert load_test.get_chain('vectorizer').transform(('test',)).toarray()[0].tolist() == \
                test_subject.get_chain('vectorizer').transform(('test',)).toarray()[0].tolist() == \
                [0,0,1]


# disable py2 incompatible code
if six.PY2:
    test_data_save_load = lambda :0

