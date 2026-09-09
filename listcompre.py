# number=[1,2,3,4,5]
# new=[i*2 for i in number]
# print(new)

# number=[2,4,6,8,10]
# new=[i*2 for i in number]
# # print(new)

# number=[4,8,12,16,20]
# new=[i*2 for i in number]
# print(new)

# numbers=[x for x in range(1,6)]
# print(numbers)
# output
# [1,2,3,4,5]


# numbers=[1,2,3,4,5,6]
# even=[num for num in numbers if num %2==0]
# print(even)
# [2,4,6]
# numbers greater than 10:-
# numbers=[5,10,15,20,25]
# result=[num for num in numbers if num > 10]
# print(result)
# output
# [15,20,25]
# list comprehension with if....else:-
# Syntax
# new_list=[value if true if condition elsevalue if false for item in iterable ]
# eg:
# even or odd:-
# numbers=[1,2,3,4,5]
# result=["even" if num %2==0 else "odd" for num in numbers]
# print(result)
# output
# ['odd','even','odd','even','odd']
# positive or negative:-
# numbers=[-2,-1,0,3,5]
# result=["positive"if n > 0 else "not positive"for n in numbers]
# print(result)
# output
# ['not positive','not positive','not positive','positive','positive']

