from random import randint, choice

list_word = "champion"

sep_list_word = list(list_word)
new_list = []

loop = True
while loop:
    random_letter = choice(sep_list_word)

    new_list.append(random_letter)
    sep_list_word.remove(random_letter)
    if len(sep_list_word) == 0:
        loop = False
print(*new_list)




while True:
    n = input("Your answer:")


    if n == "champion":
     print("bingo")
     break
    else: 
        print("Oh no")
        continue