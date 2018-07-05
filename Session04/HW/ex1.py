n = input("Your full name: ")
split_name = n.split()
loop = 0
new_name = []
while loop < len(split_name):
    new_name.append(split_name[loop].capitalize()) 
    loop+=1

print(*new_name)