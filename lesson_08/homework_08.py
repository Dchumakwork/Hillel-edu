lst = ["1,2,3,4", "1,2,3,4,50", "qweurty1,2,3", "2,6,11,30", "12,tet3,66"]

def numbers_sum(list_of_strings: list):
    elements_sum = []
    for string in list_of_strings:
        separated_list = string.split(",")
        try:
            numbers_list = [int(i) for i in separated_list]
            current_sum = sum(numbers_list)
        except:
            current_sum = "Can't do this"
        elements_sum.append(current_sum)
    print(elements_sum)

numbers_sum(lst)