# -*- coding: utf-8 -*-
'''
Random Forest classifier
'''

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from ...core.routes import register
from .base import BaseMl, BaseMlSk
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier

@register('ml.forest')
class ForestMl(BaseMlSk):
    '''Random forest
Parameters (not implemented yet) :
classifier : if not specified, create a new classifier.
data : if not specified, get most recent data from the chain.
action : if not specified, a new classifier will be created 
    and used on available data
    if 'fit' : classifier is created but not used
    if 'predict': previous classifier is used
Usage : 
#create clusters
baf.process('cluster.ward')
#load new data
baf.load('data.simple',(...))
#train classifier and use 
baf.process('ml.forest')

TODO: Allow reuse of classifiers.
    '''
    init_kwargs = ('n_estimators', 'classifier', 'data', 'action')
    run_kwargs = ()
    #max_depth
    #init_method = RandomForestClassifier.__init__
    #run_method = RandomForestClassifier.fit_transform
    classifier_class = RandomForestClassifier



@register('ml.extratrees')
class ExtraTreesMl(BaseMlSk):
    '''
    '''
    init_kwargs = ('n_estimators', 'classifier', 'data', 'action')
    run_kwargs = ()
    classifier_class = ExtraTreesClassifier


@register('ml.decisiontree')
class ExtraTreesMl(BaseMlSk):
    '''
    '''
    classifier_class = DecisionTreeClassifier

