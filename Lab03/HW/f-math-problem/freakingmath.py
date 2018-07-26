from random import *
import eval

def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(1,10)
    y = randint(1,10)
    a_list = ["+", "-", "*", "/"]

    op = choice(a_list)

    res = eval.cal(x, y, op)

    error = [-1, 0, 0, 1]
    ran_er = choice(error)
    result = res + ran_er
    return [x, y, op , result]

def check_answer(x, y, op, result, user_choice):
    boo = True
    res = eval.cal(x, y, op)
    if result == res  :
        if user_choice == True:
            boo = True
        elif user_choice == False: 
            boo = False
    else:
        if user_choice == False: 
            boo = True
        elif user_choice == True:
            boo = False
    return boo
    # sound
