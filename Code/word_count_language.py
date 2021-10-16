import  sys,operator
from math import *

# N_t used in tf-idf calculation.
def n_t(languages,word):

	ret = 0
	
	for langdict in languages:

		if word in langdict:
			ret+=1

	return ret



languages = []
lines = 16000
vecsize = 5000

word_lang = {}
# For each language get all the words with frequencies.
with open("train_new.txt",'r') as f:

	seen=0

	for line in f:
		wordslistpre = (line).split()
		wordslistpre = wordslistpre[:-1]

		wordslist = []
		for ww in wordslistpre:
			wordslist.append(ww)


		for word in wordslist:

			if word in word_lang:
				word_lang[word]+=-1
			else:
				word_lang[word]=-1

		seen+=1

		if(seen==lines):
			seen=0
			languages.append(word_lang)
			word_lang = {}

# Sort languages based on the frequencies
sortlanguages = []

for lang in languages:
	sortlanguages.append(sorted(lang.items(), key=operator.itemgetter(1)))

# Choose the top vecsize number of words in each language.
toplanguages = []

for lang in sortlanguages:

	tempdict = {}
	for i in range(0,vecsize):
		tempdict[lang[i][0]] = abs(lang[i][1])

	toplanguages.append(tempdict)


vectorlanguages = []

for lang in toplanguages:

	vector = []
	vectorwords = []

	for x,y in lang.items():
		vector.append(y)
		vectorwords.append(x)

	vectorlanguages.append((vector,vectorwords))


# modify feature values with tf_idf scoring

indexlang = 0
N_langs = 14

while(indexlang<len(vectorlanguages)):

	index=0
	size = len(vectorlanguages[indexlang][1])

	while(index<size):

		word = vectorlanguages[indexlang][1][index]
		temp = n_t(languages,word)
		ft = vectorlanguages[indexlang][0][index]
		vectorlanguages[indexlang][0][index] = log(1+N_langs*1.0/temp)*log(N_langs*1.0/temp)*log(1+ft)

		index+=1

	indexlang+=1


# Writing the model in features.txt
features = open("features.txt",'w')


for item in vectorlanguages:

	for p in item[0]:
		features.write(str(p)+"\n")

	for q in item[1]:
		features.write(q+"\n")

features.close()

dictlist = [dict() for x in range(N_langs)]

for i in range(0,N_langs):

	for tt in range(0,len(vectorlanguages[i][1])):
		(dictlist[i])[vectorlanguages[i][1][tt]] = tt



print("Confusion matrix for N = "+str(vecsize)+"\n")

sys.stdout.write("     ")
for nav in range(0,14):
	sys.stdout.write(str(nav)+"     ")



print("     ")
for i in range(0,14):
	#print(i)
	label = []
	# testing on validation data by forming feature vector for query.
	with open(str(i)+".txt") as f:
		for line in f:


			linewords = (line).split()
			linewords = linewords[:-1]
			maxscore = float("-inf")
			maxlabel = 0
			langnum = 0

			indlang = 0

			for vector in vectorlanguages:

				maxtemp = 0

				templis = []

				for lineword in linewords:

					if lineword in dictlist[indlang]:
						tempindex = dictlist[indlang][lineword]
						templis.append(lineword)
						maxtemp += vector[0][tempindex] 

				maxoflis=0
				for u in templis:
					if(maxoflis < templis.count(u)):
						maxoflis = templis.count(u)
			

				indlang+=1

				# Normalize the frequency
				if(maxoflis!=0):
					maxtemp = maxtemp*0.5/(maxoflis)				

				# Deciding the group by armax among all the languages
				if(maxtemp>maxscore):
					maxscore = maxtemp
					maxlabel = langnum

				langnum+=1

			label.append(maxlabel)

	analysis = {}

	for x in label:

		if x in analysis:
			analysis[x]+=1
		else:
			analysis[x]=1
	
	# Outputs Confusion Matrix
	sys.stdout.write(str(i)+": ")
	for nav in range(0,14):
		if nav in analysis:
			sys.stdout.write(str(analysis[nav])+"     ")
		else:
			sys.stdout.write("0"+"     ")

	sys.stdout.write("\n")

	print("________________________________________________________________________________________________________________")


