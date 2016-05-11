# -*- coding: utf-8 -*-
'''
Xml data source
====================
Loads data from xml file.

Usage :

    baf = bakfu.Chain().load('data.xml',
            file='./data.xml',
            query='//answer',
            processor=lambda x:x.text,
            targets_processor=lambda x:x.attrib['label']
            )


.. automodule::
.. autoclass::
.. autoexception::

.. inheritance-diagram:: SimpleDataSource
  :parts: 5
  :private-bases:

'''


import codecs
try:
    import lxml.etree
except:
    pass
import six
from six.moves import cStringIO

from bakfu.core.routes import register
from bakfu.data.base import BaseDataSource


@register('data.xml')
class XmlDataSource(BaseDataSource):
    '''
    Xml loader.
    '''
    init_kwargs = ('file', 'query', 'processor', 'target_processor')

    def __init__(self, *args, **kwargs):
        super(XmlDataSource, self).__init__()
        
        filename = kwargs.get('file',None)
        if filename is None:
            raise Exception('No file specified')


        #parse file
        if six.PY2:
            text = open(filename).read()
            parser = lxml.etree.XMLParser(recover=True, encoding='utf-8')
            #xml = etree.fromstring(text, parser)
            xml = lxml.etree.parse(cStringIO(text))
        else:
            text = open(filename).read().encode('utf-8')
            parser = lxml.etree.XMLParser(recover=True, encoding='utf-8')
            xml = lxml.etree.XML(text)


        #find data elements
        query_result = xml.xpath(kwargs['query'])

        processor = kwargs['processor']
        self.data = [
                (idx,processor(elt)) for idx,elt in enumerate(query_result)
                ]

        self._data = {'main_data':self.data,'data':self.data,
                        'data_source':self}

        if kwargs.get('target_processor', None) is not None:
            target_processor = kwargs['target_processor']
            self.targets = [
                    target_processor(elt) for elt in query_result
                    ]
            self._data['targets'] = self.targets
            self._data['labels'] = self.targets


    def run(self, caller, *args, **kwargs):
        return self


