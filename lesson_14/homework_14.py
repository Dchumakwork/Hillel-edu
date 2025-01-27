class Student:
    def __init__(self, fst_name, sec_name, age, avg_score):
        self.fst_name = fst_name
        self.sec_name = sec_name
        self.age = age
        self.avg_score = avg_score

    def __upd_age(self, new_age):
        self.age = new_age
    # метод валідує зміну віку лише на +1 рік
    def set_new_age(self, value):
        if value - self.age == 1:
            self.__upd_age(value)
        else:
            print(f'Invalid age value. It can be changed only to {self.age + 1}')

    def __upd_avg_score(self, new_value):
        self.avg_score = new_value
    # метод валідує значення допустимих середніх балів
    def set_new_avg(self, value):
        if value in range(1,101):
            self.__upd_avg_score(value)
        else:
            print('Wrong value, average score should be between 1 and 100')


student1 = Student('Ivan', 'Ivanov', 22, 70)
print(f'Name: {student1.fst_name}, age: {student1.age}, avg: {student1.avg_score}')
student1.set_new_age(23)
student1.set_new_avg(80)
print(f'Name: {student1.fst_name}, age: {student1.age}, avg: {student1.avg_score}')
student1.set_new_age(25)
student1.set_new_avg(115)