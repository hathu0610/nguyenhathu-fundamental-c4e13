teencode = {
    "hc" : "hoac",
    "ng" : "nguoi",
    "pt" : "phat trien",
    "eny" : "em nguoi yeu"
}

while True:
    print(*teencode.keys(), sep = "\t")
    print()
    key = input("Your code?")

    if key in teencode:
        print("translation: ",teencode[key])
    else: 
        print("your word is not in the dictionary")
        answer = input("Do you want to update?(Y/N)").upper()
        if answer == "Y":
            new_value = input("translation?")
            teencode[key] = new_value
            
        elif answer == "N":
            break
