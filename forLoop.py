import dis
def forLoop():
	x = 0
	for x in range(5):
		x += 1
	return x
dis.dis(forLoop)


