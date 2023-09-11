numbers_list = []

def fun(*args):
    numbers = list(args)
    numbers_list.extend(numbers)


fun(1,2,3)

print(numbers_list)