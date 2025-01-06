def only_strings_finder(some_list: list):
    list_string = []
    for i in some_list:
        if isinstance(i, str):
            list_string.append(i)
    return list_string

def sum_even(some_list: list):
    summ_even = 0
    for i in some_list:
        if i % 2 == 0:
            summ_even = summ_even + i
    return summ_even

def average(arr: list):
    if len(arr)>=1:
        return sum(arr) / len(arr)

def back_string(any_string: str):
    result_string = any_string[::-1]
    return result_string

