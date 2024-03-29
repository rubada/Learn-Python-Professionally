# lambda anonymous functions
# Lambda is an anonymous function because it doesn't have a name, it can take
# many arguments, but it has one expression which is evaluated and returned.
# Instead of using def to define the function, the lambda keyword is used.
# Syntax
# lambda arguments: expression
# Example:

hello = lambda: "Hello World"
# print(hello())


# Using lambda with arguments
add = lambda x, y: x + y
# print(add(4, 5))


# Using with if statements
max_num = lambda x, y: x if x > y else y
# print(max_num(4, 8))


# As Shown above when using flake8, (flake8 is a Python tool used to check
# the style and quality of the Python code), flake8 will give an error when
# assigning lambda to a variable. Because when debugging the code the lambdas
# will be shown as <lambda> in tracebacks (tracing the same name), where
# functions will display the function’s name. Although this will not give an
# error when running the code, it will raise a debugging issue when
# defining many lambdas. In this case, it is better to define a function
# (def funcname) instead of using the lambda keyword.


# In the next section, we will show how to use lambda with list comprehensions
# and higher-order built-in functions.
