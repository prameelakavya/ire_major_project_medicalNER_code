file1 = open('nodes.txt','r')
file2 = open('nodes_extra_features.txt','r')

featurefile = open('combined_features.txt','w')

lines1 = file1.read()
lines1 = lines1.split('\n')
lines2 = file2.read()
lines2 = lines2.split('\n')

for i in range(len(lines1)):
	if lines1[i]=='\n':
		featurefile.write('\n')
		continue
	split1 = lines1[i].split(' ')
	split2 = lines2[i].split(' ')
	finalstring = split1[0] + ' '
	for j in range(1,len(split1)-1):
		finalstring = finalstring + split1[j] + ' '
	for j in range(1, len(split2)):
		finalstring = finalstring + split2[j] + ' '
	finalstring = finalstring + split1[len(split1)-1] + '\n'
	featurefile.write(finalstring)
