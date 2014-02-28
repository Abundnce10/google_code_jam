import csv

n_test_cases = 0
rows = []
results = ""


with open('A-large-practice.in', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		if n_test_cases == 0:
			n_test_cases = int(row[0])
			#print "N:", n_test_cases
			continue
		rows.append(row)
		#print row


def findTwoItems(credit, itemsList):
	"""Find the two items that add up to the credit amount and returns their indices"""
	values = []
	for i, v in enumerate(itemsList):
		for idx, val in enumerate(itemsList):
			if v + val == credit and i != idx:
				# return two indices, smallest first				
				return sorted([i+1, idx+1])
	


credit = 0
items_count = 0
items = []
case = 1

for row in rows:
	if not credit:
		credit = int(row[0])
	elif not items_count:
		items_count = int(row[0])
	else:
		items = [int(n) for n in row[0].split(' ')]
		# run algo
		answers = findTwoItems(credit, items)
		print credit, items, answers, "\n------\n"
		# write results "Case #1: 2 3"
		results += "Case #%d: %d %d\n" % (case, answers[0], answers[1])
		# reset variables
		credit = 0
		items_count = 0
		items = []
		# increment case
		case += 1


# Save to text file
with open('output.txt', 'w') as f:
	f.write(results)

print results


"""
Problem

You receive a credit C at a local store and would like to buy two items. You first walk through the store and create a list L of all available items. From this list you would like to buy two items that add up to the entire value of the credit. The solution you provide will consist of the two integers indicating the positions of the items in your list (smaller number first).

Input

The first line of input gives the number of cases, N. N test cases follow. For each test case there will be:

    One line containing the value C, the amount of credit you have at the store.
    One line containing the value I, the number of items in the store.
    One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
    Each test case will have exactly one solution.

Output

For each test case, output one line containing "Case #x: " followed by the indices of the two items whose price adds up to the store credit. The lower index should be output first.

Limits

5 ≤ C ≤ 1000
1 ≤ P ≤ 1000 
"""

