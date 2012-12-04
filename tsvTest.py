# Create a table of squares and square roots import math
start, stop, step = 1914, 1941, 1 
delimiter = '\t'
filenameSplit = 'test1.tsv'
filenameSum = 'test2.tsv'
date, diaries, essays, letters, fiction, total = [], [], [], [], [], []

for val in range(start, stop+1, step): 
	date.append(val)

	#replace with actual results
	diariesRatio = 1
	essaysRatio = 2
	lettersRatio = 3
	fictionRatio = 3

	diaries.append(diariesRatio) 
	essays.append(essaysRatio)
	letters.append(lettersRatio)
	fiction.append(fictionRatio)
	total.append(diariesRatio+essaysRatio+lettersRatio+fictionRatio)

# Save  SPLITS to a delimited text file
fout = open(filenameSplit, 'w')
hdr = 'Date%sDiaries%sEssays%sLetters%sFiction\n' % (delimiter, delimiter, delimiter, delimiter) 
print hdr
fout.write(hdr)
for row in zip(date, diaries, essays, letters, fiction):   #make a float ...  2.4f
	total
	line = '%d%s%d%s%d%s%d%s%d\n' % \
 		(row[0], delimiter, row[1], delimiter, row[2], delimiter, row[3], delimiter, row[4])
	print line
	fout.write(line) 
fout.close()


# Save SUM to a delimited text file
fout = open(filenameSum, 'w')
hdr = 'Date%sSum\n' % (delimiter) 
print hdr
fout.write(hdr)
for row in zip(date, total):
	line = '%d%s%d\n' % \
		(row[0], delimiter, row[1])
	print line
	fout.write(line) 
fout.close()