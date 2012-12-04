# coding: utf-8
import re
import random
from random import randint

#========================== DATA  ==============
#====================================================
diaries  = [
	'''diariesV1.txt''',
	'''diariesV2.txt''',
	'''diariesV3.txt''',
	'''diariesV4.txt''',
	'''diariesV5.txt'''
] #format : year\n

essays = [
	'''essaysV1.txt''',
	'''essaysV2.txt''',
	'''essaysV3.txt''',
	'''essaysV4.txt''',
	'''essaysV5.txt'''
] #take from completed not edited - format: year\n

letters = [
	'''LettersV1.txt''',
	'''LettersV2.txt''',
	'''LettersV3.txt''',
	'''LettersV4.txt''',
	'''LettersV5.txt''',
	'''LettersV6.txt''',
] #format = year]\n

fiction = [
	'''aRoomOfOnesOwn.txt''',
	'''betweenTheActs.txt''',
	'''flush.txt''',
	'''jacobsRoom.txt''',
	'''mrsDalloway.txt''',
	'''nightAndDay.txt''',
	'''orlando.txt''',
	'''passionateApprentice.txt''',
	'''theYears.txt''',
	'''threeGuineas.txt''',
	'''toTheLighthouse.txt''',
	'''voyageOut.txt'''
]  #hand code in the years using map below


fictionMap = {
	'''aRoomOfOnesOwn.txt''':1929,
	'''betweenTheActs.txt''': 1941,
	'''flush.txt''':1933,
	'''jacobsRoom.txt''':1922,
	'''mrsDalloway.txt''':1925,
	'''nightAndDay.txt''':1919,
	'''orlando.txt''':1928,
	'''passionateApprentice.txt''':1903,
	'''theYears.txt''':1937,
	'''threeGuineas.txt''':1938,
	'''toTheLighthouse.txt''':1927,
	'''voyageOut.txt''':1915
} #nb. gave Passionate apprentice vague publication date (1897–1909 so took the middle: 1903)










#====================== PROGRAM EXECUTION  ==============
#====================================================
query = "war"

print "Looking for ** '" +query + "'  **"

#===========
# format is going to be a map of maps: genre => {date => [count, [...,examples,...] ]}
# Then to populate the files: keep track of the earliest and latest date found in each genre.
#===========
fullMap = {'diaries': {}, 'essays': {}, 'letters': {}, 'fiction': {}}
earliestDate = 2012
latestDate = 0


#========================== SEARCH  ==============

#====================================================
# ========  Search diaries
print "---Diaries---"
currYear = 0
count = 0
genre = "diaries"
for filename in diaries:
	#print "reading", filename
	file = open('./editedTXTFiles/diaries/'+filename)
	for line in file:
		line = line.strip()   #strips leading and trailing whitespace
		#see if it is a new year and update accordingly
		if len(line) == 4 and line.isdigit():
			if int(line) != currYear:    #only reset count if new year
				count = 0
				currYear = int(line)	
			#reset for each new year

		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			strippedToken = re.sub(r'[^a-z]', '', strippedToken)
			if (strippedToken == query):  #JACKPOT!!!
				count += 1
				lineArr = [line]
				if currYear in fullMap[genre]:
					lineArr = lineArr + fullMap[genre][currYear][1]
				fullMap[genre][currYear] = [count, lineArr]  #add to map if not in, or update

				if (int(currYear)<earliestDate):	#is this the earliest year???
					earliestDate = int(currYear)
#finished looping through all in this genre
if (int(currYear)>latestDate):	#is this the latest year so far???
	latestDate = int(currYear)
#print fullMap[genre]



#====================================================
# ========  Search essays
print "---Essays---"
currYear = 0
count = 0
genre = "essays"
for filename in essays:
	#print "reading", filename
	file = open('./completedTXTFiles/essays/'+filename)
	for line in file:
		line = line.strip()   #strips leading and trailing whitespace
		#see if it is a new year and update accordingly
		if len(line) == 4 and line.isdigit():
			if int(line) != currYear:    #only reset count if new year
				count = 0
				currYear = int(line)	
			#reset for each new year

		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			strippedToken = re.sub(r'[^a-z]', '', strippedToken)
			if (strippedToken == query):  #JACKPOT!!!
				count += 1
				lineArr = [line]
				if currYear in fullMap[genre]:
					lineArr = lineArr + fullMap[genre][currYear][1]
				fullMap[genre][currYear] = [count, lineArr]  #add to map if not in, or update

				if (int(currYear)<earliestDate):	#is this the earliest year???
					earliestDate = int(currYear)
