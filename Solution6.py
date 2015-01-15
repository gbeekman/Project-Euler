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