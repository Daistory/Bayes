#!/usr/bin/python
#encoding:utf-8
import re
def getWordVec(fileName):
    # fileName是保存文档的文件具体的位置;
    testString = open( fileName ).read()
    wordVec = re.split( r'\w*', testString )
    # 由于单词长度小于2的时候可能是a，an等没有具体含义的词所有要求只保留长度大于2的单词
    return [ tok.lower() for tok in wordVec if len( tok ) > 2 ]
    