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







#============= 'DECOMPOSED' FUNCTIONS  ==============
#====================================================


def searchCorpus(query):
	##print "Looking for ** '" +query + "'  **"

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
	#print "---Diaries---"
	currYear = 0
	count = 0
	genre = "diaries"
	for filename in diaries:
		##print "reading", filename
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
	##print fullMap[genre]



	#====================================================
	# ========  Search essays
	#print "---Essays---"
	currYear = 0
	count = 0
	genre = "essays"
	for filename in essays:
		##print "reading", filename
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
	##print fullMap[genre]



	#====================================================
	# ========  Search letters
	#print "---Letters---"
	currYear = 1888
	count = 0
	genre = "letters"
	for filename in letters:
		##print "reading", filename
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
	##print fullMap[genre]





	#====================================================
	# ========  Search fiction
	#print "---Fiction---"
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

	##print fullMap[genre]
	return [fullMap, earliestDate, latestDate]



##============ Get the lines for the text box ===============
#=========================================================
def generateRandomText(fullMap):
	randGenre = random.choice(list(fullMap.keys()))
	randGenreMap = fullMap[randGenre]
	if (len(randGenreMap)==0):    # oh no, we picked a genre without any results in it
		foundAGenre = False
		for key in list(fullMap.keys()):  #look at each genre once
			randGenreMap = fullMap[key]
			if (len(randGenreMap)!=0):   #if we found a genre with results in it
				foundAGenre = True		
				break
		if (foundAGenre ==False): #looped through and still found nothing
			return ["Could not find any occurences of your search query in the corpus", "", "", "", ""]

	randDate = random.choice(list(randGenreMap.keys()))
	randDateArr = randGenreMap[randDate]
	arrIndex = randint(0,(len(randDateArr[1])-1))
	randLine = randDateArr[1][arrIndex]
	#print randLine            #THIS IS THE RANDOM LINE FOR THE TEXT BOX


	if (randGenre == 'fiction'):
		for key in list(fictionMap.keys()):
			if fictionMap[key] == randDate:
				#print "--- From Woolf's '" + titleMap[key] + "' in " + str(randDate) #For context
				fromText = "the book '" + titleMap[key] +"'" 
	elif(randGenre == 'diaries'):
		#print "--- From Woolf's '" + randGenre + "' in " + str(randDate) #For context
		fromText = "a diary entry"
	elif(randGenre == 'letters'):
		#print "--- From Woolf's '" + randGenre + "' in " + str(randDate) #For context
		fromText = "a letter written"
	elif(randGenre == 'essays'):
		#print "--- From Woolf's '" + randGenre + "' in " + str(randDate) #For context
		fromText = "an essay written"


	##======= Now get the prev and next bits of the random line =======
	#=========================================================
	prevLine = ""
	gotIt = False
	prevText = ""
	nextText = ""

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
				##print "reading", filename
				file = open('./completedTXTFiles/essays/'+filename)
				for line in file:
					if gotIt:
						##print "Here it is : ........."
						##print prevLine + " ************ " + randLine + " ************ " +line+ " &&&&&&&&&&&&&"+file.next()
						prevText = prevLine
						nextText = line + " " + file.next()
						break
					else:
						line = line.strip()
						if line == randLine:
							#print "-- Got it!! -- essays"
							gotIt = True
						else:
							prevLine = line


	elif randGenre == 'letters':
		for filename in letters:
			if gotIt != True:
				##print "reading", filename
				file = open('./editedTXTFiles/letters/'+filename)
				for line in file:
					if gotIt:
						##print "Here it is : ........."
						##print prevLine + " ************ " + randLine + " ************ " +line+ " &&&&&&&&&&&&&"+file.next()
						prevText = prevLine
						nextText = line + " " + file.next()
						break
					else:
						line = line.strip()
						if line == randLine:
							#print "-- Got it!! -- letters"
							gotIt = True
						else:
							prevLine = line


	elif randGenre == 'fiction':
		for filename in fiction:
			if gotIt != True:
				##print "reading", filename
				file = open('./editedTXTFiles/fiction/'+filename)
				for line in file:
					if gotIt:
						##print "Here it is : ........."
						##print prevLine + " ************ " + randLine + " ************ " +line+ " &&&&&&&&&&&&&"+file.next()
						prevText = prevLine
						nextText = line + " " + file.next()
						break
					else:
						line = line.strip()
						if line == randLine:
							#print "-- Got it!! -- fiction"
							gotIt = True
						else:
							prevLine = line

	return [randLine, fromText, str(randDate), prevText, nextText]




#===================== POPULATE TSV's  ===================
#=========================================================
# Reminder: # format of fullMap: genre => {date => [count, [...,examples,...] ]}

def generateTSVs(filenameSplit, filenameSum, resultsArr):
	fullMap = resultsArr[0]
	earliestDate = resultsArr[1]
	latestDate = resultsArr[2]

	#set the range
	start, stop, step = int(earliestDate), int(latestDate), 1 
	delimiter = '\t'
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
	##print hdr
	fout.write(hdr)
	for row in zip(date, diaries, essays, letters, fiction):   #make a float ...  2.4f
		total
		line = '%d%s%d%s%d%s%d%s%d\n' % \
	 		(row[0], delimiter, row[1], delimiter, row[2], delimiter, row[3], delimiter, row[4])
		##print line
		fout.write(line) 
	fout.close()


	# Save SUM to a delimited text file
	fout = open(filenameSum, 'w')
	hdr = 'Date%sSum\n' % (delimiter) 
	##print hdr
	fout.write(hdr)
	for row in zip(date, total):
		line = '%d%s%d\n' % \
			(row[0], delimiter, row[1])
		##print line
		fout.write(line) 
	fout.close()


