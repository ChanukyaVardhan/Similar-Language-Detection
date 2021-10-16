

i=0
out = open("0.txt",'w')
lang = 0
lines = 2000

# Generates validation data for each language in a separate file i.txt where i is the language number.
with open("validation_new.txt") as f:
	for line in f:

		out.write(line)
		i+=1
		if(i==lines):
			i=0
			lang+=1
			out = open(str(lang)+".txt",'w')

