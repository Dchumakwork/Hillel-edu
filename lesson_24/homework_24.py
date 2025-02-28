import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("test_logger")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("test_search.log")
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

@pytest.fixture(scope="class")
def session():
    # Fixture for session with authentication

    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"
    credentials = {"username": "test_user", "password": "test_pass"}

    response = session.post(auth_url, json=credentials, auth=HTTPBasicAuth('test_user',
                                                                           'test_pass'))
    logger.info(f"POST request to {auth_url} returned status {response.status_code}")

    assert response.status_code == 200, "Authentication failed"

    access_token = response.json().get("access_token")
    assert access_token, "Token is not received"
    logger.info(f"Access token: {access_token}")
    session.headers.update({'Authorization': 'Bearer ' + access_token})

    return session


@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 1),
        ("brand", 30),
        ("price", 0),
        ("brand", None),
        (None, 10),
    ]
)
class TestCarsApp:
    def test_search_cars(self, session, sort_by, limit):
        # Testing cars search with different parameters

        search_url = f"{BASE_URL}/cars"
        params = {}

        response = session.get(search_url)
        data = response.json()
        max_limit = len(data)

        if sort_by:
            params["sort_by"] = sort_by
        if limit is not None:
            params["limit"] = limit

        response = session.get(search_url, params=params)

        # Results logging
        log_message = (f"GET request to {search_url} with params={params} returned status {response.status_code} "
                       f"and response {response.json()}")
        logger.info(log_message)
        print(log_message)

        assert response.status_code == 200, f"Expected code 200, but got {response.status_code}"
        data = response.json()
        assert isinstance(data, list), "The result should be a list"
        if limit is not None and 0 < limit <= max_limit:
            assert len(data) == limit, f"{limit} result(s) was/were expected, but it equal to {len(data)}"