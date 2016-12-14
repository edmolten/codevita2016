import math as m
number = input()
test = False
for i in number:
	if i == ".":
		test = True
		break
if not(test):
	number += "."

snumber = number.split(".")

numberLeft = snumber[0]
numberRight = snumber[-1]


divisor = "0"
summ = "0"
quotient = "0"
remainder = "0"
dividend = "0"

def zeroLeft(number):
	if len(number)%2 != 0:
		ret = "0"
	else:
		ret = ""
	return ret + number

def zeroRight(number):
	n = len(number)
	if 6 > n:
		ret = "0"*int(6-n)
	elif n%2 != 0:
		ret = "0"*(n%2)
	else:
		ret = ""
	return number + ret

def nexPairLeft(number):
	return number[0:2], number[2:]

def findNearSqrt(number):
	return str(int(m.sqrt(int(number))))

def findNumber(summ, remainder):
	n = int(remainder)
	for x in range(1,10):
		if int(summ+str(x)) * x > n:
			return str(x - 1)
	return "9"

numberLeft = zeroLeft(numberLeft)
numberRight = zeroRight(numberRight)

# First step
pair, numberLeft = nexPairLeft(numberLeft)
divisor = findNearSqrt(pair)
dividend = pair
quotient = divisor
summ = str(int(divisor)*2)
remainder = str(int(pair) - int(quotient)**2)

while len(numberLeft) > 0 and int(remainder) != 0:
	pair, numberLeft = nexPairLeft(numberLeft)
	dividend = remainder + pair
	i = findNumber(summ, dividend)
	quotient = quotient + i

	divisor = summ + i
	summ = str(int(summ + i) + int(i))

	remainder = str(int(dividend) - int(divisor)*int(i))

quotient = quotient + "."

while len(numberRight) > 0 and int(remainder) != 0:
	pair, numberRight = nexPairLeft(numberRight)
	dividend = remainder + pair
	i = findNumber(summ, dividend)
	quotient = quotient + i

	divisor = summ + i
	summ = str(int(summ + i) + int(i))

	remainder = str(int(dividend) - int(divisor)*int(i))

print(dividend, divisor, quotient, remainder, summ)