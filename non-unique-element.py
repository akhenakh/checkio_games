

def checkio(data):
	s = set(data)
	result = []
	for i in data:
		if data.count(i) > 1:
			result.append(i)
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
	assert isinstance(checkio([1]), list), "The result must be a list"
	assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
	assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
	assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"