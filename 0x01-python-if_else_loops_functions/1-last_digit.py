#!/usr/bin/python3
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
print(f"Last digit of {number:d} is {lastDigit:d} and is ", end="")
if lastDigit == 0:
   print("zero")
if lastDigit > 5:
   print("greater than 5")
else:
    print("less than 6 and not 0")
