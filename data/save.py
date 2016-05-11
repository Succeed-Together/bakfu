# -*- coding: utf-8 -*-
'''
Save/load system

====================
Usage : 

To save a chain to a pickle file : 

::

    baf.process('pickle.save','file.pkl')

To load from a file : 

:: 

    baf = Chain().load('pickle.load','file.pkl')

.. automodule::
.. autoclass::
.. autoexception::

.. inheritance-diagram:: PickleSaver
  :parts: 5
  :private-bases:


.. inheritance-diagram:: PickleLoader
  :parts: 5
  :private-bases:


'''

import pickle

from ..core.routes import register
from .base import BaseDataSource
from bakfu.core import Chain

@register('pickle.save')
class PickleSaver(BaseDataSource):
    '''
    Save chain to a pickle file.

    baf.data('pickle.save','file.pkl')
    '''

    def __init__(self, *args, **kwargs):
        self.save_path = args[0]
        super(PickleSaver, self).__init__(*args, **kwargs)


    def run(self, caller, data, *args, **kwargs):
        super(PickleSaver, self).run(caller, *args, **kwargs)
        save = Chain(lang='en')

        for elt in caller.chain:
            save.data.update(elt._data)
        save.data.pop('data_source')

        with open(self.save_path,"wb") as f:
            pickle.dump(save.data,f)

        return self


@register('pickle.load')
class PickleLoader(BaseDataSource):
    '''
    Load chain from a pickle file.

    baf.data('pickle.load','file.pkl')
    '''
    def __init__(self, *args, **kwargs):
        self.load_path = args[0]        
        super(BaseDataSource, self).__init__(*args, **kwargs)

    def run(self, caller, data, *args, **kwargs):
        super(BaseDataSource, self).run(caller, *args, **kwargs)

        with open(self.load_path,'rb') as f:
            caller.data = pickle.load(f)

        return self
