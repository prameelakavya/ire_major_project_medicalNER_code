import os
import re
from string import punctuation

path = '../data/twitter/training_Annotations/'
subdir = os.listdir(path)
words = []
labels = []
relation = []
arg1 = []
arg2 = []
outside = []

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
		current_keywords = []
		for k in contents:
			if len(k) == 0 or not k[0] == 'T':
				continue
			components = k.split('\t')
			for l in components:
				l = l.strip()
			classname = components[1].split(' ')[0]
			if classname == 'Disease' or classname == 'Symptom-or-Side-Effect' or classname == 'Drug':
				terms = components[2].split(' ')
				if terms[0] == '':
					continue
				labels.append('B_'+classname)
				words.append(terms[0])
				for l in range(1, len(terms)):
					if terms[l] == '':
						continue
					words.append(terms[l])
					current_keywords.append(terms[l])
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
					if o == '' or o in current_keywords:
						continue
					outside.append(o)

nodes = open('nodes.txt','w')	
for i in range(len(words)):
	nodes.write(words[i]+' '+labels[i]+'\n')
for i in range(len(outside)):
	nodes.write(outside[i]+' '+'Outside'+'\n')
nodes.close()

'''edges = open('edges.txt','w')
for i in range(len(relation)):
	edges.write(relation[i]+'\t'+arg1[i]+'\t'+arg2[i]+'\n')
edges.close()'''
