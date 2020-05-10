myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:
# def increment_by_one(x):
#     new_list = []
#     new_list.append(x * 3)
#     return new_list

# result = list(map(increment_by_one, myNumbers))
# print(result)

def increment_by_one(x):
    return x * 3

new_list = list(map(increment_by_one, myNumbers))
print(new_list)   
