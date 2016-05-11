# -*- coding: utf-8 -*-
'''
Main classes
'''
from abc import abstractmethod
import inspect
from itertools import chain

def get_args_and_kwargs(var):
    '''Extracts args ans kwargs variables from
    the following forms :
    ((*args),{kwargs}), 
    (*args), 
    {kwargs}, 
    Returns :
    (args,kwargs)

    The form : 
    (*args,{kwargs}) can lead to errors  
    and is not accepted
    '''
    if isinstance(var, dict):
        return (), var
    elif len(var) == 2 and isinstance(var[1], dict):
        return var
    return var, {}

class Processor(object):
    '''
    The base class for the processing chain.
    Each processor represents an step in the chain.

    The processor acts as a wrapper to other classes.
    It works with 2 steps :
    #) init
    #) run
    '''


    init_args = ()
    init_kwargs = ()
    run_args = ()
    run_kwargs = ()

    init_method = None
    run_method = None

    @staticmethod
    def _update_kwargs(valid_list, source, target):
        '''
        Find items matching keys in sources from valid_list
        and put them in target.
        '''
        for key in valid_list:
            if key != 'self' and key in source:
                target[key] = source.pop(key)
        return target

    @classmethod
    def get_args_list(cls, method):
        '''Get argument list from wrapped class.'''
        return inspect.getargspec(method).args

    @classmethod
    def get_args_list_init(cls):
        '''Get argument list from wrapped class when calling init.'''
        if cls.init_method:
            return cls.get_args_list(cls.init_method)
        return ()

    @classmethod
    def get_args_list_run(cls):
        '''Get argument list from wrapped class when calling run.'''
        if cls.run_method:
            return cls.get_args_list(cls.run_method)
        return ()

    def __init__(self, *args, **kwargs):
        self._next = None
        self._prev = None
        self._data = {}

    @abstractmethod
    def run(self, caller, *args, **kwargs):
        pass

    @staticmethod
    def init_run_static(cls, caller, predecessor, *args, **kwargs):
        '''
        This method will parse args, kwargs and
        call functions __init__ and run with the
        corresponding parameters.
        '''

        if '_init' in kwargs:
            init_args, init_kwargs = get_args_and_kwargs(kwargs.pop('_init'))
        else:
            init_args, init_kwargs = (), {}

        #useless block ?
        #for kw in cls.init_kwargs:
            #if kw in kwargs:
                #init_kwargs[kw] = kwargs.pop(kw)

        init_valid_keys = chain(cls.get_args_list_init(), cls.init_kwargs)
        cls._update_kwargs(init_valid_keys, kwargs, init_kwargs)

        if len(init_args) == 0:
            init_args = args

        obj = cls(*init_args, **init_kwargs)
        obj._prev = predecessor

        if '_run' in kwargs:
            run_args, run_kwargs = get_args_and_kwargs(kwargs.pop('_run'))
        else:
            run_args, run_kwargs = args, kwargs

        #useless block ?
        #for kw in cls.run_kwargs:
            #if kw in kwargs:
                #run_kwargs[kw] = kwargs.pop(kw)

        run_valid_keys = chain(cls.get_args_list_run(), cls.run_kwargs)
        cls._update_kwargs(run_valid_keys, kwargs, run_kwargs)

        if len(run_args) == 0:
            run_args = args

        obj.run(caller, *run_args, **run_kwargs)

        return obj

    @classmethod
    def init_run(cls, caller, *args, **kwargs):
        return Processor.init_run_static(cls, caller, *args, **kwargs)

    def next(self):
        '''Returns the next Processor in the chain.'''
        return self._next

    def prev(self):
        '''Returns the previous Processor in the chain.'''
        return self._prev

    def get(self, key):
        '''Looks for something. If not found, look in prev element.'''
        if key in self._data:
            return self._data.get(key)
        return self.prev().get(key)

    def update(self, **kwargs):
        '''Update _data '''
        self._data.update(kwargs)
        return self

    def __repr__(self):
      try:
          return self.registered_name
      except:
          return object.__repr__(self)

