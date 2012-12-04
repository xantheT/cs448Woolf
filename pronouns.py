# coding: utf-8
from __future__ import division
import re
import pickle
import math
import operator

inFile =open("./editedTXTFiles/fiction/aRoomOfOnesOwn.txt","r")

words = []
count = []
wordMap = {}
threshold = 20
MAX = 150


#pronouns taken from here: http://en.wikipedia.org/wiki/English_personal_pronouns
#first
	#sing
firstS =['i', 'me', 'myself', 'mine', 'my', 'mine', 'me']
	#plural
firstP = ['we', 'us', 'ourselves', 'ourself', 'ours', 'our']
#second
	#sing
secondS = ['you', 'yourself', 'yours', 'your']
	#plural
secondP = ['you', 'yourselves', 'yours', 'your']
#third
	#sing
		#masc. 
thirdSM = ['he', 'him', 'himself', 'hisself', 'his']
		#fem
thirdSF = ['she', 'her', 'herself','hers']
		#neut
thirdSN = ['it', 'it', 'itself', 'its', 'themself', 'theirself', 'one', 'oneself', "one's"] 
																			#nb. careful of one! Not always used as a pronoun.
	#plural
thirdP = ['they', 'them', 'themselves', 'theirselves', 'theirs', 'their']

pronounMap = {'first': {'sing':0, 'plural':0}, 'second':{'sing':0, 'plural':0}, 'third':{'sing':{'masc':0, 'fem':0, 'neut':0}, 'plural':0} }



def constructMaps(inFile, pMap):
	for line in inFile:
		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			if strippedToken in firstS:
				(pMap['first'])['sing'] +=1
			elif strippedToken in firstP:
				(pMap['first'])['plural'] +=1
			elif strippedToken in secondS:
				(pMap['second'])['sing'] +=1
			elif strippedToken in secondP:
				(pMap['second'])['plural'] +=1
			elif strippedToken in thirdSM:
				((pMap['third'])['sing'])['masc'] +=1
			elif strippedToken in thirdSF:
				((pMap['third'])['sing'])['fem'] +=1
			elif strippedToken in thirdSN:
				((pMap['third'])['sing'])['neut'] +=1
			elif strippedToken in thirdP:
				(pMap['third'])['plural'] +=1	
	return pMap

def makePersonMap(inFile, keepList, wordMap):
	for line in inFile:
		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			strippedToken = re.sub(r'[^a-z]', '', strippedToken)
			if ((strippedToken !=  '') and (strippedToken in keepList) ):
				if strippedToken in wordMap:
					wordMap[strippedToken] += 1
				else:
					wordMap[strippedToken] = 1
	return wordMap
		

def removeInsignificantWords(wordMap, threshold):
	toDel = []
	newMap = wordMap
	for key in wordMap:
		if wordMap[key] < threshold:
			toDel.append(key)
	for i in toDel:
		del newMap[i]
	return newMap

def sortList(wordMap):
	sortedList = sorted(wordMap.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedList

def normalizeOverFile(wordMap):
	total = sum(wordMap.itervalues())
	normMap = {}
	for key in wordMap:
		normMap[key] = (wordMap[key] / total)*10000
	return normMap

def getLog(wordMap):
	logMap = {}
	for key in wordMap:
		logMap[key] = math.log(1+ wordMap[key])
	return logMap



def writeListToFiles(writeFileWords, writeFileCount, slist, count):
	writeFileWords.write('[')
	writeFileCount.write('[')
	for i in range(0,count):
		writeFileWords.write("'")
		writeFileCount.write("'")

		writeFileWords.write(slist[i][0])
		writeFileCount.write(str(slist[i][1]))

		writeFileWords.write("'")
		writeFileCount.write("'")

		writeFileWords.write(', ')
		writeFileCount.write(', ')
	writeFileWords.write(']')
	writeFileCount.write(']')


#======== execution of Program ==========

#Constructs a basic frequency stuff and exports to files
wordMap = constructMaps(inFile, pronounMap)
print wordMap
outfileWords = open("./splitText/aRoomOfOnesOwn_pronounW.txt", "w")
outfileCount = open("./splitText/aRoomOfOnesOwn_pronounC.txt", "w")
#sortedList = sortList(wordMap)
#writeListToFiles(outfileWords, outfileCount, sortedList, MAX)


# base
#


 #{ label: 'Aggressive', pct: [30, 10, 6, 30, 14, 10] },
