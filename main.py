#!/usr/bin/python
#encoding:utf-8
import bayes
from numpy import *
postingList , classList = bayes.loadDataSet()
myVocabList = bayes.createVocabList(postingList)
trainMat = []
for a in postingList:
    trainMat.append( bayes.setOfWords( myVocabList, a ) )
pc, p0, p1 = bayes.trainNB0(trainMat, classList)
test = ['stupid', 'garbage']
thisDoc = array( bayes.setOfWords( myVocabList, test ) )
print bayes.classifyNB(thisDoc, p0, p1, pc)