# coding: utf-8
from __future__ import division
import re
import pickle
import math
import operator

inFile =open("./editedTXTFiles/essays/essaysV5.txt","r")

words = []
count = []
wordMap = {}
threshold = 20
MAX = 150


#pronouns taken from here: http://en.wikipedia.org/wiki/English_personal_pronouns
#first
	#sing
firstS =['i', 'me', 'myself', 'mine', 'my']
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

pronounMap = {'first': {'sing':0, 'plural':0}, 'second':{'any':0}, 'third':{'sing':{'masc':0, 'fem':0, 'neut':0}, 'plural':0} }



def constructMaps(inFile, pMap):
	for line in inFile:
		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			if strippedToken in firstS:
				(pMap['first'])['sing'] +=1
			if strippedToken in firstP:
				(pMap['first'])['plural'] +=1
			if (strippedToken in secondS) or (strippedToken in secondP):
				(pMap['second'])['any'] +=1
			if strippedToken in thirdSM:
				((pMap['third'])['sing'])['masc'] +=1
			if strippedToken in thirdSF:
				((pMap['third'])['sing'])['fem'] +=1
			if strippedToken in thirdSN:
				((pMap['third'])['sing'])['neut'] +=1
			if strippedToken in thirdP:
				(pMap['third'])['plural'] +=1
	return pMap


# { label: 'basic' pct: [first, second, third]}
# { label: 'sp' pct: [firstSing, firstPlu, secondSing, secondPlu, thirdSing, thirdPlu]}
# { label: 'spmf' pct: [firstSing, firstPlu, secondSing, secondPlu, thirdSingM, thirdSingF, thirdSingN, thirdPlu]}
def makeSummedMaps(pMap):
	firstMap = pMap['first']
	firstTotal = sum(firstMap.itervalues())
	secondMap = pMap['second']
	secondTotal = sum(secondMap.itervalues())
	thirdMap = pMap['third']
	thirdSingMap = thirdMap['sing']
	thirdSingTotal = sum(thirdSingMap.itervalues())

	basicMap = {'label': 'basic', 'pct':[firstTotal, 0,0,(secondTotal),0,(thirdSingTotal + thirdMap['plural']),0,0,0,0,0]}

	sp = {'label': 'singAndPlural', 'pct':[0,firstMap['sing'], firstMap['plural'], 0,(secondTotal), 0,thirdSingTotal, 0,0,0,thirdMap['plural']]}

	spmf = { 'label': 'singPluralMascFem', 'pct': [0,firstMap['sing'], firstMap['plural'], 0,(secondTotal), 0,0,thirdSingMap['masc'], thirdSingMap['fem'], thirdSingMap['neut'], thirdMap['plural']]}
	
	return [basicMap, sp, spmf]



def writeToFiles(writeFile, arr):
	writeFile.write(str(arr[0]))
	writeFile.write("\n")
	writeFile.write(str(arr[1]))
	writeFile.write("\n")
	writeFile.write(str(arr[2]))


#======== execution of Program ==========

#Constructs a basic frequency stuff and exports to files
pMap = constructMaps(inFile, pronounMap)
fullArr = makeSummedMaps(pMap)

outfile = open("./splitText/essaysV5/essaysV5_pronouns.txt", "w")
writeToFiles(outfile, fullArr)


# base
# { label: 'basic' pct: [first, second, third]}
# { label: 'sp' pct: [firstSing, firstPlu, secondSing, secondPlu, thirdSing, thirdPlu]}
# { label: 'spmf' pct: [firstSing, firstPlu, secondSing, secondPlu, thirdSingM, thirdSingF, thirdSingN, thirdPlu]}

 #{ label: 'Aggressive', pct: [30, 10, 6, 30, 14, 10] },
