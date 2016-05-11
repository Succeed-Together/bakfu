# -*- coding: utf-8 -*-
'''
tag_treetagger.py

This module is a wrapper to TreeTagger.

'''

import os
import sys
import string

import six
import sklearn
from itertools import chain

from bakfu.core.routes import register
from bakfu.process.base import BaseProcessor

__errors__ = []


try:
    import pattern.fr
except Exception:
    e = sys.exc_info()
    __errors__.append(e)

try:
    import pattern.en
except Exception:
    e = sys.exc_info()
    if e[1].msg == "No module named 'pywordnet'":
        # py3 incompatibility ; must be fixed in pattern
        pass
    else:
        __errors__.append(e)


def tag(tagger, sentence):
    '''
    '''
    lemmas = []
    [lemmas.extend(a.lemma) for a in tagger(sentence,tokenize = True,  tags = True, chunks = True, relations = True, lemmata = True,   light = False)]
    return lemmas


@register('tagging.pattern', __errors__)
class PatternTagger(BaseProcessor):
    '''
    Pre-processes data with pattern.

    :Example:

.. doctest::

    >>>from bakfu.examples.dataset1 import DATA
    >>>import nltk
    >>>baf = bakfu.Chain(lang="en")
    >>>baf.load("data.simple",DATA)
    >>>baf.process('tagging.pattern')
    >>>baf.process('vectorize.sklearn',
    ...        min_df = 2,
    ...        ngram_range=(1, 3),
    ...        #stop_words=nltk.corpus.stopwords.words(baf.get('language')),
    ...        max_features=100,
    ...        tokenizer=lambda x:x,
    ...        )
    ...        preprocessor=lambda x:x,
    >>>print(baf.get_chain("vectorizer").get_feature_names())
    >>>print(baf.get_chain("vectorizer_result").toarray()[0])
    '''

 

    init_args = ()
    init_kwargs = ()
    run_args = ()
    run_kwargs = ()

    def __init__(self, *args, **kwargs):
        super(PatternTagger, self).__init__(*args, **kwargs)
        self.tagger =  None

    def run(self, caller, *args, **kwargs):
        '''
        '''
        super(PatternTagger, self).run(caller, *args, **kwargs)

        data_source = caller.get_chain('data_source')
        self.caller=caller

        lang = caller.get('lang')
        if lang == 'fr':
            self.tagger = pattern.fr.parsetree
        elif  lang == 'en':
            self.tagger = pattern.en.parsetree
            
        cur_data = data_source.get_data()

        result = [tag(self.tagger, s) for s in cur_data]
        caller.data['result'] = result

        #reformat data to ((id,data),...)
        #note: data now contains lists of tokens instead of sentences
        uids = data_source.get_uids()
        new_data = zip(uids, result)

        #Assign processed data to a new data source
        new_data_source = self.caller.load_unchained("data.simple", new_data)

        new_data_source.meta_data = {"tokenized":True}

        self._data.update(
            {'result':result,
             'tagger_result':result,
             'data_source':new_data_source,
            })
        return self
