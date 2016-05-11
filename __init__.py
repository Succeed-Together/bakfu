# -*- coding: utf-8 -*-
"""
bakfu
"""
__version__ = '0.1 α'

import six

import bakfu.data
import bakfu.process
import bakfu.classify
import bakfu.tools

from .core import Chain
from .core import routes
from .core.routes import list_modules

__all__ = ['Chain', 'list_modules']

if len(routes.__processors_failed__)>0:
    print('WARNING :The following modules failed to register : ')
    for failed in six.iterkeys(routes.__processors_failed__):
        print(failed)
