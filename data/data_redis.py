# -*- coding: utf-8 -*-
'''
:mod:`bakfu.data.data_redis` loads data from a redis database.

'''
import six

try:
    import redis
except ImportError:
    pass

from ..core.routes import register
from .base import BaseDataSource



@register('data.redis')
class RedisDataSource(BaseDataSource):
    '''
    By default, the redis data must be a str representation following :
    ((id,data), (id,data), ...) 

    Example: 
    .load('data.redis',_init=((),{'keyname':'data1'}))
    '''

    def __init__(self, *args, **kwargs):
        super(RedisDataSource, self).__init__()

        self.keyname = kwargs.get('keyname', 'data')
        self.redis = redis.StrictRedis()

    def run(self, caller, *args, **kwargs):
        self.data = eval(self.redis.get(self.keyname) or '[]')
        #A.decode('unicode_escape')
        return self

