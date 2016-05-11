# -*- coding: utf-8 -*-
import re
import six

__processors__ = {}
__processors_failed__ = {}

def get_processor(name, regexp=None):
    if regexp == None:
        try:
            return  __processors__[name]
        except:
            raise KeyError("Unknown processor : {}".format(name))
    else:
        regexp = re.compile(regexp)
        return [key for key in __processors__.keys()
                if regexp.match(key)]
    


def register(name, errors = []):
    '''
    Try to register processor.
    If processor cannot be registered,
    it is added to the __processors_failed__ list.
    '''
    def decorator(processor):
        global __processors__
        global __processors_failed__
        if errors == []:
            __processors__[name] = processor
            processor.registered_name = name            
            return processor
        else:
            __processors_failed__[name] = errors            
    return decorator

def list_modules(failed=False):
    '''
    List all registered modules.
    If failed, also list failed modules.
    '''
    for name,processor in six.iteritems(__processors__):
        print(name)
    
    if failed:
        print("\n\nFailed modules : \n")
        for name,errors in  six.iteritems(__processors_failed__):
            print(name)
            for error in errors:
                print(error)
            

'''

import bakfu.data.base
from bakfu.core.routes import __processors__
__processors__
bakfu.data.base.BaseDataSource
'''

