import math


def isPrime(num):
	if num > 1:
		for i in range(2, num):
			if(num % i == 0):
				return False
	return True

def findTwoNumbers(num):
	numsqrt = math.sqrt(num)
	if(isPrime(num)):
		num2 = (int(numsqrt)+1)
		return [num2, num2, num-num2**2]
	min_pair = [1, num, 0]
	for i in range(1,int(numsqrt)+1):
		if num % i == 0 and abs(min_pair[0]-min_pair[1])>abs(i-num/i):
			min_pair = [i, int(num/i), 0]

	return min_pair