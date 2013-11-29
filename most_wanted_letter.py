from collections import defaultdict

def checkio(text):
	d = defaultdict(int)
	for x in text.lower():
		d[x] += 1

	max=0
	letter_max = ""
	for k in d.keys():
		if d[k] >= max:
			max = d[k]
			letter_max = k

	return letter_max

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("Hello World!") == "l", "Hello test"
	assert checkio("How do you do?") == "o", "O is most wanted"
	assert checkio("One") == "e", "All letter only once."