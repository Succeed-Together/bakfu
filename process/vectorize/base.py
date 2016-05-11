# -*- coding: utf-8 -*-
'''

'''

from ...core.classes import Processor

class BaseVectorizer(Processor):
    '''Base class for vectorizers.
    '''
    def __init__(self, *args, **kwargs):
        super(BaseVectorizer, self).__init__(*args, **kwargs)
        self.vectorizer = None
        
    def __getattr__(self, attr):
        '''Propagate attribute search to the vectorizer.'''
        if attr == 'vectorizer':
            return super(BaseVectorizer, self).getattr(attr)
        try:
            return super(BaseVectorizer, self).getattr(attr, None)
        except AttributeError:
            return getattr(self.vectorizer, attr)
