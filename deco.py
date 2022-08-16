# defining a decorator
def hello_decorator(function_to_be_used):

	# inner1 is a Wrapper function in
	# which the argument is called
	
	# inner function can access the outer local
	# functions like in this case "func"
	def inner1():
		print("time 23.31 =====================================================")

		# calling the actual function now
		# inside the wrapper function.
		function_to_be_used()

		print(" time 23.32=================== END ===============================")
	
	# print("Hello 0")
	return inner1


# defining a function, to be called inside wrapper
@hello_decorator
def function_to_be_used():
	print("Dilshad")

# function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()
