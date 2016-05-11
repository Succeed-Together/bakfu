# -*- coding: utf-8 -*-

'''
:mod:`bakfu.data.data_mongo` provides an interface to mongo databases.
'''

import six

try:
    import pymongo
except ImportError:
    pass

from ..core.routes import register
from .base import BaseDataSource


@register('data.mongo')
class MongoDataSource(BaseDataSource):
    '''

    '''

    def __init__(self, *args, **kwargs):
        super(MongoDataSource, self).__init__()

        self.db_host = kwargs.get('host', 'mongodb://localhost:27017')
        self.mongo_db = pymongo.Connection(self.db_host)

    def run(self, caller, *args, **kwargs):

        db_name = kwargs.get('db', 'dbtest1')
        collection_name = kwargs.get('collection', 'collection1')

        mongo_db = self.mongo_db[db_name][collection_name]

        collection_name = kwargs.get('collection', 'collection1')
        self.data = mongo_db.find()
        self.data = [(a['id'], a['text']) for a in self.data]

        return self

