a = int(input("Enter a number a = "))


for j in range(1,(a+1)):
    for i in range(1, a+1):
        k = j*i
        print(k, end="\t")
    print()

