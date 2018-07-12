def fib(n):

  if n == 0:
        return 1
  elif n == 1:
        return 2
  else:
        return fib(n-1) + fib(n-2)



for n in range(0,5):
    numb_of_rab = fib(n)
    print("Month {0}: {1} pairs(s) of rabbit".format(n,numb_of_rab))
