# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import print_function

import collections
import math
import os
import random
import zipfile

import numpy as np
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin
import tensorflow as tf
import re

class Word2vecWord:
    def __init__(self, word, vector):
        self.word = word
        self.vector = vector

class Word2vecDictionary:
    def __init__(self, reverse_dictionary, final_embeddings):
        self.list = []
        self.words = []
        self.vectors = []
        self.reverse_dictionary = reverse_dictionary
        self.final_embeddings = final_embeddings
        for i, label in enumerate(reverse_dictionary):
            plain_word = str(reverse_dictionary[i]).replace("b'", "").replace("'", "")
            word = Word2vecWord(plain_word, final_embeddings[i])
            self.list.append(word)
            self.words.append(plain_word)
            self.vectors.append(final_embeddings[i])

    def search_word_from_id(self, id):
        return self.words[id]

    def search_vector_from_word(self, input_word):
        try:
            index = self.words.index(input_word)
            return self.final_embeddings[index]
        except ValueError:
            print("not exists")

    def search_word_from_vector(self, input_vector):
        min_distance = 5
        for i,v in enumerate(self.vectors):
            distance = np.linalg.norm(v-input_vector)
            if distance <min_distance:
                result = self.search_word_from_id(i)
                min_distance = distance
        if min_distance<5:
            return result
        else:
            return "not exists"

    def search_words_rankings_from_vector(self, input_vector):
        word_tuples = []

        for i,v in enumerate(self.vectors):
            distance = np.linalg.norm(v-input_vector)
            word_tuples.append((i, self.search_word_from_id(i), distance))

        result = sorted(word_tuples, key=lambda word: word[2] )

        for i,r in enumerate(result):
            print(r)
            if i>5:
                break
