from collections import defaultdict

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

def computeIDF(N,idfDict):
    import math
    '''idfDict = dict.fromkeys(documents[0].keys(), 0)
                for document in documents:
                    for word, val in document.items():
                        if val > 0:
                            idfDict[word] += 1'''
    
    for word, val in idfDict.items():
        idfDict[word] = math.log(N / float(val))
    return idfDict

def computeTFIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items():
        tfidf[word] = val * idfs[word]
    return tfidf

def dictSort(dic):
    l1=defaultdict(list)

    for k, v in dic.items():
        l1[v].append(k)

    sor={}
    for k, v in sorted(l1.items(), reverse=True):
        sor[int(k)] = v[0]
        print(k, ', '.join(v))

    return sor
