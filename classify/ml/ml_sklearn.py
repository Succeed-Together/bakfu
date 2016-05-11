# -*- coding: utf-8 -*-
'''
Random Forest classifier
'''

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler

from ...core.routes import register
from .base import BaseMl, BaseMlSk
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.lda import LDA

@register('ml.gaussianNB')
class SKGaussianNB(BaseMlSk):
    '''
    Gaussian Naive Bayes (from sklearn)
    '''
    init_kwargs = ('class_count_', 'theta_', 'sigma_',
                   'classifier', 'data', 'action')
    run_kwargs = ()
    classifier_class = GaussianNB


@register('ml.AdaBoost')
class AdaBoost(BaseMlSk):
    '''
    AdaBoost (from sklearn)
    '''
    init_kwargs = ('base_estimator', 'n_estimators', 
                   'learning_rate', 'algorithm', 'random_state',
                   'classifier', 'data', 'action')
    run_kwargs = ()
    classifier_class = AdaBoostClassifier

@register('ml.KNeighborsClassifier')
class AdaBoost(BaseMlSk):
    '''
    AdaBoost (from sklearn)
    '''
    init_kwargs = ('n_neighbors', 'weights', 
                   'algorithm', 'gamma', 'coef0', 'probability', 'shrinking',
                   'tol', 'cache_size', 'class_weight', 'max_iter', 'random_state',
                   'classifier', 'data', 'action')
    run_kwargs = ()
    classifier_class = KNeighborsClassifier

@register('ml.SVC')
class AdaBoost(BaseMlSk):
    '''
    AdaBoost (from sklearn)
    '''
    init_kwargs = ('C', 'kernel', 
                   'degree', 'leaf_size', 'metric', 'p', 'metric_params',
                   'classifier', 'data', 'action')
    run_kwargs = ()
    classifier_class = SVC

@register('ml.LDA')
class LDA(BaseMlSk):
    '''
    LDA (from sklearn)
    '''
    init_kwargs = ('solver', 'shrinkage', 'priors', 'n_components', 
                   'store_covariance', 'tol')
    run_kwargs = ()
    classifier_class = LDA

