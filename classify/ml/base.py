# -*- coding: utf-8 -*-
'''
Base class for machine supervised classifiers.
'''

from abc import abstractmethod
import six
from ...core.classes import Processor

class BaseMl(Processor):
    '''Base class for vectorizers. 
    '''
    def __init__(self, *args, **kwargs):
        super(BaseMl, self).__init__(*args, **kwargs)
        self.clusterizer = None
        self.classifier = None

    def __getattr__(self, attr):
        '''Propagate attribute search to the vectorizer.'''
        if attr == 'classifier':
            return super(BaseMl, self).getattr(attr)
        try:
            return super(BaseMl, self).getattr(attr, None)
        except AttributeError:
            return getattr(self.classifier, attr)


class BaseMlSk(BaseMl):
    '''
    Base class for sklearn supervised classifiers. 
    '''
    classifier_class = None

    init_kwargs = ()
    run_kwargs = ()

    def __init__(self, *args, **kwargs):
        super(BaseMlSk, self).__init__(*args, **kwargs)
        self.action = kwargs.pop('action',None)

        init_kwargs = {k:v for k,v in six.iteritems(kwargs) if k in self.init_kwargs}

        if self.action != "predict":
            self.classifier = self.classifier_class(**init_kwargs)
            self._data['classifier'] = self.classifier
        else:
            self.classifier = None

    def _get_classifier(self):
        if self.classifier:
            return self.classifier
        else:
            classifier = self.get('classifier')
            self.classifier = classifier
            return classifier

    def fit(self, caller, *args, **kwargs):
        '''Train a classifier from tagged data'''
        classifier = self._get_classifier()

        vectorizer_result = caller.get('vectorizer_result')
        #clusters = caller.get("clusterizer_result")
        clusters = caller.get_chain('labels')
        classifier.fit(vectorizer_result.toarray(), clusters)

        return classifier

    def predict(self, caller, *args, **kwargs):
        '''Use classifier on new data'''
        classifier = self._get_classifier()
        vectorizer = caller.get_chain('vectorizer')

        #New data
        data_source = caller.get_chain("data_source")
        new_vectorizer_result = vectorizer.transform(data_source.get_data())
        self.new_vectorizer_result = new_vectorizer_result
        result = self.classifier.predict(new_vectorizer_result.toarray())

        return result

    def run(self, caller, *args, **kwargs):
        super(BaseMlSk, self).run(caller,*args, **kwargs)

        if self.action in (None, 'fit'):
            result = self.fit(caller, *args, **kwargs)
            self.update(
                result = result,
                classifier = result
                )

        if self.action in (None, 'predict'):
            result = self.predict(caller, *args, **kwargs)
            self.update(
                result=result,
                classifier_result=result,
                new_vectorizer_result=self.new_vectorizer_result
                )

        return self