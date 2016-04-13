import re

file1 = open('nodes.txt','r')
file2 = open('nodes_extra_features.txt', 'r')
file3 = open('metamap_training.txt', 'r')
finalfile = open('final_features.txt', 'w')

lines1 = file1.read()
lines1 = lines1.split('\n')
lines2 = file2.read()
lines2 = lines2.split('\n')
lines3 = file3.read()
lines3 = lines3.split('\n')

ctr1 = 0
ctr2 = 0

while True:
	if ctr1 >= len(lines1):
		break
	if lines1[ctr1] == '\n':
	 	ctr1 = ctr1 + 1
	 	finalfile.write('\n')
	split1 = lines1[ctr1].split(' ')
	split2 = lines2[ctr1].split(' ')
	split3 = lines3[ctr2].split(' ')
	print split1[0]
	print split3[0]
	print ctr1
	print ctr2
	if split1[0].replace("'",'')==split3[0]:
		fstring = split1[0].replace("'",'') + ' '
		for i in range(1, len(split1)-1):
			fstring = fstring + split1[i] + ' '
		for i in range(1,len(split2)):
			fstring = fstring + split2[i] + ' '
		for i in range(1, len(split3)):
			fstring = fstring + split3[i] + ' '
		fstring = fstring + split1[len(split1)-1] + '\n'
		finalfile.write(fstring)
		ctr1 = ctr1 + 1
		ctr2 = ctr2 + 1
	elif split1[0]=='\n':
	  	ctr1 = ctr1 + 1
	elif split3[0]=='\n':
	  	ctr2 = ctr2 + 1
	else:
	  	word = split3[0]
	  	l = re.findall(r"[\w']+", word)
	  	words = []
	  	for o in l:
			if o == '' or o in words:
				continue
			words.append(o)
		print words
		if len(words) == 1:
		 	fstring = words[0] + ' '
		 	split1 = lines1[ctr1].split(' ')
		 	split2 = lines2[ctr1].split(' ')
		 	if not split1[0].replace("'",'') == words[0]:
		 		print 'yes'
			  	ctr1 = ctr1 + 1
			else:
				for i in range(1, len(split1)-1):
					fstring = fstring + split1[i] + ' '
				for i in range(1,len(split2)):
					fstring = fstring + split2[i] + ' '
				for i in range(1, len(split3)):
					fstring = fstring + split3[i] + ' '
				fstring = fstring + split1[len(split1)-1] + '\n'
				finalfile.write(fstring)
				ctr1 = ctr1 + 1
				ctr2 = ctr2 + 1
		elif len(words)>1:
			for w in words:
				fstring = w + ' '
				split1 = lines1[ctr1].split(' ')
				split2 = lines2[ctr1].split(' ')
				if split1[0]==w:
					for i in range(1, len(split1)-1):
						fstring = fstring + split1[i] + ' '
					for i in range(1, len(split2)):
						fstring = fstring + split2[i] + ' '
					fstring = fstring + split3[1] 
					fstring = fstring + split1[len(split1)-1] + '\n'
					ctr1 = ctr1 + 1
					finalfile.write(fstring)
				elif lines1[ctr1]=='\n':
				  	ctr1 = ctr1 + 1
				  	finalfile.write('\n')
				  	break
				else:
				  	ctr2 = ctr2 + 1
				  	break
			ctr2 = ctr2 + 1
		else:
		    	ctr2 = ctr2 + 1
