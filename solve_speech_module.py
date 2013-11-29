FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
						 "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
							"sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
							"eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
	res = ""
	if number >= 100:
		res = FIRST_TEN[int(number/100)] + " hundred "
		number -= int(number / 100) * 100
 
	if number >= 20:
		res += OTHER_TENS[int(number/10) - 2] + " "
		number -= int(number / 10) * 10 

	if number >= 10:
		res += SECOND_TEN[number-10] + " "
	elif number > 0:
		res += FIRST_TEN[number]
	
	return res.strip()

print(checkio(400))
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio(4) == 'four', "1st example"
	assert checkio(133) == 'one hundred thirty three', "2nd example"
	assert checkio(12) == 'twelve', "3rd example"
	assert checkio(101) == 'one hundred one', "4th example"
	assert checkio(212) == 'two hundred twelve', "5th example"
	assert checkio(40) == 'forty', "6th example"