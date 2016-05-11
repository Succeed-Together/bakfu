# -*- coding: utf-8 -*-

'''
This is an interface to sklearn vectorizer classes.

'''

from sklearn.cluster import SpectralClustering
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from ...core.routes import register
from .base import BaseClusterizer


@register('cluster.spectral')
class SpectralClusterizer(BaseClusterizer):
    
    init_kwargs = ('n_clusters',)
    classifier_class = SpectralClustering


