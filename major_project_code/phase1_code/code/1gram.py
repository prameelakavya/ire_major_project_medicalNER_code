import os
import re
from string import punctuation

path = '../data/twitter/training_Annotations/'
subdir = os.listdir(path)

writefile = open('nodes.txt', 'w')
files_done = []

for i in subdir:
	if i[0] == '.':
		continue
	subpath = path + i
	list_of_files = os.listdir(subpath)
	for j in list_of_files:
		if j[0] == '.' or j.split('.')[0] in files_done:
			continue
		filenum = j.split('.')[0]
		files_done.append(filenum)
		filename = open(subpath+'/'+filenum+'.ann','r')
		contents = filename.read()
		contents = contents.split('\n')
		words = []
		labels = []
		for k in contents:
			if len(k) == 0 or not k[0] == 'T':
				continue
			components = k.split('\t')
			for l in components:
				l = l.strip()
			classname = components[1].split(' ')[0]
			if classname == 'Disease' or classname == 'Symptom-or-Side-Effect' or classname == 'Drug':
				terms = components[2].split(' ')
				labels.append('B_'+classname)
				words.append(terms[0])
				for l in range(1, len(terms)):
					if terms[l] == '':
						continue
					words.append(terms[l])
					labels.append('I_'+classname)
		filename.close()
		filename = open(subpath+'/'+filenum+'.txt','r')
		contents = filename.read()
		contents = contents.split('\n')
		for k in contents:
			tokens = k.split(' ')
			for l in tokens:
				l = re.findall(r"[\w']+", l)
				for o in l:
					if o == '' or o in words:
						continue
					words.append(o)
					labels.append('Outside')
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
				index = words.index(final_tokens[o])
				writefile.write(words[index] + ' ')
				writefile.write(labels[index])
				writefile.write('\n')
		writefile.write('\n')