def do_everything_and_give_me_the_RandomArr(query, filenameSplit, filenameSum):
	resultsArr = searchCorpus(query)
	generateTSVs(filenameSplit, filenameSum, resultsArr);
	randomArr = generateRandomText(resultsArr[0])
	return [randomArr, resultsArr[0]]



#######################################################################
# 
# ANDREW, YOU ONLY NEED TO LOOK FROM HERE DOWNWARDS!
#_______________________________________________________________________
#====================== PROGRAM EXECUTION  ==============
#====================================================
# 1. Take a look to understand what each fn is returning
query = "telephone"
filenameSplit = 'split.tsv'
filenameSum = 'sum.tsv'

resultsArr = searchCorpus(query)
#NOTE: the resultsArr is formated as follows (web side of things should not need this though): 
	#resultsArr[0] = the map of the results
	#resultsArr[1] = the earliestDate from the returned results
	#resultsArr[0] = the latestDate from the returned results

#GENERATE_TSVs 
#takes in two filenames & the resultsArr as arguments
generateTSVs(filenameSplit, filenameSum, resultsArr)

#GENERATE RANDOM TEXT
#Take in the resultsMap and return array with the random string at 0th index,
# context for the random string at indices 1 & 2
# and the extra string bits (used if the user clicks 'more') at indices 3 & 4
# FORMAT:
#randomArr[0] = random string for textbox
#randomArr[1] = 'a diary entry'   < or  'the book 'The Voyage Out'' >...etc
#randomArr[2] = '1928'    <a date>
#                 -- Indices [1] & [2] allow us to give context to the random string, 
#                 -- Use as follows: "From randomArr[1] in randomArr[2]"
#randomArr[3] = previous text  <to add to the TOP of the random string is user clicks 'more'>
#randomArr[4] = next text      <to add to the BOTTOM of the random string is user clicks 'more'>
randomArr = generateRandomText(resultsArr[0])
	# NOTE: call this function again 
print "********** _______RANDLINE_____*************"
print str(randomArr[0])
print "***********_____FROM TEXT_____************"
print str(randomArr[1])
print "***********_____DATE_____************"
print str(randomArr[2])
print "***********_____PREV TEXT_____************"
print str(randomArr[3])
print "***********_____NEXT TEXT_____************"
print str(randomArr[4])
print "done first random generation!"


randomArr = generateRandomText(resultsArr[0])              # calling it a second time is trouble
	# NOTE: call this function again 
print "********** _______RANDLINE_____*************"
print str(randomArr[0])
print "***********_____FROM TEXT_____************"
print str(randomArr[1])
print "***********_____DATE_____************"
print str(randomArr[2])
print "***********_____PREV TEXT_____************"
print str(randomArr[3])
print "***********_____NEXT TEXT_____************"
print str(randomArr[4])
print "done second random generation!"

#2. Now you understand it, all you'll need to call when a user enters a query is this:
lazyResultsArr = do_everything_and_give_me_the_RandomArr(query, filenameSplit, filenameSum)
# Returns:
#lazyResultsArr[0] = the random array   (see above)
#lazyResultsArr[1] = the results map 
#    -- (to be used if the user clicks to generate a new random string - just call 'generateRandomText(lazyResultsArr[1])')



# 3. That's it! but...
#-------------- RUN IT AGAIN (if you like)------------------------------------
# SEARCH FN IS REUSABLE
# so we could run diff queries and populate diff files with results, 
# to display two searches on the graph at once
newQuery = "what"
filenameSplit = 'split2.tsv'
filenameSum = 'sum2.tsv'
additionalLazyArr = do_everything_and_give_me_the_RandomArr(query, filenameSplit, filenameSum)
print "********** _______RANDLINE_____*************"
print str(additionalLazyArr[0][0])
print "***********_____FROM TEXT_____************"
print str(additionalLazyArr[0][1])
print "***********_____DATE_____************"
print str(additionalLazyArr[0][2])
print "***********_____PREV TEXT_____************"
print str(additionalLazyArr[0][3])
print "***********_____NEXT TEXT_____************"
print str(additionalLazyArr[0][4])


randomArr = generateRandomText(resultsArr[0])              # calling it a second time is trouble
	# NOTE: call this function again 
print "********** _______RANDLINE_____*************"
print str(randomArr[0])
print "***********_____FROM TEXT_____************"
print str(randomArr[1])
print "***********_____DATE_____************"
print str(randomArr[2])
print "***********_____PREV TEXT_____************"
print str(randomArr[3])
print "***********_____NEXT TEXT_____************"
print str(randomArr[4])
print "--------done first  random generation for second search -------!"

randomArr = generateRandomText(resultsArr[0])              # calling it a second time is trouble
	# NOTE: call this function again 
print "********** _______RANDLINE_____*************"
print str(randomArr[0])
print "***********_____FROM TEXT_____************"
print str(randomArr[1])
print "***********_____DATE_____************"
print str(randomArr[2])
print "***********_____PREV TEXT_____************"
print str(randomArr[3])
print "***********_____NEXT TEXT_____************"
print str(randomArr[4])
print "--------done second  random generation for second search -------!"
