from homework_16 import TeamLead
import pytest

@pytest.mark.parametrize('name, salary, department, programming_language, team_size', [
    ('Petro', 5300, 'Software Development', 'Python', 8),
    ('Anna', 4800, 'AQA', 'Python', 3),
    ('Ivan', 2000, 'DevOps', 'JS', 3),
])
def test_teamlead_attributes(name, salary, department, programming_language, team_size):
    team_lead = TeamLead(
        name=name,
        salary=salary,
        department=department,
        programming_language=programming_language,
        team_size=team_size
    )
    # Manager class attributes checking
    assert hasattr(team_lead, 'name'), "TeamLead should have a 'name' attribute from Employee class"
    assert hasattr(team_lead, 'salary'), "TeamLead should have a 'salary' attribute from Employee class"
    assert hasattr(team_lead, 'department'), "TeamLead should have a 'department' attribute from Manager class"

    # Developer class attributes checking
    assert hasattr(team_lead, 'programming_language'), "TeamLead should have a 'programming_language' attribute from Developer class"

    print('TeamLead class has all necessary attributes ')