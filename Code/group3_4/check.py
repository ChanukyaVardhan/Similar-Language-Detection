# ngrams_char = [word[i:i+n] for i in range(len(word)-n+1)];
import  sys,operator,liblinear
import numpy as np
from liblinearutil import *
from math import *
from copy import deepcopy
from ctypes import *

# gram_model = 0;
# gram_model = 2;
N = 32000;
vecsize = 2000;
# N = 2;
# vecsize = 2;

def main_cal(gram_model):
	features_lang_tf = {};
	features_lang_df = {};
	with open("g_4.txt",'r') as f:
	# with open("g_temp.txt",'r') as f:

		for line in f:
			words = line.split();
			if gram_model == 0:
				n = 3;
				ngrams_char_3 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
				all_ngrams = ngrams_char_3;
				# vecsize = 2000;
				vecsize = 30000;
			elif gram_model == 1:
				n = 4;
				ngrams_char_4 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
				all_ngrams = ngrams_char_4;
				# vecsize = 2000;
				vecsize = 30000;
			elif gram_model == 2:
				ngrams_word_1 = [];
				for i in range(len(words)):
					ngrams_word_1.append(words[i]);
				all_ngrams = ngrams_word_1;
				vecsize = 30000;
			elif gram_model == 3:
				ngrams_word_2 = [];
				for i in range(len(words)-1):
					ngrams_word_2.append(words[i] + " " + words[i+1]);
				all_ngrams = ngrams_word_2;
				vecsize = 30000;
			elif gram_model == 4:
				ngrams_word_3 = [];
				for i in range(len(words)-2):
					ngrams_word_3.append(words[i] + " " + words[i+1] + " " + words[i+2]);
				all_ngrams = ngrams_word_3;
				vecsize = 30000;
			elif gram_model == 5:
				n = 5;
				ngrams_char_5 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
				all_ngrams = ngrams_char_5;
				# vecsize = 2000;
				vecsize = 30000;
			elif gram_model == 6:
				n = 6;
				ngrams_char_6 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
				all_ngrams = ngrams_char_6;
				# vecsize = 2000;
				vecsize = 30000;
			elif gram_model == 7:
				n = 7;
				ngrams_char_7 = [' '*(n-1) + line[i:i+n] + ' '*(n) for i in range(len(line)-n+1)];
				all_ngrams = ngrams_char_7;
				vecsize = 30000;

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
		for i in range(0, vecsize):
			features_lang_tfidf_top.append(features_lang_tfidf_sorted[i][0]);

		# print(features_lang_tfidf_top);
		print(len(features_lang_tfidf_top))
	f.close();

	inverse_dict = {};

	for i in range(0, len(features_lang_tfidf_top)):
		inverse_dict.update({features_lang_tfidf_top[i]:i});

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
				feature.update({temp:1});
		return feature;


	list1 = [];

	# m = load_model("result" + str(gram_model))
	m = load_model("result" + str(gram_model) + "_" + str(vecsize));
	label = [];
	dvalues = [];
	with open("3_4.txt",'r') as ffff:

		for line in ffff:
			featurenode = gen_feature_nodearray(return_features(line))[0]
			# tempi = liblinear.predict(m,featurenode)
			vali = (c_double * 3)();
			tempi = liblinear.predict_values(m, featurenode, vali);
			label.append(tempi);
			dvalues.append(vali);

	# print(label)
	ffff.close();
	# return label;
	return dvalues;

# res = [];
# # for gram_model in [0]:
# # for gram_model in [0, 1]:
# # for gram_model in [0, 1, 5]:
# # for gram_model in [0, 1, 5, 6]:

# for gram_model in [0, 1, 2, 3, 5]:
# 	temp = main_cal(gram_model);
# 	res.append(deepcopy(temp));
# final_labels = [];
# for i in range(0, len(temp)):
# 	frequency = {}
# 	frequency[1] = 0;
# 	frequency[2] = 0;
# 	frequency[3] = 0;
# 	for j in range(0, len(res)):
# 		frequency[res[j][i]] += 1;
# 	# print(frequency)
# 	final_labels.append(max(frequency.iteritems(), key=operator.itemgetter(1))[0]);
# # print(final_labels);






res = [];
# for gram_model in [0, 1, 2, 3]:
# for gram_model in [0]:
# for gram_model in [0, 1]:
# for gram_model in [0, 1, 5]:
# for gram_model in [0, 1, 5, 6]:
# for gram_model in [0, 1, 5, 6, 7]:

# for gram_model in [2]:
# for gram_model in [2, 3]:
# for gram_model in [2, 3, 4]:

# for gram_model in [0, 1, 2, 3]:
for gram_model in [0, 1, 2, 3, 5]:
	temp = main_cal(gram_model);
	res.append(deepcopy(temp));
final_labels = [];
for i in range(0, len(temp)):
	maxval=float("-inf")
	finalLabel=0
	for k in range(0,len(temp[0])):
		summ=0
		for j in range(0, len(res)):
			summ+=res[j][i][k]
		if(summ>maxval):
			finalLabel=k
			maxval=summ
	final_labels.append(finalLabel)
# print(final_labels)

out_final = open("answers_3_4.txt", "w");
for i in final_labels:
	out_final.write(str(i) + "\n");


analysis = {}
for x in final_labels:
	if x in analysis:
		analysis[x]+=1
	else:
		analysis[x]=1
print(analysis)