#finished looping through all in this genre
if (int(currYear)>latestDate):	#is this the latest year so far???
	latestDate = int(currYear)
#print fullMap[genre]



#====================================================
# ========  Search letters
print "---Letters---"
currYear = 1888
count = 0
genre = "letters"
for filename in letters:
	#print "reading", filename
	file = open('./editedTXTFiles/letters/'+filename)
	for line in file:
		line = line.strip()   #strips leading and trailing whitespace
		#see if it is a new year and update accordingly
		matchYear = re.findall(r'\d{4}]$', line)
		if matchYear:                                #actually found a date of the right format
		 	thisYear = matchYear[0].strip(']') 
			if int(thisYear) != currYear:                 #only reset count if new year
				count = 0
				currYear = int(thisYear)	

		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			strippedToken = re.sub(r'[^a-z]', '', strippedToken)
			if (strippedToken == query):  #JACKPOT!!!
				count += 1
				lineArr = [line]
				if currYear in fullMap[genre]:
					lineArr = lineArr + fullMap[genre][currYear][1]
				fullMap[genre][currYear] = [count, lineArr]  #add to map if not in, or update

				if (int(currYear)<earliestDate):	#is this the earliest year???
					earliestDate = int(currYear)
#finished looping through all in this genre
if (int(currYear)>latestDate):	#is this the latest year so far???
	latestDate = int(currYear)
#print fullMap[genre]





#====================================================
# ========  Search fiction
print "---Fiction---"
genre = "fiction"
for filename in fiction: 
	currYear = fictionMap[filename] 	#for each new fiction, reset the year and count!
	count = 0
	file = open('./editedTXTFiles/fiction/'+filename)
	for line in file:
		line = line.strip()   #strips leading and trailing whitespace
		tokens = line.split(' ')   #get each word
		for i in range(0,len(tokens)):  #for each word
			strippedToken = tokens[i].strip().lower()
			strippedToken = re.sub(r'[^a-z]', '', strippedToken)
			if (strippedToken == query):  #JACKPOT!!!
				count += 1
				lineArr = [line]
				if currYear in fullMap[genre]:
					lineArr = lineArr + fullMap[genre][currYear][1]
				fullMap[genre][currYear] = [count, lineArr]  #add to map if not in, or update

				#also add in the example...
				if (int(currYear)<earliestDate):	#is this the earliest year???
					earliestDate = int(currYear)
#finished looping through all in this genre
if (int(currYear)>latestDate):	#is this the latest year so far???
	latestDate = int(currYear)

#print fullMap[genre]





##============ Get the lines for the text box ===============
#=========================================================

#If you are looking at the sum graph
randGenre = random.choice(list(fullMap.keys()))
randGenreMap = fullMap[randGenre]
randDate = random.choice(list(randGenreMap.keys()))
randDateArr = randGenreMap[randDate]
arrIndex = randint(0,(len(randDateArr[1])-1))
randLine = randDateArr[1][arrIndex]
print randLine           #THIS IS THE RANDOM LINE FOR THE TEXT BOX

#THIS IS THE RANDOM LINE FOR THE TEXT BOX
titleMap = {
	'''aRoomOfOnesOwn.txt''':"A Room of One's Own",
	'''betweenTheActs.txt''': "Between the Acts",
	'''flush.txt''':"Flush",
	'''jacobsRoom.txt''':"Jacob's Room",
	'''mrsDalloway.txt''':"Mrs Dalloway",
	'''nightAndDay.txt''':"Night and Day",
	'''orlando.txt''':"Orlando",
	'''passionateApprentice.txt''':"A Passionate Apprentice",
	'''theYears.txt''':"The Years",
	'''threeGuineas.txt''':"Three Guineas",
	'''toTheLighthouse.txt''':"To The Lighthouse",
	'''voyageOut.txt''':"Voyage Out"
} 



if (randGenre == 'fiction'):
	for key in list(fictionMap.keys()):
		if fictionMap[key] == randDate:
			print "--- From Woolf's '" + titleMap[key] + "' in " + str(randDate) #For context 
else:
	print "--- From Woolf's '" + randGenre + "' in " + str(randDate) #For context


#What if they want the next one?
	# - generate a new random line


#What if they want to see more? - We search through and return prev and next
prevLine = ""
gotIt = False
prevText = ""
nextText=""

