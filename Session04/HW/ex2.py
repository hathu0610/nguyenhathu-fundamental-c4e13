from babel.numbers import format_currency

n = int(input("Enter your balance:"))

s = format_currency(n, 'USD', locale='en_US')


print("Your updated balance:",s.strip(".00"))