import os
import re
from string import punctuation

path = '../data/twitter/testing_Annotations/'
subdir = os.listdir(path)
words = []
labels = []
relation = []
arg1 = []
arg2 = []
outside = []
writefile = open('test_tokens.txt','w')

for i in subdir:
	if i[0] == '.' or len(i.split('.ann'))==2:
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
			for l in tokens:
				l = re.findall(r"[\w']+", l)
				for o in l:
					if o == '':
						continue
					writefile.write(o+'\n')
		writefile.write('\n')
