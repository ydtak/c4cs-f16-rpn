#!/usr/bin/env python3

import operator
import readline


help_message = """
'a': use last result output
'q': quit
"""

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod
}

def help():
	print(help_message)

def calculate(myarg, last_result = 0):
	stack = []
	for token in myarg.split():
		if token == 'a':
			stack.append(last_result)
			continue
		try:
			token = int(token)
			stack.append(token)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1, arg2)
			stack.append(result)
		print(stack)
	if len(stack) != 1:
		raise TypeError("Too many parameters!")
	return stack.pop()

def main():
	result = 0
	finished = False
	while not finished:
		cmd = input("rpn calc ('h' for help)> ")
		if cmd == 'h':
			help()			
		elif cmd == 'q':
			return 0
		else:
			result = calculate(cmd, result)
			print("Result: ", result)


if __name__ == "__main__":
	main()
