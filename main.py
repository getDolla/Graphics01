def draw(filename, x, y):
    s = "P3\n" + str(x) + " " + str(y) + " 255\n" #header

    r = 0
    while r < y:
        c = 0
        while c < x:
            R = (c + r)%255
	    G = 255
	    B = (r/2) % 255

            s += str(R) + " " + str(G) + " " + str(B) + " \n"
            c += 1
        r += 1

    with open(filename+".ppm", "w") as f:
        f.write(s)

draw("pic", 500, 500)

			
