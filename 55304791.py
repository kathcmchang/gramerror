#!/usr/bin/env python
# coding: utf-8

# In[72]:


import nltk
import string

#capitalization error
def CapError(sent):
    if sent[0].islower():
        return True 
    
#fragment error
def FragError(tagged_words):
    if 'V' not in str(tagged_words):
        return True
    
#verb form error
def hasModalError(curTags):
    if curTags[2].startswith('V') and (curTags[2] != 'VB'):
        if (curTags[1] == 'MD') or (curTags[1] == 'TO'):
            return True
        elif (curTags[0] == 'MD' or (curTags[0] == 'TO')) and (not curTags[1].startswith('V')):
            return True
    return False

#Subject-verb agreement error
def SubjVError(curTags, curWTags):
    if curTags[2].startswith('V') and (curTags[2] == 'VBP' or curTags[2] == 'VBD'):
        if curTags[1] == 'NN' or curTags[1] == 'NNP':
            return True
        elif (curTags[0] == 'NN' or curTags[0] == 'NNP') and (not curTags[1].startswith('V')):
            return True
    if curTags[2].startswith('V') and (curTags[2] == 'VBZ' or curTags[2] == 'VBD'):
        if (curTags[1] == 'NNS') or (curTags[1] == 'NNPS'):
            return True
        elif (curTags[0] == 'NNS' or curTags[0] == 'NNPS') and (not curTags[1].startswith('V')):
            return True
    if curTags[2] == 'VB' or curTags[2] == 'VBP':
        if curWTags[1].lower() == 'he' or curWTags[1].lower() == 'she' or curWTags[1].lower() == 'it':
            return True
        elif (curWTags[0].lower() == 'he' or curWTags[0].lower() == 'she' or curWTags[0].lower() == 'it') and (not curTags[1].startswith('V')):
            return True
    if curTags[2] == 'VBZ':
        if curWTags[1].lower() == 'i' or curWTags[1].lower() == 'you' or curWTags[1].lower() == 'we' or curWTags[1].lower() == 'they':
            return True
        elif (curWTags[0].lower() == 'i' or curWTags[0].lower() == 'you' or curWTags[0].lower() == 'we' or curWTags[0].lower() == 'they') and (not curTags[1].startswith('V')):
            return True
    return False
        
        
#Spelling error
def SpellError(curWord, curPOS):
    curWordLow = curWord.lower()
    lemma = wnl.lemmatize(curWordLow)
    if curPOS.startswith('V'):
        lemma = wnl.lemmatize(lemma,'v')
    if (not lemma in wordlist) and (not lemma in string.punctuation) and (not curPOS == 'NNP'):
        return True
    
wnl = nltk.WordNetLemmatizer()
wordlist = nltk.corpus.words.words()
fileName = 'error.txt'
try:
    print('Opening', fileName)
    f = open(fileName)
except:
    print('Cannot open', fileName)
else:
    text = f.read()
    print('Detecting errors:')
    sents = nltk.sent_tokenize(text)
    for sent in sents:  
        words = nltk.word_tokenize(sent)
        tagged_words = nltk.pos_tag(words)
        curTags = ['<tag>', '<tag>', '<tag>']
        curWTags = ['<tag>', '<tag>', '<tag>']
        #print sentences
        print(sent)
    
        if CapError(sent):
            print('**Capitalization error:', words[0])
        
        if FragError(tagged_words):
            print('**Fragment error')
        
        for tagged_word in tagged_words:
            curWord = tagged_word[0]
            curPOS = tagged_word[1]
            curTags.pop(0)
            curTags.append(curPOS) 
            curWTags.pop(0)
            curWTags.append(curWord)
        
            if hasModalError(curTags):
                print('**Verb form error:', curWord)
        
        
            if SubjVError(curTags, curWTags):
                print('**Subject-verb agreement error:', curWord)
        

            if SpellError(curWord, curPOS):
                print('** Spelling error:', curWord)

        f.close()
finally:
    print('--End of error detection--')


# In[ ]:




