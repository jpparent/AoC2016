input = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"

n = 0
e = 1
s = 2
w = 3

dir = n
x,y = 0,0

inputs = input.split(", ")

seen = []
crossedPath = False

for i, move in enumerate(inputs):
	side = move[:1]
	steps = int(move[1:])

	if side == "R":
		dir = (dir + 1) % 4
	elif side == "L":
		dir = (dir - 1) % 4

	# loop on each single steps and store it as seen
	for j in range(steps):
		
		if dir == n:
			y += 1
		elif dir == e:
			x += 1
		elif dir == s:
			y -= 1
		elif dir == w:
			x -= 1

		current = "{0},{1}".format(x,y)
		if current not in seen:
			seen.append(current)
		else: 
			crossedPath = True
			break # we found what we're looking for, no need to continue

	if crossedPath:
		break

print("final destination: {0},{1}".format(x, y))
blocks = abs(x) + abs(y)
print("{0} blocks away".format(blocks))		