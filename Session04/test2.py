
n = int(input("Enter a number:"))
loop = True

for i in range(2,(round(n**0.5)+1)):
    if n%i ==0:
        loop = False
        break
    else:
        loop = True

if loop == True:
    print("prime")
else:
    print("not prime")
            
