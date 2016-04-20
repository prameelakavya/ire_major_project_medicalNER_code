from sklearn.metrics import confusion_matrix

file1 = open('nodes_with_label.txt','r')
file2 = open('output_combined.txt','r')

lines1 = file1.read()
lines1 = lines1.split('\n')
lines2 = file2.read()
lines2 = lines2.split('\n')

total = 0
correct = 0

actual = []
predicted = []

for i in range(len(lines1)):
	split1 = lines1[i].split(' ')
	split2 = lines2[i].split('\t')
	actual.append(split1[len(split1)-1])
	predicted.append(split2[len(split2)-1])
	if split1[len(split1)-1]==split2[len(split2)-1]:
		correct = correct + 1
	total = total + 1

print float(correct)/total

print confusion_matrix(actual,predicted)
