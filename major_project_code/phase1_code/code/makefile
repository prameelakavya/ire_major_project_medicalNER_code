all : nodes_1gram.txt model_1gram.txt model_5grams.txt testnodes.txt test_tokens.txt output_1gram.txt output_5grams.txt accuracy_1gram.txt accuracy_5grams.txt

#all : nodes_1gram.txt nodes_5grams.txt model_5grams.txt testnodes_5grams.txt test_tokens_5grams.txt output_5grams.txt accuracy_5grams.txt

nodes_1gram.txt : 1gram.py
	python 1gram.py

model_1gram.txt : nodes.txt template_file_1gram
	crf_learn -t template_file_1gram nodes.txt model_1gram

model_5grams.txt : nodes.txt template_file_5grams
	crf_learn -t template_file_5grams nodes.txt model_5grams

testnodes.txt : test_1gram.py
	python test_1gram.py

test_tokens.txt : convert_test_1gram.py
	python convert_test_1gram.py

output_1gram.txt : test_tokens.txt model_1gram
	crf_test -m model_1gram test_tokens.txt > output_1gram.txt

output_5grams.txt : test_tokens.txt model_5grams
	crf_test -m model_5grams test_tokens.txt > output_5grams.txt

accuracy_1gram.txt : compare_1gram.py output_1gram.txt testnodes.txt
	python compare_1gram.py

accuracy_5grams.txt : compare_5grams.py output_5grams.txt testnodes.txt
	python compare_5grams.py
