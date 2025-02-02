class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
     def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Employee):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(name, salary)
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size

def test_teamlead_attributes():

    team_lead = TeamLead(
        name='John Doe',
        salary=5300,
        department='Software Development',
        programming_language='Python',
        team_size=8
    )

    assert hasattr(team_lead, 'name'), "TeamLead має мати атрибут 'name' із класу Employee"
    assert hasattr(team_lead, 'salary'), "TeamLead має мати атрибут 'salary' із класу Employee"
    assert hasattr(team_lead, 'department'), "TeamLead має мати атрибут 'department' із класу Manager"


    assert hasattr(team_lead,
                   'programming_language'), "TeamLead має мати атрибут 'programming_language' із класу Developer"

    print('Усі атрибути успішно перевірені!')

test_teamlead_attributes()