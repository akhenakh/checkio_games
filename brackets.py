""" You are given an expression with numbers, brackets and operators. 
For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". 
Brackets are used to determine scope or to restrict some expression. If a bracket is open, 
then it must be closed with a closing bracket of the same type. The scope of a bracket must not 
intersected by another bracket. For this task, you should to make a decision to correct an expression 
or not based on the brackets. Do not worry about operators and operands.
Input: An expression with different of types brackets. A string (unicode).
Output: The correctness the expression or don’t. A boolean."""

def checkio(expr):
	par, sq, br = 0, 0, 0
	heap = []
	try:
		for x in expr:
			if x == '(' or x == '[' or x == '{':
				heap.append(x)
			elif x == ')':
				if heap.pop() != '(':
					return False
			elif x == ']':
				if heap.pop() != '[':
					return False
			elif x == '}':
				if heap.pop() != '{':
					return False
	except IndexError:
		return False
	if len(heap):
		return False
	return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
	assert checkio("((5+3)*2+1)") == True, "Simple"
	assert checkio("{[(3+1)+2]+}") == True, "Different types"
	assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
	assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
	assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"