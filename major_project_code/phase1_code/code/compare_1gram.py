actualfile = open('testnodes.txt', 'r')
predictedfile = open('output_1gram.txt', 'r')

actual = actualfile.read().split('\n')
predicted = predictedfile.read().split('\n')

correct = 0
total = 0

for i in range(len(actual)):
	record1 = actual[i].split(' ')
	record2 = predicted[i].split('\t')
	if record1[-1] == record2[-1]:
		correct = correct + 1
	total = total + 1

accuracy_file = open('accuracy_1gram.txt', 'w')
accuracy_file.write('Accuracy: ')
accuracy_file.write(str(100*float(correct)/total))
