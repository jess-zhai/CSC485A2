#!/usr/bin/env python3
# Student Name: NAME
# Student Number: NUMBER
# UTORid: ID

import typing as T
from collections import defaultdict

from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import Synset

import torch
from torch import Tensor
from torch.linalg import norm

from tqdm import tqdm, trange

from q1 import mfs
from wsd import (batch_evaluate, load_bert, run_bert, load_eval, load_train,
                 WSDToken)

def gather_sense_vectors():

    offset_mappings =  [[[0, 0], [0, 8], [0, 1], [0, 3], [3, 4], [4, 9], [9, 13], [0, 9],
         [0, 1], [0, 0]],
         [[0, 0], [0, 4], [0, 1], [1, 3], [0, 1], [0, 0], [0, 0], [0, 0],
         [0, 0], [0, 0]]]
    for offset_mapping in offset_mappings:
        align = []
        for i, (start, end) in enumerate(offset_mapping):
            if [start, end] == [0, 0]:
                # It's an invalid token, skip it
                continue
            if start == 0:
                # It's the start of a new word
                align.append([i, i + 1])
            else:
                align[-1][1] = i+1
        print(align)

if __name__ == '__main__':
    gather_sense_vectors()