import re

f = open('day03.input')
inputs = f.read()
f.close()

count = 0

lines = inputs.split('\n')

for col in range(0,3):
	for i in range(0,len(lines),3):

		s = []
		s.append( [int(x) for x in re.findall(r'(\d+)',lines[i])][col] )
		s.append( [int(x) for x in re.findall(r'(\d+)',lines[i+1])][col] )
		s.append( [int(x) for x in re.findall(r'(\d+)',lines[i+2])][col] )
		s.sort()

		print(s)

		if s[0] + s[1] > s[2]:
			count += 1

print(count)