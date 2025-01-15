from homework_10 import log_event
import pytest

def get_last_log():
    with open('login_system.log', 'r') as log_file:
        for line in log_file:
            pass
        last_log = line
    log_file.close()
    return last_log

@pytest.mark.parametrize('username', ['Petro', "Anna", 'Ivan'])
def test_log_success(username, status="success"):
    log_event(username, status)
    current_log_message = f"Login event - Username: {username}, Status: {status}"
    assert current_log_message in get_last_log()

@pytest.mark.parametrize('username', ['Olha', "Inna", 'Andrew'])
def test_log_expired(username, status="expired"):
    log_event(username, status)
    current_log_message = f"Login event - Username: {username}, Status: {status}"
    assert current_log_message in get_last_log()

@pytest.mark.parametrize('username', ['Natalia', "Oleh", 'Dimon'])
def test_log_failed(username, status="failed"):
    log_event(username, status)
    current_log_message = f"Login event - Username: {username}, Status: {status}"
    assert current_log_message in get_last_log()