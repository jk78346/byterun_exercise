import dis
def elif_cond():
	x = 0
	if x > 0:
		x = 1
	elif x < 0:
		x = 1
	else:
		x = 0
dis.dis(elif_cond)