if randGenre == 'diaries':
	for filename in diaries:
		if gotIt != True:
			file = open('./editedTXTFiles/diaries/'+filename)
			for line in file:
				if gotIt:
					prevText = prevLine
					nextText = line + " " + file.next()
					break
				else:
					line = line.strip()
					if line == randLine:
						gotIt = True
					else:
						prevLine = line


elif randGenre == 'essays':
	for filename in essays:
		if gotIt != True:
			#print "reading", filename
			file = open('./completedTXTFiles/essays/'+filename)
			for line in file:
				if gotIt:
					#print "Here it is : ........."
					#print prevLine + " ************ " + randLine + " ************ " +line+ " &&&&&&&&&&&&&"+file.next()
					prevText = prevLine
					nextText = line + " " + file.next()
					break
				else:
					line = line.strip()
					if line == randLine:
						print "-- Got it!! -- essays"
						gotIt = True
					else:
						prevLine = line


elif randGenre == 'letters':
	for filename in letters:
		if gotIt != True:
			#print "reading", filename
			file = open('./editedTXTFiles/letters/'+filename)
			for line in file:
				if gotIt:
					#print "Here it is : ........."
					#print prevLine + " ************ " + randLine + " ************ " +line+ " &&&&&&&&&&&&&"+file.next()
					prevText = prevLine
					nextText = line + " " + file.next()
					break
				else:
					line = line.strip()
					if line == randLine:
						print "-- Got it!! -- letters"
						gotIt = True
					else:
						prevLine = line


elif randGenre == 'fiction':
	for filename in fiction:
		if gotIt != True:
			#print "reading", filename
			file = open('./editedTXTFiles/fiction/'+filename)
			for line in file:
				if gotIt:
					#print "Here it is : ........."
					#print prevLine + " ************ " + randLine + " ************ " +line+ " &&&&&&&&&&&&&"+file.next()
					prevText = prevLine
					nextText = line + " " + file.next()
					break
				else:
					line = line.strip()
					if line == randLine:
						print "-- Got it!! -- fiction"
						gotIt = True
					else:
						prevLine = line





#===================== POPULATE TSV's  ===================
#=========================================================
# Reminder: # format of fullMap: genre => {date => [count, [...,examples,...] ]}


#set the range
start, stop, step = int(earliestDate), int(latestDate), 1 
delimiter = '\t'
filenameSplit = 'split.tsv'
filenameSum = 'sum.tsv'
date, diaries, essays, letters, fiction, total = [], [], [], [], [], []

for val in range(start, stop+1, step): 
	date.append(val)

	if val in fullMap['diaries']:
		diariesRatio = int(fullMap['diaries'][val][0])     #will have to adjust if [count, example]
	else:
		diariesRatio = 0

	if val in fullMap['essays']:
		essaysRatio = int(fullMap['essays'][val][0])     #will have to adjust if [count, example]
	else:
		essaysRatio = 0

	if val in fullMap['letters']:
		lettersRatio = int(fullMap['letters'][val][0])     #will have to adjust if [count, example]
	else:
		lettersRatio = 0

	if val in fullMap['fiction']:
		fictionRatio = int(fullMap['fiction'][val][0])     #will have to adjust if [count, example]
	else:
		fictionRatio = 0

	diaries.append(diariesRatio) 
	essays.append(essaysRatio)
	letters.append(lettersRatio)
	fiction.append(fictionRatio)
	total.append(diariesRatio+essaysRatio+lettersRatio+fictionRatio)

# Save  SPLITS to a delimited text file
fout = open(filenameSplit, 'w')
hdr = 'Date%sDiaries%sEssays%sLetters%sFiction\n' % (delimiter, delimiter, delimiter, delimiter) 
#print hdr
fout.write(hdr)
for row in zip(date, diaries, essays, letters, fiction):   #make a float ...  2.4f
	total
	line = '%d%s%d%s%d%s%d%s%d\n' % \
 		(row[0], delimiter, row[1], delimiter, row[2], delimiter, row[3], delimiter, row[4])
	#print line
	fout.write(line) 
fout.close()


# Save SUM to a delimited text file
fout = open(filenameSum, 'w')
hdr = 'Date%sSum\n' % (delimiter) 
#print hdr
fout.write(hdr)
for row in zip(date, total):
	line = '%d%s%d\n' % \
		(row[0], delimiter, row[1])
	#print line
	fout.write(line) 
fout.close()

