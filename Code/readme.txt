Name the entire raw train data as project_train.txt.

First run the following files in order:

pre_process_input.py
train_validation.py
eachlang.py
	This generates i.txt.
word_count_language.py
labels_data.py
	This generates the train data into groups
	Put these data in the corresponding folders along with the validation i.txt files as generated after eachlang.py was executed
svm.py
	Generates result<gram_model>_<vecsize>
check.py
	Name the testing file as input.txt and run check.py to get final results.
grouping_test.py is used to check for the test data results


Stable Github link : https://github.com/Simdiva/DSL-Task/tree/master/data/DSLCC-v2.0/train-dev

Libraries:
liblinear, liblinearutil, numpy, ctypes, math, copy, string, operator.

We have one folder for each language group with their corresponding models.
About_the_files.txt file contains the function of each file.
results_analysis.txt contains the values of the observations of the testing that we have done for the training data, validation data. This is used for the plotting of the graphs.
Plots folder contains all the relevant graphs.
Confusion Matrix folder contains Confusion Matrix for group classification.
result<gram_model>_<vecsize> and features files are the model files(which contains weights and features of model).