condition = True
list_items = ["T-Shirt","Sweater"]
while condition == True:
    question = input("Welcome to our shop, what do you want (C, R, U, D)?")

    if question == 'R' or question =='r':
        condition = True
    elif question == 'C' or question =='c':
        new_items = input("Enter new item:")
        list_items.append(new_items)
        condition = True    
    elif question == 'U' or question =='u':
        update_position = int(input("Update position?"))
        if update_position > len(list_items):
            print("The position you want to update do not exist!")
            continue
        replace_item = input("New item?")
        list_items[update_position-1] = replace_item
        condition = True
    elif question == 'D' or question =='d':
        dele_posi = int(input("Delete position?"))
        
        if dele_posi > len(list_items):
            print("The position you want to delete do not exist!")
            continue
        list_items.pop(dele_posi - 1)
        condition = True
    else: 
        print("Your input is not valid!!")
        continue
    print("Our items:", ",".join(list_items))    
    n = input("Would you like to continue?")
    if n == 'yes':
        condition = True
    elif n == 'no':
        condition = False


    





