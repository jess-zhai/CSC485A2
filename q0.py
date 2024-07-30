#!/usr/bin/env python3
# Student Name: Xueqing Zhai
# Student Number: 1006962413
# UTORid: zhaixueq

import typing as T
from string import punctuation
from nltk.corpus import stopwords, wordnet as wn
from nltk.tokenize import word_tokenize

def deepest():
    """Find and print the synset with the largest maximum depth along with its
    depth on each of its hyperonym paths.

    Returns:
        None
    """
    ### START CODE HERE
    deepest_set = None
    max_depth = 0
    for synset in wn.all_synsets():
        depth = synset.max_depth()
        if depth > max_depth:
            max_depth = depth
            deepest_set = synset

    print("Deepest Synset:", deepest_set)
    print("Maximum Depth:", max_depth)
    print("Hypernym Paths and Depths:")

    for i, hypernym_path in enumerate(deepest_set.hypernym_paths()):
        print(f"Path {i + 1}:")
        for j, hypernym in enumerate(hypernym_path):
            print(f"  {hypernym} (Depth: {j})")
            #print(f"  {hypernym} (Depth: {hypernym.max_depth()})")
    # raise NotImplementedError


def superdefn(s: str) -> T.List[str]:
    """Get the "superdefinition" of a synset. (Yes, superdefinition is a
    made-up word. All words are made up...)

    We define the superdefinition of a synset to be the list of word tokens,
    here as produced by word_tokenize, in the definitions of the synset, its
    hyperonyms, and its hyponyms.

    Args:
        s (str): The name of the synset to look up

    Returns:
        list of str: The list of word tokens in the superdefinition of s

    Examples:
        >>> superdefn('toughen.v.01')
        ['make', 'tough', 'or', 'tougher', 'gain', 'strength', 'make', 'fit']
    """
    ### START CODE HERE
    tokens = []
    synset = wn.synset(s)
    tokens.extend(word_tokenize(synset.definition()))
    hypernyms = synset.hypernyms()
    hyponyms = synset.hyponyms()

    for hypernym in hypernyms:
        tokens.extend(word_tokenize(hypernym.definition()))
    for hyponym in hyponyms:
        tokens.extend(word_tokenize(hyponym.definition()))

    return tokens
    #raise NotImplementedError


def stop_tokenize(s: str) -> T.List[str]:
    """Word-tokenize and remove stop words and punctuation-only tokens.

    Args:
        s (str): String to tokenize

    Returns:
        list[str]: The non-stopword, non-punctuation tokens in s

    Examples:
        >>> stop_tokenize('The Dance of Eternity, sir!')
        ['Dance', 'Eternity', 'sir']
    """
    ### START CODE HERE
    tokens = word_tokenize(s)
    stop_words = set(stopwords.words('english'))
    ret = []
    for token in tokens:
        temp = token.lower()
        if token in ret or temp in ret or temp in punctuation or temp in stop_words:
            continue
        ret.append(token) # changed back
    
    return ret
    #raise NotImplementedError


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    deepest()
