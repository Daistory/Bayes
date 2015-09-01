#!/usr/bin/python
#encoding:utf-8
from numpy import DataSource
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'] ,
                                ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                                ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                                ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                                ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                                ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1]  #1代表侮辱性文字，0代表正常言论
    return postingList, classVec
def createVocabList(dataSet):  #就是将数据中的特征提取出来不重复
    vocabset = []
    for vec in dataSet:
        for i in vec:
            vocabset.append(i)
    vocabset = set(vocabset)  #将set类型的数据转换成List类型
    return list(vocabset)
def setOfWords(vocabList, inputSet): #判断得到的特征List里对应元素是否出现在一个文档之中，1表示出现，0表示没有出现
    vecWords = []
    num = len ( vocabList)
    for i in range(num):
        vecWords.append(0)
    for a in inputSet:
        if a in  vocabList:
            vecWords[ vocabList.index(a) ] = 1
        else:
            print "the word:%s is not in my vocabulary!" %a
    return vecWords
