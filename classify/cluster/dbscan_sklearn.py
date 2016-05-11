# -*- coding: utf-8 -*-
'''
DBSCAN clustering through sklearn.
'''

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from ...core.routes import register
from .base import BaseClusterizer


@register('cluster.dbscan')
class DBSCANClusterizer(BaseClusterizer):

    def __init__(self, *args, **kwargs):
        super(DBSCANClusterizer, self).__init__(*args, **kwargs)
        clusterizer = DBSCAN(*args, **kwargs)
        self._data['clusterizer'] = clusterizer


    def clusterize(self, data_source, *args, **kwargs):
        '''

        '''
        self.data['result'] = 42

        return result

    def run(self, caller, *args, **kwargs):
        super(DBSCANClusterizer, self).run(*args, **kwargs)

        data_source = caller.data['main_data']
        vectorizer_result = caller.data['vectorizer_result']

        X = StandardScaler(with_mean=False).fit_transform(vectorizer_result)
        db = self.clusterizer.fit(X)

        caller.data['clusterizer_result'] = db
        caller.data['labels'] = db

        return self.update(
            result=db,
            clusterizer_result=db)


