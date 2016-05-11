# -*- coding: utf-8 -*-

import pytest

from bakfu.core import Chain
from bakfu.process.vectorize import vec_sklearn

@pytest.fixture
def fixture():
    '''
    Creates a processor chain with test data.
    '''
    data=((0,'data test 1'),
          (1,'Data test 2'),
          (2,'other data test 3.')
          )
    return Chain().load('data.simple',data)

def setup_module(module):
    print ("setup_module      module:%s" % module.__name__)

def setup_function(method):
    print ("setup_method      method:%s" % method.__name__)

def test_init_simple():
    
    test_subject = fixture().process('vectorize.sklearn')
    vectorizer = test_subject.data['vectorizer']

    assert len(vectorizer.vocabulary_.keys()) > 0
    assert 'data' in vectorizer.vocabulary_


def test_init_kwargs_1():
    
    test_subject = fixture().process(
        'vectorize.sklearn',
        _init={'ngram_range':(1,5)})
    vectorizer = test_subject.data['vectorizer']

    assert len(vectorizer.vocabulary_.keys()) > 0
    assert 'data' in vectorizer.vocabulary_
    assert 'data test' in vectorizer.vocabulary_
    assert vectorizer.ngram_range == (1,5)

def test_init_kwargs_2():
    
    test_subject = fixture().process(
        'vectorize.sklearn',
        ngram_range=(1,5))
    vectorizer = test_subject.data['vectorizer']

    assert len(vectorizer.vocabulary_.keys()) > 0
    assert 'data' in vectorizer.vocabulary_
    assert 'data test' in vectorizer.vocabulary_
    assert vectorizer.ngram_range == (1,5)
