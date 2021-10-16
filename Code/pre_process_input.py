import sys, string



remove = list(string.punctuation)
print(remove)

# remove contains all special characters and numbers
for i in range(0,10):
	remove.append(str(i)) 

out = open("project_train_processed.txt",'w')

with open("project_train.txt") as f:
	for line in f:
		
		decodeline = line.decode('utf-8')
		
		for i in remove:
		 	decodeline = decodeline.replace(i,"")

		lowerline = decodeline.lower()
		out.write(lowerline.encode('utf-8'))
	
# project_train_processed.txt is written by processing project_train.txt file i.e., by removing special characters and numbers.

out.close()