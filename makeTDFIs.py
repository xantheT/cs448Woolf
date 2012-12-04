# coding: utf-8
from __future__ import division
import re
import pickle
import math

stopList = []


def writeTFIDF(arr, outfile):
	for word in arr:
		outfile.write(word)
		outfile.write(" ")

def cleanText(inFile):
	textArr= []
	for line in inFile:
		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			strippedToken = re.sub(r'[^a-z]', '', strippedToken)   #allow 0-9???
			if ((strippedToken !=  '') and (strippedToken not in stopList) ):
				textArr.append(strippedToken)
	return textArr


def outputCleanFile(infile, outfile):
	cleanArr = cleanText(infile)
	writeTFIDF(cleanArr, outfile)


#======== execution of Program ==========

#output for all other texts
infile1 = open("./editedTXTFiles/essays/essaysV1.txt","r")
outfile1 = open("./cleanedText/essaysV1_TFIDF.txt", "w")
outputCleanFile(infile1, outfile1)
infile1.close();
outfile1.close();

#done:
#diaries1

#essays1

#Room of one's own
