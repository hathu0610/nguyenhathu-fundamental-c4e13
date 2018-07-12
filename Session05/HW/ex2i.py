numbers = [1, 6, 8, 1, 2, 1, 5, 6]

n = int(input("Enter a number?"))
count=0


for i in range(len(numbers)):
   if numbers[i] == n:
       count+=1
       


print(n," appears {} times in my list".format(count))