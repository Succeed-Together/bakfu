# -*- coding: utf-8 -*-
import sys
import pytest
import six
from bakfu.core import Chain
from bakfu.process.tagging import tag_pattern

@pytest.fixture
def fixture_en():
    '''
    Creates a processor chain with test data.
    '''
    data=((0,'This is a test.'),
          (1,'We were testing.'),
          (2,'Other things. More tests.')
          )
    return Chain(lang='en').load('data.simple',data)


@pytest.mark.skipif(sys.version_info >= (3,0),
                    reason="does not support python 3")
def test_tagging_en():
    baf = fixture_en()
    baf.process('tagging.pattern')
    tagged_data = baf.get_chain("data_source").get_data()
    reference_tagged_data = [['this', 'be', 'a', 'test', '.'], ['we', 'be', 'testing', '.'], ['other', 'thing', '.', 'more', 'test', '.']]
    assert tagged_data == reference_tagged_data


@pytest.fixture
def fixture_fr():
    '''
    Creates a processor chain with test data.
    '''
    data=((0,'Ceci est un test.'),
          (1,'Autres choses. Autres tests.')
          )
    return Chain(lang='fr').load('data.simple',data)


@pytest.mark.skipif(sys.version_info >= (3,0),
                    reason="does not support python 3")
def test_tagging_fr():
    baf = fixture_fr()
    baf.process('tagging.pattern')
    tagged_data = baf.get_chain("data_source").get_data()

    if six.PY3:
        reference_tagged_data = [['ceci', '\xeatre', 'un', 'test', '.'], ['autre', 'choses', '.', 'autre', 'test', '.']]
    else:
        reference_tagged_data = [[u'ceci', u'\xeatre', u'un', u'test', u'.'], [u'autre', u'choses', u'.', u'autre', u'test', u'.']]

    assert tagged_data == reference_tagged_data
