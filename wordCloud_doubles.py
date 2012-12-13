# coding: utf-8
from __future__ import division
import re
import pickle
import math
import operator

inFile =open("./editedTXTFiles/essays/essaysV5.txt","r")

words = []
count = 0
wordMap = {}
threshold = 20
MAX = 150

# From Jonathan Feinberg's cue.language, see lib/cue.language/license.txt.
bigStopList = ['i','me','my','myself','we','us','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves','what','which','who','whom','whose','this','that','these','those','am','is','are','was','were','be','been','being','have','has','had','having','do','does','did','doing','will','would','should','can','could','ought',"i'm","you're","he's","she's","it's","we're","they're","i've","you've","we've","they've","i'd","you'd","he'd","she'd","we'd","they'd","i'll","you'll","he'll","she'll","we'll","they'll","isn't","aren't","wasn't","weren't","hasn't","haven't","hadn't","doesn't","don't","didn't","won't","wouldn't","shan't","shouldn't","can't",'cannot',"couldn't","mustn't","let's","that's","who's","what's","here's","there's","when's","where's","why's","how's",'a','an','the','and','but','if','or','because','as','until','while','of','at','by','for','with','about','against','between','into','through','during','before','after','above','below','to','from','up','upon','down','in','out','on','off','over','under','again','further','then','once','here','there','when','where','why','how','all','any','both','each','few','more','most','other','some','such','no','nor','not','only','own','same','so','than','too','very','say','says','said','shall', 
				'nd', 'o', 'ut','et', 'ofthe', 'rs', 'en', 'll', 'iss','ane',
				'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# added annoying words to the list that crop up a lot - OCR problems
#nb. Alice's suggestion, remove 'I', 'we', 'he', 'him',she', 'her', - instead, maybe make a separate viz for these
personList = ['i','me','my','myself','we','us','our','ours','ourselves','you','your','yours','yourself','yourselves','he','him','his','himself','she','her','hers','herself','it','its','itself','they','them','their','theirs','themselves']



def constructDoubleArrays(inFile, stopList, wordMap, count):
	lastWord = ""
	currWord = ""
	combinedWord = ""
	for line in inFile:
		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			strippedToken = re.sub(r'[^a-z]', '', strippedToken)
			currWord = strippedToken
			combinedWord = lastWord+" "+currWord
			if ((currWord !=  '') and (lastWord !=  '')):
				count +=1 																# 'and' for pairEx (ie, no words in stoplist) but could use 'or' to allow at most one stoplist word in word pair
			if ((currWord !=  '') and (lastWord !=  '') and ((currWord not in stopList) and (lastWord not in stopList)) ): #not rubbish, and not both in stop list
				if combinedWord in wordMap:
					wordMap[combinedWord] += 1
				else:
					wordMap[combinedWord] = 1
			lastWord = currWord
	return {'wordMap': wordMap, 'count':count}




def sortList(wordMap):
	sortedList = sorted(wordMap.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedList

def normalizeOverFile(wordMap, count):
	total = count#total = sum(wordMap.itervalues())
	print count
	print sum(wordMap.itervalues())
	normMap = {}
	for key in wordMap:
		normMap[key] = (wordMap[key] / total)*100000
	return normMap




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
info = constructDoubleArrays(inFile, bigStopList, wordMap, count)
#outfileWords = open("./splitText/jacobsRoom/jacobsRoom_double_Words.txt", "w")
#outfileCount = open("./splitText/jacobsRoom/jacobsRoom_double_Count.txt", "w")
#sortedList = sortList(info['wordMap'])
#writeListToFiles(outfileWords, outfileCount, sortedList, MAX)


#Constructs a normalized frequency and exports to files
outfileNormWords = open("./splitText/essaysV5/essaysV5_double_Norm_Words.txt", "w")
outfileNormCount = open("./splitText/essaysV5/essaysV5_double_Norm_Count.txt", "w")
normMap = normalizeOverFile(info['wordMap'], info['count'])
sortedNorms = sortList(normMap)
writeListToFiles(outfileNormWords, outfileNormCount, sortedNorms,MAX)








# #Constructs a basic frequency stuff and exports to files
# wordMap = constructArrays(inFile, bigStopList, wordMap)
# outfileWords = open("./splitText/jacobsRoom/jacobsRoom_Words.txt", "w")
# outfileCount = open("./splitText/jacobsRoom/jacobsRoom_Count.txt", "w")
# sortedList = sortList(wordMap)
# writeListToFiles(outfileWords, outfileCount, sortedList, MAX)


# #Constructs a normalized frequency and exports to files
# outfileNormWords = open("./splitText/jacobsRoom/jacobsRoom_Norm_Words.txt", "w")
# outfileNormCount = open("./splitText/jacobsRoom/jacobsRoom_Norm_Count.txt", "w")
# normMap = normalizeOverFile(wordMap)
# sortedNorms = sortList(normMap)
# writeListToFiles(outfileNormWords, outfileNormCount, sortedNorms,MAX)

# #Constructs a log frequency and exports to file
# outfileLogWords = open("./splitText/jacobsRoom/jacobsRoom_Log_Words.txt", "w")
# outfileLogCount = open("./splitText/jacobsRoom/jacobsRoom_Log_Count.txt", "w")
# logsMap = getLog(wordMap)
# sortedLogs = sortList(logsMap)
# writeListToFiles(outfileLogWords, outfileLogCount, sortedLogs, MAX)











#OLD STUFF -----------------

#finishedMap = removeInsignificantWords(wordMap, threshold)
#writeToFiles(outfileWords, outfileCount, finishedMap)

# def writeToFiles(writeFileWords, writeFileCount, wordMap):
# 	writeFileWords.write('[')
# 	writeFileCount.write('[')
# 	for key in wordMap:
# 		writeFileWords.write("'")
# 		writeFileCount.write("'")

# 		writeFileWords.write(key)
# 		writeFileCount.write(str(wordMap[key]))

# 		writeFileWords.write("'")
# 		writeFileCount.write("'")

# 		writeFileWords.write(', ')
# 		writeFileCount.write(', ')
# 	writeFileWords.write(']')
# 	writeFileCount.write(']')




#--------------------------------------------------
#finalLists = removeInsignificantWords(words, count)
#writeToFile(outfileWords, finalLists[0])
#writeToFile(outfileCount, finalLists[1])


# outfileWords.write('[')
# for word in words:
# 	outfileWords.write("'")
# 	outfileWords.write(word)
# 	outfileWords.write("'")
# 	outfileWords.write(', ')
# outfileWords.write(']')

# outfileCount.write('[')
# for num in count:
# 	outfileCount.write("'")
# 	outfileCount.write(str(num))
# 	outfileCount.write("'")
# 	outfileCount.write(', ')
# outfileCount.write(']')


#outfileWords.write(words)
#outfileCount.write(count)
#pickle.dump(words, outfileCount)
