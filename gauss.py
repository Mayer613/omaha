import math
import random
import numpy 

M = numpy.zeros(1000500)

for i in range(1000500):
	k = random.random()
	if k < 0.071675:
		M[i] = random.gauss(0.44263, 2.0447)
	else :
		M[i] = random.gauss(0.55979, 0.82083)


numpy.savetxt("Gauss.txt", M, fmt='%10.5f', delimiter=';')

