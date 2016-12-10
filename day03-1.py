import re

f = open('day03.input')
inputs = f.read()
f.close()

count = 0

lines = inputs.split('\n')

for i, line in enumerate(lines):
	s = [int(x) for x in re.findall(r'(\d+)',line)]
	s.sort()

	if s[0] + s[1] > s[2]:
		count += 1

print(count)