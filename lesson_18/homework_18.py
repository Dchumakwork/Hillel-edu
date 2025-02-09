import logging

print(f'{"-"*20} task 1 {"-"*20}')
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)
print(20*"-")

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

for num in fibonacci(21):
    print(num)

print(f'{"-"*20} task 2 {"-"*20}')
class ReverseIterator:
    def __init__(self, lst):
        self.lst = lst[::-1]
        self.index = len(lst)

    def __iter__(self):
        return iter(self.lst)

    def __next__(self):
        if self.index == 0:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
for item in ReverseIterator(my_list):
    print(item)

print(20*"-")

class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num > self.n:
            raise StopIteration
        else:
            result = self.current_num
            self.current_num += 2
            return result

for num in EvenIterator(10):
    print(num)

print(f'{"-"*20} task 3 {"-"*20}')
def log_decorator(func):
    def wrapper(*args):
        result = func(*args)
        logging.info(print(f'Function {func.__name__} with arguments {args} executed with result: {result}'))
        return result
    return wrapper

def exception_handle_decorator(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            print(f'An exception occured: {e}')
            return None
    return wrapper

@log_decorator
@exception_handle_decorator
def calc_sum(num_list: list):
    result = sum(num_list)
    return result

print(calc_sum([1, 8, 3]))
print(calc_sum([1, '9', 3]))