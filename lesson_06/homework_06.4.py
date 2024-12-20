numbers_list = [1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 100, 111, 120, 145, 170]
summ_even = 0
for i in numbers_list:
    if i%2==0:
        summ_even = summ_even + i
print(summ_even)