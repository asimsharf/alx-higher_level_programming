#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
msg1 = "Last digit of"
msg2 = "and is greater than 5"
msg3 = "and is less than 6 and not 0"
if number < 0:
    last = number % -10
else:
    last = number % 10
if last > 5:
    print("{:s} {:d} is {:d} {:s}".format(msg1, number, last, msg2))
elif last == 0:
    print("{:s} {:d} is {:d} and is 0".format(msg1, number, last))
else:
    print("{:s} {:d} is {:d} {:s}".format(msg1, number, last, msg3))
