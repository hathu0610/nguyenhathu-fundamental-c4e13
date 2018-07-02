a = int(input("Enter a number: "))

for j in range(a):
    for i in range(a):
        if (i+j)% 2 == 1:
            print(0,end= ' ')
        else:
            print(1,end= ' ')
    print()
