from random import randint
import eval
import random
x = randint(1,10)
y = randint(1,10)

a_list = ["+", "-", "*", "/"]

op = random.choice(a_list)

res = eval.cal(x, y, op)

error = [-1, 0, 0, 0, 1]
ran_er = random.choice(error)
# error = random.choice([-1,0,1])
display_res = res + ran_er
print("{0} {1} {2} = {3}".format(x, op, y, display_res))


ans = input("(Y/N)? ").upper()

if ran_er == 0:
    if ans == "Y":
        print("yay")
    elif ans == "N":
        print("You're wrong")
else:
    if ans == "N" :
        print("yay")
    elif ans == "Y":
        print("You're wrong")


