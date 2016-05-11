# -*- coding: utf-8 -*-

import os
import pytest

from bakfu.core import Chain


def test_data_xml():
    filepath = os.path.join(os.path.dirname(__file__), 'data.xml')
    baf = Chain().load('data.xml',
            file=filepath,
            query='//answer',
            processor=lambda x:x.text,
            target_processor=lambda x:x.attrib['label']
            )

    data_source = baf.data['base_data']

    assert data_source.get_data() == ['Test 1',
        'Test 2',
        'Test 3',
        'Other',
        'Other 2',
        'Other 3']
    assert data_source.targets == ['1', '1', '1', '2', '2', '2']
