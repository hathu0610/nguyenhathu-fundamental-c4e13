sheep_sizes = [5,7,300,90,24,50,75]

print("Hello, my name is Thu and these are my sheep sizes", sheep_sizes)

print("Now my biggest sheep has size {} let's shear it".format(max(sheep_sizes)))

max_size = sheep_sizes.index(max(sheep_sizes))
sheep_sizes[max_size] = 8

print("After shearing, here is my flock", sheep_sizes)

new_sheep_sizes = [x+50 for x in sheep_sizes]

print("One month has passed, now here is my flock", new_sheep_sizes)