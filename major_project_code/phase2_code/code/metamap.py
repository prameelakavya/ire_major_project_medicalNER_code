import re
	
training = open('metamap_training.txt', 'r')
training = training.read()
training = training.split('\n')

final_training = open('final_metamap_training.txt', 'w')

testing = open('metamap_testing.txt', 'r')
testing = testing.read()
testing = testing.split('\n')

final_testing = open('final_metamap_testing.txt', 'w')

for line in training:
	words = line.split(' ')
	all_words = re.findall(r"[\w']+", words[0])
	for i in all_words:
		if i == '':
			continue
		else:
			final_training.write(i + ' ' + words[1] + '\n')


for line in testing:
	words = line.split(' ')
	all_words = re.findall(r"[\w']+", words[0])
	for i in all_words:
		if i == '':
			continue
		else:
			final_testing.write(i + ' ' + words[1] + '\n')


