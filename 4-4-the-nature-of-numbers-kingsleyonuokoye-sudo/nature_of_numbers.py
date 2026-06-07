import math


def is_even(n: int) -> bool:
	return n % 2 == 0


def is_perfect_square(n: int) -> bool:
	if n < 0:
		return False
	root = int(math.isqrt(n))
	return root * root == n


def factors(n: int) -> list[int]:
	n_abs = abs(n)
	res = []
	for i in range(1, int(math.sqrt(n_abs)) + 1):
		if n_abs % i == 0:
			res.append(i)
			j = n_abs // i
			if j != i:
				res.append(j)
	return sorted(res)


def main() -> None:
	while True:
		print("Please enter a whole number")
		try:
			s = input().strip()
			num = int(s)
		except (ValueError, EOFError):
			print("Invalid input. Please enter a whole number")
			continue

		if is_even(num):
			print(f"{num} is an even number.")
		else:
			print(f"{num} is an odd number.")

		if is_perfect_square(num):
			print(f"{num} has a perfect square root.")
		else:
			print(f"{num} does not have a perfect square root.")

		facs = factors(num)
		# print factors as comma-separated values with no spaces to match tests
		print(",".join(str(x) for x in facs))

		print("Would you like to enter another number? (Y/N)")
		try:
			again = input().strip()
		except EOFError:
			again = 'n'

		if not again or again[0].lower() != 'y':
			print("Thank you for playing!")
			break


if __name__ == '__main__':
	main()