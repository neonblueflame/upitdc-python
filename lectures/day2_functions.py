# Multiple arguments, tuple
def print_args(*args):
    print(type(args))
    
    arg1, arg2 = args
    print(arg1, arg2)

print_args(1, 2)
print_args([1, 2, 3], ("a", 1))

# Multiple arguments, dictionary
def print_args2(**args):
    print(type(args))
    print(args)

print_args2(name="Hanger", type="cat")

# Lambda function
nameless_func = lambda x: x ** 2
print(nameless_func(5))

num_list = [1, 2, 3, 4, 5, 6, 7]
print(f"num_list: {num_list}")

# filter() offers an elegant ay to filter out elements of a list; returns boolean True
result = filter(lambda x: x %2 == 0, num_list)
for num in result:
    print(num)