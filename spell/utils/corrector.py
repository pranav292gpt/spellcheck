import re
from collections import Counter
from db.models import WordFrequency, BigWordFrequency
from django.db.models import Min

f = open("right_wrong.txt", "r").readlines()


def words(text):
    return re.findall(r'\w+', text)

#WORDS = open('lac_words', 'r').readlines()

"""def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N
"""
def correction(word): 
    if not WordFrequency.objects.filter(word=word).exists():
        for line in f:
            if word in re.split("[^\\w'*]+",line.lower()):
                line =  re.split("[^\\w']+",line.lower())
                #print line
                return line[0]
    if   (first_known([word]) or first_known(edits1(word)) or first_known(edits2(word))):
        return (first_known([word]) or first_known(edits1(word)) or first_known(edits2(word)))

    if (first_known_big(edits1(word)) or first_known_big(edits2(word))):
        return (first_known_big(edits1(word)) or first_known_big(edits2(word)))
    return(word)
    #return "Hello"
'''
    #"Most probable spelling correction for word."
    elif (first_known([word]) or first_known(edits1(word)) or first_known(edits2(word)) or word):
        return (first_known([word]) or first_known(edits1(word)) or first_known(edits2(word)) or word)
    '''

'''def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])
'''
def extended_corrections(word):
    if known(edits1(word)):
        corrections = known(edits1(word))
    #if known(edits2(word)):
    #  corrections.append(known(edits2(word)))
        return corrections

def known(words):
    word_list = []
    known = WordFrequency.objects.filter(word__in=words)
    for w in known:
        word_list.append(w.word)
    return word_list

def first_known(words):
    w = WordFrequency.objects.filter(word__in=words)
    try:
        first = WordFrequency.objects.filter(word__in=words).first().word
        return first
    except Exception:
        pass
    
def first_known_big(words):
    w = BigWordFrequency.objects.filter(word__in=words)
    try:
        first = BigWordFrequency.objects.filter(word__in=words).first().word
        return first
    except Exception:
        pass



def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
