#!/usr/bin/python
#encoding:utf-8
from numpy import *
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problem', 'help', 'please'] ,
                                ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                                ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                                ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                                ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                                ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]  #1代表侮辱性文字，0代表正常言论
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
'''
参数：
trainMatrix：所有文档的使用词语信息，将每一个文档对应的01list组成新的List
trainCategory:是所有文档对应的类别，例如前面的classVec
'''
def trainNB0(trainMatrix, trainCategory):
    '''
    求出P(C1)（表示的是类型1的文档在所有文档中的比例）
    '''
    numAllDoc = len( trainMatrix )
    pC1 = sum( trainCategory )/float( numAllDoc)
    '''
    求出条件概率，即在条件C1下的每一个特征出现的概率
    在C0条件下每一个特征出现的概率
    '''
    numWords = len ( trainMatrix[0] ) #得到一共有多少特征
    p0Num = zeros ( numWords )
    p1Num = zeros ( numWords )
    p0All = 0.0 #文档0所有出现的单词总数
    p1All = 0.0 
    for i in range(numAllDoc):
        if trainCategory [ i ] == 1:  #表示该文档属于类型1
            p1Num += trainMatrix [ i ]
            p1All += sum( trainMatrix[ i ] )
        else:
            p0Num += trainMatrix[ i ]
            p0All += sum( trainMatrix[ i ] )
    p0 = p0Num / p0All
    p1 = p1Num / p1All
    return pC1, p0, p1
            
    