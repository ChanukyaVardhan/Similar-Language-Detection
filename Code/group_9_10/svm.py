# ngrams_char = [word[i:i+n] for i in range(len(word)-n+1)];
import  sys,operator,liblinear
import numpy as np
from liblinearutil import *
from math import *

# gram_model = 0; # Character 3
# gram_model = 1; # Character 4
# gram_model = 5; # Character 5
# gram_model = 2; # Word 1
gram_model = 3; # Word 2


# gram_model = 4; # Word 3
# gram_model = 6; # Character 6
# gram_model = 7; # Character 7

N = 32000;
vecsize = 30000;
# N = 2;
# vecsize = 2;
features_lang_tf = {};
features_lang_df = {};
with open("g_5.txt",'r') as f:
# with open("g_temp.txt",'r') as f:

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


		# all_ngrams = ngrams_char_3 + ngrams_char_4 + ngrams_word_1 + ngrams_word_2;
		# all_ngrams = ngrams_word_2;
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

	features_lang_tfidf = {x: 1.0*features_lang_tf[x]*log(N*1.0/(-features_lang_df[x])) for x in features_lang_tf};
	features_lang_tfidf_sorted = sorted(features_lang_tfidf.items(), key=operator.itemgetter(1));

	features_lang_tfidf_top = [];
	# print(len(features_lang_tfidf_sorted))
	for i in range(0, vecsize):
		features_lang_tfidf_top.append(features_lang_tfidf_sorted[i][0]);

	# print(features_lang_tfidf_top);
	# print(len(features_lang_tfidf_top))
f.close();

inverse_dict = {};

for i in range(0, len(features_lang_tfidf_top)):
	inverse_dict[features_lang_tfidf_top[i]] = i;
	# inverse_dict.update({features_lang_tfidf_top[i]:i});

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
	
	for item in temp_ngrams:
		# if item in features_lang_tfidf_top:
		if item in inverse_dict:
			# temp = int(np.where(np.array(features_lang_tfidf_top)==item)[0][0]+1)
			temp = inverse_dict[item] + 1;
			# print(str(temp) + "        " + str(int(np.where(np.array(features_lang_tfidf_top)==item)[0][0]+1)));
			# print(temp);
			feature.update({temp:1});
	return feature;


list1 = [];

with open("g_5.txt",'r') as ffff:

	for line in ffff:
		list1.append(return_features(line));
# print(list1);

values = [1]*(N/2) + [2]*(N/2);
# values = [1]*(N/3) + [2]*(N/3) + [3]*(N/3);
# values = [0]*(N/3) + [1]*(N/3) + [2]*(N/3);

# for item in list1:
# 	print(type(item))

solver = problem(values,list1)

solution = train(solver, parameter('-c 0.01 -s 4'));

# save_model("result" + str(gram_model) + "_" + str(vecsize) + "_old",solution)
# save_model("result" + str(gram_model) + "_" + str(vecsize) + "_new",solution)
save_model("result" + str(gram_model) + "_" + str(vecsize),solution)

