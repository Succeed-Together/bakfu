# -*- coding: utf-8 -*-

'''
Ward clustering using sklearn
'''

from sklearn.cluster import Ward
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from ...core.routes import register
from .base import BaseClusterizer


@register('cluster.ward')
class WardClusterizer(BaseClusterizer):

    init_kwargs = ('n_clusters',)
    classifier_class = Ward

    #def __init__(self, *args, **kwargs):
        #super(WardClusterizer, self).__init__(*args, **kwargs)

        #self.clusterizer = Ward(**kwargs)

    #def clusterize(self, data_source, *args, **kwargs):
        #'''

        #'''

        #self.results = {'clusters':result}

        #return result

    #def run(self, caller, *args, **kwargs):
        #data_source = caller.data['main_data']
        #vectorizer_result = caller.data['vectorizer_result']

        #X = vectorizer_result
        #predictions = self.clusterizer.fit_predict(X.toarray())

        #caller.data['clusterizer_result'] = predictions
        #caller.data['clusterizer'] = self.clusterizer

        #return self.update(
            #result=predictions,
            #clusterizer_result=predictions)