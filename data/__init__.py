# -*- coding: utf-8 -*-
'''
Data is expected to be of the form :

data = (
    (id, data),
    (id, data),
    ...
    )



.. automodule:: bakfu.data.base
.. automodule:: bakfu.data.simple
.. automodule:: bakfu.data.data_xml
.. automodule:: bakfu.data.data_redis
.. automodule:: bakfu.data.data_mongo
.. automodule:: bakfu.data.data_rest
'''


from . import base
from . import simple
from . import data_redis
#from . import data_rest
from . import data_mongo
from . import data_xml
from . import save
