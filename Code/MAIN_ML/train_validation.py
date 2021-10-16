
train_lines = 16000
total_lines = 18000

trainorvalid = 0
count = 0

trainout = open("train_new.txt",'w')
validout = open("validation_new.txt",'w')


with open("project_train_processed.txt") as f:
	for line in f:

		if(trainorvalid==0):
			trainout.write(line)
		else:
			validout.write(line)

		count+=1

		if(count==train_lines):
			trainorvalid=1
		if(count==total_lines):
			count=0
			trainorvalid=0

