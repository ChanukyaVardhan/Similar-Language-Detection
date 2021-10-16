import  sys,operator
from copy import deepcopy
from math import *

N_langs = 14
vecsize = 5000

vectorlanguages = []

# Read the model from features.txt
with open("features.txt") as f:

	values = []
	names = []
	count=0
	wornum = 0

	for line in f:

		if(wornum==0):
			values.append(float(line))
			count+=1
		else:
			names.append(line[:-1])
			count+=1

		if(count==vecsize):
			wornum = 1
		if(count==2*vecsize):
			count=0
			wornum=0
			vectorlanguages.append((deepcopy(values),deepcopy(names)))
			names = []
			values = []

print("started tesing")

dictlist = [dict() for x in range(N_langs)]

for i in range(0,N_langs):

	for tt in range(0,len(vectorlanguages[i][1])):
		(dictlist[i])[vectorlanguages[i][1][tt]] = tt

for i in range(0,1):
	print(i)
	label = []
	with open("input"+".txt") as f:
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


				if(maxoflis!=0):
					maxtemp = maxtemp*0.5/(maxoflis)				

				# for i in range(0,vecsize):
				# 	maxtemp+=vecword[i]*vector[0][i]

				#print("Maxtemp="+str(maxtemp))
				if(maxtemp>maxscore):
					maxscore = maxtemp
					maxlabel = langnum

				langnum+=1

			label.append(maxlabel)
			#break
			#print(maxlabel)

	print(label)

	analysis = {}

	for x in label:

		if x in analysis:
			analysis[x]+=1
		else:
			analysis[x]=1

	print(analysis)
	print("________________________________________________________________________________________________________________")
