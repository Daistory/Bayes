#!/usr/bin/python
#encoding:utf-8
import bayes
postingList , classList = bayes.loadDataSet()
myVocabList = bayes.createVocabList(postingList)
trainMat = []
for a in postingList:
    trainMat.append( bayes.setOfWords( myVocabList, a ) )
pc, p0, p1 = bayes.trainNB0(trainMat, classList)
print pc
print p0
print p1