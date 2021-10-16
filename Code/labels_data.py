
lines = 16000
l = []

# out1 = open("g1.txt",'w')
# out2 = open("g2.txt",'w')
# out3 = open("g3.txt",'w')
# out4 = open("g4.txt",'w')
# out5 = open("g5.txt",'w')
# out6 = open("g6.txt",'w')
out1 = open("g_1.txt",'w')
out2 = open("g_2.txt",'w')
out3 = open("g_3.txt",'w')
out4 = open("g_4.txt",'w')
out5 = open("g_5.txt",'w')
out6 = open("g_6.txt",'w')

l.append(out1)
l.append(out2)
l.append(out3)
l.append(out4)
l.append(out5)
l.append(out6)

dictonary = {0:0,1:1,2:2,3:3,4:3,5:1,6:5,7:0,8:5,9:4,10:4,11:2,12:1}

lang = 0
i=0

# Write all the sentences of train data for all the languages which belong to a group into seperate files with names as the group numbers(given by us)
with open("train_new.txt") as f:
	for line in f:
		words = line.split();
		words = words[:-1];
		temp_line = ' '.join(words);
		(l[dictonary[lang]]).write("#" + temp_line + "#\n")
		i+=1
		if(i==lines):
			i=0
			lang+=1
		if(lang==13):
			break

for item in l:
	item.close()