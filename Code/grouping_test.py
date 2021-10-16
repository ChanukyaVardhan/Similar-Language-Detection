import  sys,operator
from copy import deepcopy
from math import *

dict_lang = {"bg":0, "bs":1, "cz":2, "es-AR":3, "es-ES":4, "hr":5, "id":6, "mk":7, "my":8, "pt-BR":9, "pt-PT":10, "sk":11, "sr":12, "xx":13};

vecsize = 5000

vectorlanguages = []

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

# print(vectorlanguages)

print("started tesing")

out_0 = open("0.txt", "w");
out_1_5_12 = open("1_5_12.txt", "w");
out_2 = open("2.txt", "w");
out_3_4 = open("3_4.txt", "w");
out_6_8 = open("6_8.txt", "w");
out_7 = open("7.txt", "w");
out_9_10 = open("9_10.txt", "w");
out_11 = open("11.txt", "w");

out_0_ans = open("0_ans.txt", "w");
out_1_5_12_ans = open("1_5_12_ans.txt", "w");
out_2_ans = open("2_ans.txt", "w");
out_3_4_ans = open("3_4_ans.txt", "w");
out_6_8_ans = open("6_8_ans.txt", "w");
out_7_ans = open("7_ans.txt", "w");
out_9_10_ans = open("9_10_ans.txt", "w");
out_11_ans = open("11_ans.txt", "w");

for i in range(0,1):
	print(i)
	label = []
	with open("test-gold"+".txt") as f:
		for preline in f:

			prewords = preline.split();
			answer = prewords[len(prewords)-1];
			if(answer == "xx"):
				continue;
			prewords = prewords[:-1];
			line = " ".join(prewords);

			linewords = (line).split()
			maxscore = float("-inf")
			maxlabel = 0
			langnum = 0

			for vector in vectorlanguages:

				vecword = [0]*vecsize

				for lineword in linewords:

					if lineword in vector[1]:
						vecword[(vector[1]).index(lineword)] += 1

				maxoflis = max(vecword)

				if(maxoflis!=0):
					vecword = [0.0 + x*0.5/maxoflis for x in vecword]

				# print("----------------------------------------")
				# ud = 0
				# while(ud<100):
				# 	print(vecword[ud],vector[0][ud],vector[1][ud])
				# 	ud+=1

				maxtemp = 0

				for i in range(0,vecsize):
					maxtemp+=vecword[i]*vector[0][i]
				#print("Maxtemp="+str(maxtemp))
				if(maxtemp>maxscore):
					maxscore = maxtemp
					maxlabel = langnum

				langnum+=1

			label.append(maxlabel)
			#break
			#print(maxlabel)

			if maxlabel == 0:
				out_0.write(line + "\n");
				out_0_ans.write(str(dict_lang[answer]) + "\n");
			elif maxlabel == 1 or maxlabel == 5 or maxlabel == 12:
				out_1_5_12.write(line + "\n");
				out_1_5_12_ans.write(str(dict_lang[answer]) + "\n");
			elif maxlabel == 2:
				out_2.write(line + "\n");
				out_2_ans.write(str(dict_lang[answer]) + "\n");
			elif maxlabel == 3 or maxlabel == 4:
				out_3_4.write(line + "\n");
				out_3_4_ans.write(str(dict_lang[answer]) + "\n");
			elif maxlabel == 6 or maxlabel == 8:
				out_6_8.write(line + "\n");
				out_6_8_ans.write(str(dict_lang[answer]) + "\n");
			elif maxlabel == 7:
				out_7.write(line + "\n");
				out_7_ans.write(str(dict_lang[answer]) + "\n");
			elif maxlabel == 9 or maxlabel == 10:
				out_9_10.write(line + "\n");
				out_9_10_ans.write(str(dict_lang[answer]) + "\n");
			elif maxlabel == 11:
				out_11.write(line + "\n");
				out_11_ans.write(str(dict_lang[answer]) + "\n");

	print(label)
	out_0.close();
	out_1_5_12.close();
	out_2.close();
	out_3_4.close();
	out_6_8.close();
	out_7.close();
	out_9_10.close();
	out_11.close();
	out_0_ans.close();
	out_1_5_12_ans.close();
	out_2_ans.close();
	out_3_4_ans.close();
	out_6_8_ans.close();
	out_7_ans.close();
	out_9_10_ans.close();
	out_11_ans.close();

	analysis = {}

	for x in label:

		if x in analysis:
			analysis[x]+=1
		else:
			analysis[x]=1

	print(analysis)
	print("________________________________________________________________________________________________________________")
f.close();