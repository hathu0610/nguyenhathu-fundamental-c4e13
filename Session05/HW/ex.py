n = input().lower()

list_word = {}
for i in n:
    list_word[i] = list_word.get(i,0) +1


new_list = list(list_word.items())

new_list.sort()

for x in new_list:
    print(x[0], x[1]) 



