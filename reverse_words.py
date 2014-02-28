import csv

phrases = []
results = []
n = 0
output = ""

with open('B-large-practice.in', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		if n == 0:
			n = int(row[0])
			continue
		phrases.append(row)


for phrase in phrases:
	words = phrase[0].split(' ')
	results.append(words[::-1])

counter = 1

for result in results:
	output += "Case #%d: " % counter + " ".join(result) + "\n"
	counter += 1

with open('output.txt', 'w') as f:
	f.write(output)

"""
Problem

Given a list of space separated words, reverse the order of the words. Each line of text contains L letters and W words. A line will only consist of letters and space characters. There will be exactly one space character between each pair of consecutive words.

Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will a line of letters and space characters indicating a list of space separated words. Spaces will not appear at the start or end of a line.

Output

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.
"""