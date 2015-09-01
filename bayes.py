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
'''
将所有的文档中出现的特征合并，并且去掉其中重复的部分，最后并转换成List类型
'''
def createVocabList(dataSet):
    vocabset = []
    for vec in dataSet:
        for i in vec:
            vocabset.append(i)
    vocabset = set(vocabset)  #将set类型的数据转换成List类型
    return list(vocabset)
'''
判断得到的特征List里对应元素是否出现在一个文档之中，1表示出现，0表示没有出现
得到特征值在不同文档里面是否出现
'''
def setOfWords(vocabList, inputSet): 
    vecWords = []
    num = len ( vocabList)
    for i in range(num):
        vecWords.append(0)
    for a in inputSet:
        if a in  vocabList:
            vecWords[ vocabList.index(a) ] += 1
        else:
            print "the word:%s is not in my vocabulary!" %a
    return vecWords
'''
参数：
trainMatrix：所有文档的使用词语信息，将每一个文档对应的01list组成新的List
trainCategory:是所有文档对应的类别，例如前面的classVec
得到不同类情况下不同特征对应的概率
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
    '''
    为了避免出现因为一个概率值为零的时候几个概率乘积也是零，则分子最小是1,分母2
    '''
    p0Num = ones( numWords )#zeros ( numWords )
    p1Num = ones( numWords ) #zeros ( numWords )
    p0All = 2.0 #文档0所有出现的单词总数
    p1All = 2.0 
    for i in range(numAllDoc):
        if trainCategory [ i ] == 1:  #表示该文档属于类型1
            p1Num += trainMatrix [ i ]
            p1All += sum( trainMatrix[ i ] )
        else:
            p0Num += trainMatrix[ i ]
            p0All += sum( trainMatrix[ i ] )
    '''
    为了避免几个极小的数相乘最后得到下溢的结果成为0,利用自然对数log(f(x))和f(x)有相同的极值情况，和相同的增减变化，虽然大小不同也可以忽略影响
    p0 = p0Num / p0All
    p1 = p1Num / p1All
    '''
    p0 = log( p0Num / p0All )
    p1 =log(  p1Num / p1All )
    return pC1, p0, p1
'''
参数，vecClassify:类型array,需要划分的文文本信息
p0:表示的是在对已知的文本进行学习得到的每一个不同特征值对应0类时候的出现概率
p1:表示的是在对已知的文本进行学习得到的每一个不同特征值对应1类时候的出现概率
pC1:表示的是在文本中1类出现的概率
'''
def classifyNB(vecClassify, p0, p1, pC1):
    pA = sum( vecClassify * p0 )  + log( 1 - pC1 )
    pB = sum( vecClassify * p1 )  + log( pC1 )
    if pA < pB:
        return 1
    else:
        return 0