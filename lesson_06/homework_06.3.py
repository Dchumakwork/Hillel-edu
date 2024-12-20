lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list_string = []
list_others = []
for i in lst1:
    if isinstance(i, str):
        list_string.append(i)
    else:
        list_others.append(i)

print(list_string)
print(list_others)

