# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
from math import trunc

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
# 6 10 13 > 30y
people_records.insert(0, ('Dmytro', 'Chumak', 33, 'QAE', 'Kyiv'))
a = people_records[1]
people_records[1] = people_records[5]
people_records[5] = a
print(people_records)

# функція приймає 3 аргументи: список людей, список з індексами потрібних записів та вік для порівняння і виводить відповідь перевірки
def check_people(people_list: list, peopl_to_comp: list, age: int):
    check_result = True
    for i in range(len(peopl_to_comp)):
        if people_list[peopl_to_comp[0]][2]>age:
            continue
        else:
            check_result = False
            break
    if check_result:
        print(f"All chosen people are older than {age} years.")
    else:
        print(f"Some of chosen people are yanger than {age} years.")

    return

check_people(people_records, [6,10,13], 30)
check_people(people_records, [1,6,10,13], 30)