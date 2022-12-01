

from math import sqrt


def checkcomposite(n):
	
	# Check if there is any divisor of n less than sqrt(n)
	for i in range(2,int(sqrt(n))+1,1):
		if (n % i == 0):
			return 1
	return 0

def power(x, y, mod):
	res = 1

	while (y):
		if (y & 1):
			res = (res * x) % mod

		y = y >> 1
		x = (x * x) % mod

	return res

# Function to check for Fermat Pseudoprime
def Check(n,a):
	if (a>1 and checkcomposite(n) and power(a, n - 1, n) == 1):
		return 1

	return 0

if __name__ == '__main__':
    N = int(input("enter N: "))
	#a = int(input("enter A: "))
    input_string = input('Enter possible a: ')
    a = input_string.split()

    print('a[]: ', a)

    nomatch = 1

    for i in range(len(a)):
        if(Check(N, int(a[i]))):
            print(a[i] + " matches")
            nomatch = 0

    if(nomatch):
        print("none of these")
