import os
import re
from string import punctuation

path = '../data/twitter/testing_Annotations/'
subdir = os.listdir(path)

writefile = open('test_tokens_5grams.txt', 'w')

for i in subdir:
	if i[0] == '.':
		continue
	subpath = path + i
	list_of_files = os.listdir(subpath)
	for j in list_of_files:
		if j[0] == '.':
			continue
		filenum = j.split('.')[0]
		filename = open(subpath+'/'+filenum+'.txt','r')
		contents = filename.read()
		contents = contents.split('\n')
		for k in contents:
			tokens = k.split(' ')
			final_tokens = []
			for l in tokens:
				l = re.findall(r"[\w']+", l)
				for o in l:
					if o == '':
						continue
					final_tokens.append(o)
			for o in range(len(final_tokens)):
				writefile.write(final_tokens[o] + ' ')
				if o > 0:
					writefile.write(final_tokens[o - 1] + ' ')
				else:
					writefile.write('N/A ')
				if o > 1:
				 	writefile.write(final_tokens[o - 2] + ' ')
				else:
					writefile.write('N/A ')
				if o < len(final_tokens) - 1:
					writefile.write(final_tokens[o + 1] + ' ')
				else:
					writefile.write('N/A ')
				if o < len(final_tokens) - 2:
				 	writefile.write(final_tokens[o + 2] + ' ')
				else:
					writefile.write('N/A ')
				writefile.write('\n')


