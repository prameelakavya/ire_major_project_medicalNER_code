import re

file1 = open('nodes.txt','r')
file2 = open('nodes_extra_features.txt', 'r')
file3 = open('final_metamap_training.txt', 'r')
finalfile = open('final_features.txt', 'w')

lines1 = file1.read()
lines1 = lines1.split('\n')
lines2 = file2.read()
lines2 = lines2.split('\n')
lines3 = file3.read()
lines3 = lines3.split('\n')

ctr1 = 0
ctr2 = 0

while not ctr1 == len(lines1) and not ctr2 == len(lines3):
	split1 = lines1[ctr1].split(' ')
	split2 = lines2[ctr1].split(' ')
	split3 = lines3[ctr2].split(' ')
	while not (ctr1 + 1 == len(lines1) or split1[0] == split3[0]):
		if lines1[ctr1] == '':
	 		finalfile.write('\n')
		ctr1 = ctr1 + 1
		print split1[0]
		print split3[0]
		split1 = lines1[ctr1].split(' ')
		split2 = lines2[ctr1].split(' ')
	for i in range(len(split1) - 1):
		finalfile.write(split1[i] + ' ')
	for i in range(1, len(split2)):
		finalfile.write(split2[i] + ' ')
	for i in range(1, len(split3)):
		finalfile.write(split3[i] + ' ')
	finalfile.write(split1[len(split1) - 1] + '\n')
	ctr1 = ctr1 + 1
	ctr2 = ctr2 + 1



