prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key in prices.keys():
    print(key)
    print("price:", prices[key])
    print("stock:", stock[key])
    print()

total = 0
total = []
for key in prices.keys():
    value = prices[key]*stock[key]
    print("Value of {0}: {1}".format(key,value))
    total.append(value)

print("Total: {}".format(sum(total)))