
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


#your code go here:
hello = []
for i in my_list:
    if type(i) == dict:
        hello.append(i)
    if type(i) == list:
        hello.append(i)

print(hello)
