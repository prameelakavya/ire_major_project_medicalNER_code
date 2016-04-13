import os
import re
from string import punctuation
import nltk

path = '../data/twitter/training_Annotations/'
subdir = os.listdir(path)

writefile = open('nodes_extra_features.txt', 'w')
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
			pos_tags = {}
			all_tags = nltk.pos_tag(final_tokens)
			for o in all_tags:
				pos_tags[o[0]]=o[1]
			for o in range(len(final_tokens)):
				index = words.index(final_tokens[o])
				prev_adj = 'N/A'
				next_verb = 'N/A'
				for p in range(o):
					if pos_tags[final_tokens[o-p-1]][0:2] == 'JJ':
						prev_adj = final_tokens[o-p-1]
				for p in range(len(final_tokens)-o-1):
					if pos_tags[final_tokens[o+p+1]][0:2] == 'VB':
						next_verb = final_tokens[o+p+1]
						break
				writefile.write(words[index] + ' ')
				writefile.write(prev_adj + ' ')
				writefile.write(next_verb + ' ') 
				writefile.write('\n')
		writefile.write('\n')

