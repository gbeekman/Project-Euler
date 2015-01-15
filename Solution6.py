'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def square_of_sum(n):
	sum_total = (n*(n+1))/2

	return sum_total**2

def sum_of_squares(n):
	sum_total = 0

	while n > 0:
		sum_total = sum_total + n**2
		n = n - 1

	return sum_total


def difference(n):

	return square_of_sum(n) - sum_of_squares(n)