import dis
def whileLoop():
	x = 0
	while x < 5:
		x += 1
	return
dis.dis(whileLoop)

