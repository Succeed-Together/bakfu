# -*- coding: utf-8 -*-
'''
Simple data source
====================
This loader doesn't do much.

.. automodule::
.. autoclass::
.. autoexception::

.. inheritance-diagram:: SimpleDataSource
  :parts: 5
  :private-bases:

'''
from ..core.routes import register
from .base import BaseDataSource

@register('data.simple')
class SimpleDataSource(BaseDataSource):
    '''
    Usage SimpleDataSource(data)
    where :
    data : [(id,'text'), ...]
    '''


    init_kwargs = ('data1',)

    def __init__(self, *args, **kwargs):
        data = kwargs.pop('data', None)
        super(SimpleDataSource, self).__init__(*args, **kwargs)

        if len(args)>0 and data is None:
            data = args[0]

        self.data = data
        self._data['data'] = data

    def run(self, caller, data, *args, **kwargs):
        super(SimpleDataSource, self).run(caller, *args, **kwargs)
        
        self.data = data
        self._data = {'main_data':data,'data':data,'data_source':self}
        return self
