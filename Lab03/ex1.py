import eval
x = int(input("x = "))
operation = input("Operation(+,-,*,/):")
y = int(input("y = "))

res = eval.cal(x, y, operation)

print("* " * 20)
print( "{0} {1} {2} = {3}".format(x, operation ,y, res))