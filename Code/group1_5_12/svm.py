# ngrams_char = [word[i:i+n] for i in range(len(word)-n+1)];
import  sys,operator,liblinear
import numpy as np
from liblinearutil import *
from math import *

# gram_model = 0; # Character 3
# gram_model = 1; # Character 4
# gram_model = 5; # Character 5
gram_model = 2; # Word 1
# gram_model = 3; # Word 2


# gram_model = 4; # Word 3
# gram_model = 6; # Character 6
# gram_model = 7; # Character 7

N = 48000;
vecsize = 20000;
# N = 2;
# vecsize = 2;
features_lang_tf = {};
features_lang_df = {};
with open("g_2.txt",'r') as f:
# Generating the n-grams(both character and word n-grams based on model)
	for line in f:
		words = line.split();
		if gram_model == 0:
			n = 3;
			ngrams_char_3 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
			all_ngrams = ngrams_char_3;
		elif gram_model == 1:
			n = 4;
			ngrams_char_4 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
			all_ngrams = ngrams_char_4;
		elif gram_model == 2:
			ngrams_word_1 = [];
			for i in range(len(words)):
				ngrams_word_1.append(words[i]);
			all_ngrams = ngrams_word_1;
		elif gram_model == 3:
			ngrams_word_2 = [];
			for i in range(len(words)-1):
				ngrams_word_2.append(words[i] + " " + words[i+1]);
			all_ngrams = ngrams_word_2;
		elif gram_model == 4:
			ngrams_word_3 = [];
			for i in range(len(words)-2):
				ngrams_word_3.append(words[i] + " " + words[i+1] + " " + words[i+2]);
			all_ngrams = ngrams_word_3;
		elif gram_model == 5:
			n = 5;
			ngrams_char_5 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
			all_ngrams = ngrams_char_5;
		elif gram_model == 6:
			n = 6;
			ngrams_char_6 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
			all_ngrams = ngrams_char_6;
		elif gram_model == 7:
			n = 7;
			ngrams_char_7 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
			all_ngrams = ngrams_char_7;

		# Calulating tf and idf
		for item in all_ngrams:
			if item in features_lang_tf:
				features_lang_tf[item] += -1;
			else:
				features_lang_tf[item] = -1;

		temp_ngrams = list(set(all_ngrams));

		for item in temp_ngrams:
			if item in features_lang_df:
				features_lang_df[item] += -1;
			else:
				features_lang_df[item] = -1;

	# Calculating the score based on tf-idf value
	features_lang_tfidf = {x: 1.0*features_lang_tf[x]*log(N*1.0/(-features_lang_df[x])) for x in features_lang_tf};
	features_lang_tfidf_sorted = sorted(features_lang_tfidf.items(), key=operator.itemgetter(1));

	features_lang_tfidf_top = [];
	# Choose the top vecsize number of words
	for i in range(0, vecsize):
		features_lang_tfidf_top.append(features_lang_tfidf_sorted[i][0]);

f.close();

# Stores index of each word in the top featured list
inverse_dict = {};

for i in range(0, len(features_lang_tfidf_top)):
	inverse_dict[features_lang_tfidf_top[i]] = i;

# return features for a query sentence
def return_features(line):
	feature = {};

	words = line.split();
	if gram_model == 0:
		n = 3;
		ngrams_char_3 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
		all_ngrams = ngrams_char_3;
	elif gram_model == 1:
		n = 4;
		ngrams_char_4 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
		all_ngrams = ngrams_char_4;
	elif gram_model == 2:
		ngrams_word_1 = [];
		for i in range(len(words)):
			ngrams_word_1.append(words[i]);
		all_ngrams = ngrams_word_1;
	elif gram_model == 3:
		ngrams_word_2 = [];
		for i in range(len(words)-1):
			ngrams_word_2.append(words[i] + " " + words[i+1]);
		all_ngrams = ngrams_word_2;
	elif gram_model == 4:
		ngrams_word_3 = [];
		for i in range(len(words)-2):
			ngrams_word_3.append(words[i] + " " + words[i+1] + " " + words[i+2]);
		all_ngrams = ngrams_word_3;
	elif gram_model == 5:
		n = 5;
		ngrams_char_5 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
		all_ngrams = ngrams_char_5;
	elif gram_model == 6:
		n = 6;
		ngrams_char_6 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
		all_ngrams = ngrams_char_6;
	elif gram_model == 7:
		n = 7;
		ngrams_char_7 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
		all_ngrams = ngrams_char_7;

	temp_ngrams = list(set(all_ngrams));
	
	# Return feature as a dictionary.
	for item in temp_ngrams:
		if item in inverse_dict:
			temp = inverse_dict[item] + 1;
			feature.update({temp:1});
	return feature;


list1 = [];

with open("g_2.txt",'r') as ffff:

	for line in ffff:
		list1.append(return_features(line));

# labels for the train data.
values = [1]*(N/3) + [2]*(N/3) + [3]*(N/3);

# Training examples
solver = problem(values,list1)

# solution = train(solver, parameter('-c 0.001 -s 4'));
# solution = train(solver, parameter('-c 0.01 -s 4')); # original
# solution = train(solver, parameter('-c 0.1 -s 4'));
# solution = train(solver, parameter('-c 1 -s 4'));

# Run svm
solution = train(solver, parameter('-c 0.01 -s 4'));
# solution = train(solver, parameter('-c 0.01 -s 6'));
# solution = train(solver, parameter('-c 0.01 -s 5'));
# solution = train(solver, parameter('-c 0.01 -s 4'));
# solution = train(solver, parameter('-c 0.01 -s 3'));
# solution = train(solver, parameter('-c 0.01 -s 2'));
# solution = train(solver, parameter('-c 0.01 -s 1'));
# solution = train(solver, parameter('-c 0.01 -s 0'));

# Store weights in result file
save_model("result" + str(gram_model) + "_" + str(vecsize),solution)

