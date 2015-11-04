import numpy
B = numpy.zeros((7, 87))
for num in range(5):
	ii = 0 ; x = "M"+str(num+1)+".txt"
	bdf = open(x, "r")
	print(x)
	for line in bdf:
		ii += 1
		print(ii)
		print(num)
		mat = float(line.replace(";",""))
		print(mat)
		B[num][ii]=mat
	bdf.close()
file = open("M1.csv", "w")
print(str(B))
for ii in range(1,83):
	ans = str(B[0][ii])+";"+str(B[1][ii])+";"+str(B[2][ii])+";"+str(B[3][ii])+";"+str(B[4][ii])
	file.write(str(ans))
	file.write("\n")
file.close
