import csv
import itertools

headers = True
length_of_words = 0
num_known_words = 0
num_test_cases = 0
rows = []
known_words = []
test_cases = []
results = []
solution = ""

with open('A-small-practice.in', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		if headers:
			headers = False
			# grab problem variables
			header_values = row[0].split(' ')
			length_of_words = int(header_values[0])
			num_known_words = int(header_values[1])
			num_test_cases = int(header_values[2])
			continue
		rows.append(row)


# cycle thru known words
for row in rows[:num_known_words]:
	known_words.append(row[0])

# cycle thru test cases
for row in rows[num_test_cases * -1:]:
	test_cases.append(row[0])


# test how many words in the alien language match the pattern
for test_case in test_cases:
	# if there are no parentheses in the string
	if not "(" in test_case:
		# parse into separate lists
		l = list(test_case)
	# if there are parentheses
	else:
		# parse into separate lists
		l = []
		tmp = []
		flag = False
		for i in test_case:
			if flag:
				if i == ")":
					l.append(tmp)
					tmp = []
					flag = False
				else:
					tmp.append(i)
			elif i == "(":
				flag = True
			else:
				l.append([i])
	# find all possible combos
	possible_combos = [''.join(map(str,y)) for y in itertools.product(*l)]
	# test whether any of the combos are in known_words
	total = 0
	for possible_combo in possible_combos:
		if possible_combo in known_words:
			total += 1
	# append total to results list
	results.append([total])


i = 1
for result in results:
	solution += "Case #%d: " %d + str(result) + "\n"

with open('output.txt', 'w') as f:
	f.write(solution)


"""
Problem

After years of study, scientists at Google Labs have discovered an alien language transmitted from a faraway planet. The alien language is very unique in that every word consists of exactly L lowercase letters. Also, there are exactly D words in this language.

Once the dictionary of all the words in the alien language was built, the next breakthrough was to discover that the aliens have been transmitting messages to Earth for the past decade. Unfortunately, these signals are weakened due to the distance between our two planets and some of the words may be misinterpreted. In order to help them decipher these messages, the scientists have asked you to devise an algorithm that will determine the number of possible interpretations for a given pattern.

A pattern consists of exactly L tokens. Each token is either a single lowercase letter (the scientists are very sure that this is the letter) or a group of unique lowercase letters surrounded by parenthesis ( and ). For example: (ab)d(dc) means the first letter is either a or b, the second letter is definitely d and the last letter is either d or c. Therefore, the pattern (ab)d(dc) can stand for either one of these 4 possibilities: add, adc, bdd, bdc.

Input

The first line of input contains 3 integers, L, D and N separated by a space. D lines follow, each containing one word of length L. These are the words that are known to exist in the alien language. N test cases then follow, each on its own line and each consisting of a pattern as described above. You may assume that all known words provided are unique.
"""