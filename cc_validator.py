def validator(digits):
	checker = digits[-1]
	digits = list(reversed(digits[:-1]))
	for i in range(0, len(digits), 2):
		if digits[i] * 2 > 9:
			digits[i] *= 2
			digits[i] -= 9
		else:
			digits[i] *= 2
	summation = sum(digits)
	return checker == summation * 9 %10


def init_digit(string):
	if type(string) == type('str') or type(string) == type(1):
		string = str(string)
		digits = []
		for digit in string:
			digits.append(int(digit))
		return digits
	else:
		raise ValueError('input has wrong format')

# loop to generate all the possible credit card numbers
am = 4000236000000039

def generate_cc(template):
	possible = []
	template = str(template)
	prefix = template[0]
	suffix = template[4:]
	for i in range(0, 10):
		for j in range(0, 10):
			for k in range(0, 10):
				poss = prefix + str(i) + str(j) + str(k) + suffix
				possible.append(poss)
	return possible

all_possible = generate_cc(am)

all_verified = []
for poss in all_possible:
	if validator(init_digit(poss)):
		all_verified.append(poss)

print len(all_verified)
print all_verified
