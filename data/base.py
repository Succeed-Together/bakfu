# -*- coding: utf-8 -*-
'''
Base data source
====================
This base data source others inherit from.

.. automodule::
.. autoclass::
.. autoexception::

.. inheritance-diagram::
  :parts: 5
  :private-bases:

'''
from ..core.routes import register
from abc import abstractmethod
from ..core.classes import Processor


@register('data.base')
class BaseDataSource(Processor):
    '''
    data: [(id,'text'),]
    '''
    def __init__(self, *args, **kwargs):
        super(BaseDataSource, self).__init__(*args, **kwargs)
        self.data = None

    def get_data(self):
        '''
        returns a list of str
        ['text1', 'text2', ...]
        '''
        return [d[1] for d in self.data]

    def get_uids(self):
        '''Returns a list of ids for the data elements.'''
        return [d[0] for d in self.data]

    def get_uid_to_index_map(self):
        '''Returns a map from uids to indices in the list.'''
        return dict([(d[0], i) for i, d in enumerate(self.data)])
