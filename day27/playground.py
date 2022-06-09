# def add(*args):
#     sum = 0
#     for n in args:
#         sum = sum + n
#     return sum

# print(add(1,2,3,4,5))
def add(*args):
   for n in args:
       print(args)

add(1,2,3,4,5)

# from numpy import multiply


# def calculate(**kwargs):
#     print(type(kwargs))


# calculate(add=3,multiply=5)