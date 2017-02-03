def draw(filename, x, y):
	'''
	Makes file if it doesn't exist and writes headers
	'''

	file = open(filename, "w")
	s = "P3\n" + str(x) + " " + str(y) + " 255\n"
	file.write(s)

	r = c = 0
	while r < y:
		while c < x:
			R = 0
			G = 255
			B = 0

			
