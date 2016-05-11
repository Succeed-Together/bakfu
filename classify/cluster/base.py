# -*- coding: utf-8 -*-

from abc import abstractmethod
from ...core.classes import Processor
from ..base import SklearnClassifier

class BaseClusterizer(SklearnClassifier):
    '''Base class for vectorizers. 
    '''
    def __init__(self, *args, **kwargs):
        super(BaseClusterizer, self).__init__( *args, **kwargs)

        #deprecated : use classifier
        self.clusterizer = None

    def run_classifier(self, caller, *args, **kwargs):
        data_source = caller.data['main_data']
        vectorizer_result = caller.data['vectorizer_result']

        X = vectorizer_result
        predictions = self.classifier.fit_predict(X.toarray())

        caller.data['clusterizer_result'] = predictions
        caller.data['labels'] = predictions
        caller.data['clusterizer'] = self.classifier

        return self.update(
            result=predictions,
            classifier_result=predictions,)

