some_str = input("Type something here ")
unique_amount = 0
unique_symbols = []
for i in some_str:
    if i not in unique_symbols:
        unique_symbols.append(i)
        unique_amount = unique_amount+1
if unique_amount > 10:
    print(True)
    print(f"The amount of unique symbols is {unique_amount}")
else:
    print(False)
    print(f"The amount of unique symbols is {unique_amount}")
