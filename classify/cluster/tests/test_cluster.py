# -*- coding: utf-8 -*-

import pytest

from bakfu.core import Chain
from bakfu.classify.cluster import ward_sklearn
from bakfu.data.simple import SimpleDataSource
from bakfu.process.vectorize.vec_sklearn import CountVectorizer
from bakfu.classify.cluster.ward_sklearn import WardClusterizer

def test_cluster():
    
    data=((0,'data test 1'),
          (1,'Data test 2'),
          (2,'other data test 3.')
          )
    test_subject = Chain().load('data.simple',data).process('vectorize.sklearn').process('cluster.ward')

    
    assert isinstance(test_subject.chain[0],SimpleDataSource)
    assert isinstance(test_subject.chain[1],CountVectorizer)
    assert isinstance(test_subject.chain[2],WardClusterizer)
    
    result = test_subject.get_chain('result')
    assert len(result) == len(data)

    assert result.tolist() == test_subject.chain[-1].get('result').tolist()
    assert result.tolist() == test_subject.chain[-1]._data['result'].tolist()


def test_cluster_ncluster():
    '''
    We test if 3 sets of data are clustered into 3 sets.
    n_clusters is specified.
    '''
    CLASSIFIERS = ('cluster.ward', 'cluster.spectral')

    G1 = 'First set'
    G2 = 'Second group'
    G3 = 'Third cluster'
    data = enumerate((G1,G1,G1,G2,G2,G2,G3,G3,G3))
    data = list(data)

    for classifier in CLASSIFIERS:
        baf = Chain().load('data.simple',data) \
                 .process('vectorize.sklearn') \
                 .process(classifier, n_clusters=3)
    
        result = baf.get_chain('result')


        assert result[0] == result[1] == result[2]
        assert result[3] == result[4] == result[5]
        assert result[6] == result[7] == result[8]

        assert len(set(result)) == 3
