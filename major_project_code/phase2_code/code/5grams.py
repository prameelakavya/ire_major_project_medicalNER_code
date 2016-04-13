import os
import re
from string import punctuation

path = '../data/twitter/training_Annotations/'
subdir = os.listdir(path)

writefile = open('nodes_5grams.txt', 'w')

for i in subdir:
	if i[0] == '.':
		continue
	subpath = path + i
	list_of_files = os.listdir(subpath)
	for j in list_of_files:
		if j[0] == '.':
			continue
		filenum = j.split('.')[0]
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
			#print len(final_tokens) - len(words)
			#print final_tokens
			#print words
			for o in range(len(final_tokens)):
				index = words.index(final_tokens[o])
				writefile.write(words[index] + ' ')
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
				writefile.write(labels[index])
				writefile.write('\n')


