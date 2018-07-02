sheep_sizes = [5,7,300,90,24,50,75]

print("Hello, my name is Thu and these are my sheep sizes", sheep_sizes)

for i in range (1,4):
    print("MONTH", i)

    new_sheep_sizes = [x+50 for x in sheep_sizes]

    print("One month has passed, now here is my flock", new_sheep_sizes)
    print("Now my biggest sheep has size {} let's shear it".format(max(new_sheep_sizes)))

    max_size = new_sheep_sizes.index(max(new_sheep_sizes))
    new_sheep_sizes[max_size] = 8

    print("After shearing, here is my flock", new_sheep_sizes)
    sheep_sizes = new_sheep_sizes



