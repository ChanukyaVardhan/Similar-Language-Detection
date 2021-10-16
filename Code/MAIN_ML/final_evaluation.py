out1 = open("test_test.txt", "w");
out2 = open("test_answers.txt", "w");

dict_lang = {"bg":0, "bs":1, "cz":2, "es-AR":3, "es-ES":4, "hr":5, "id":6, "mk":7, "my":8, "pt-BR":9, "pt-PT":10, "sk":11, "sr":12, "xx":13};

with open("test-gold.txt",'r') as f:
	for line in f:
		words = line.split();
		answer = words[len(words)-1];
		words = words[:-1];
		temp = " ".join(words);

		if(answer == "xx"):
			continue;
		out1.write(temp + "\n");
		out2.write(str(dict_lang[answer]) + "\n");