n = int(input("Enter the total number of 1's and 0's: "))

for i in range(n):
    if i % 2 == 1:
        print(0,end= " ")
    else:
        print(1,end= " ")
print()