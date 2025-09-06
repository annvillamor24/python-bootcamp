"""
    TODO: Create a function `line_generaator` that has  parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""

# TODO: Use the function once

# def line_generator():
#     print("Line 1")
#     print("Line 2")
#     print("Line 3")
# line_generator()

def line_generator(number):
    for item in range(number):
        print(item)
line_generator(50)