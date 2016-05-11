"""Base classes for classifiers"""

from ..core.classes import Processor

class BaseClassifier(Processor):
    '''
    The base class for classifiers.
    '''
    def __init__(self, *args, **kwargs):
        super(BaseClassifier, self).__init__(*args, **kwargs)
        self.classifier = None


class SklearnClassifier(BaseClassifier):
    '''
    A class wrapping sklearn classifiers.
    '''

    #The sklearn classifier
    classifier_class = None

    def __init__(self, *args, **kwargs):
        super(BaseClassifier, self).__init__(*args, **kwargs)
        self.init_classifier(*args, **kwargs)

    def init_classifier(self, *args, **kwargs):
        '''
        Init sklearn classifier.
        '''
        self.classifier = self.classifier_class(*args, **kwargs)

    def run_classifier(self, caller, *args, **kwargs):
        pass

    def run(self, caller, *args, **kwargs):
        return self.run_classifier(caller, *args, **kwargs)

    def __getattr__(self, attr):
        '''Propagate attribute search to the clusterizer.'''
        try:
            return getattr(self, attr)
        except:
            return getattr(self.clusterizer, attr)        