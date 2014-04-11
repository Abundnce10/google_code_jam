from itertools import combinations
import csv

input_file = "A-large-practice.in"
output_file = "large-output.txt"

rows = []
results = []
n = 0


def compareWires(tup1, tup2):
	if tup1[0] > tup2[0] and tup1[1] < tup2[1]:
		return 1
	if tup1[0] < tup2[0] and tup1[1] > tup2[1]:
		return 1
	return 0

def findIntersections(wiresList):
	total_intersections = 0
	combos = combinations(wiresList, 2)
	for combo in combos:
		total_intersections += compareWires(combo[0], combo[1])
	return total_intersections



with open(input_file, 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		if n == 0:
			n = int(row[0])
			continue
		rows.append(row)



n = 0
wires = []
count_of_wires = 0

for row in rows:
	if n == 0:
		n = int(row[0])
		continue

	count_of_wires += 1
	wires.append((int(row[0].split(' ')[0]), int(row[0].split(' ')[1])))

	if count_of_wires == n:
		results.append(findIntersections(wires))

		# reset instance values
		n = 0
		wires = []
		count_of_wires = 0



# print results
counter = 1
with open(output_file, 'w') as f:
	for result in results:
		f.write("Case #%d: " % counter + str(result) + "\n")
		counter += 1

