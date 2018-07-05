print("Think of a number. Press'Enter'")
input()

print("""
All you have to do is to answer to my guess
'c' if answer is 'C'orrect
'l' if answer is 'L'ower than your number
's' if answer is 'S'maller than your number
""")
loop = 0

low = 0
high = 100


# // la so nguyen
# / la so thap phan

while True:
    mid = (low+high)//2 
    n = input("Is {} your number?".format(mid)).lower()
    #chuyen het nhap thanh chu thuong. upper la chu hoa
    
    
    if n == 'c':
        break
    elif n == 'l':
        
        high = mid
     
       # mid = (low+high)//2
       
    elif n == 's':
        low = mid
        #mid = (low+high)//2
    loop+=1
    if loop ==7:
        print("Your number doesn't exist")
        break
    
        
    

