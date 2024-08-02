import pytest
from src.user_info import User
from src.user_info import dict_to_model
import requests
import json

import pytest
from unittest.mock import MagicMock


@pytest.mark.integration
def test_get_all_users_save_db(api_client, logger, save_users_to_db):
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users")
    response_json = response.json()
    assert response.status_code == 200
    logger.info(f"Response: {response_json}")

    users = [dict_to_model(User, item) for item in response_json]

    save_users_to_db(users)
    

    for user in users:
        print(user)

    assert len(users) > 0 

    first_user = users[0]
    assert first_user.name is not None 
    assert isinstance(first_user.name, str) 

@pytest.mark.integration
def test_get_all_users_404(api_client, logger):
    api_client.get = MagicMock(return_value=MagicMock(status_code=404, json=lambda: {}))
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users")
    assert response.status_code == 404
    logger.error("API returned 404 Not Found")

@pytest.mark.integration
def test_get_all_users_500(api_client, logger):
    api_client.get = MagicMock(return_value=MagicMock(status_code=500, json=lambda: {}))
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users")
    assert response.status_code == 500
    logger.error("API returned 500 Internal Server Error")

@pytest.mark.integration
def test_get_all_users_empty_response(api_client, logger):
    api_client.get = MagicMock(return_value=MagicMock(status_code=200, json=lambda: []))
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users")
    response_json = response.json()
    assert response.status_code == 200
    logger.info(f"Response: {response_json}")
    users = [dict_to_model(User, item) for item in response_json]
    assert len(users) == 0
    logger.error("API returned an empty response")

@pytest.mark.integration
def test_get_all_users_missing_fields(api_client, logger):
    incomplete_user_data = [{"id": "1", "email": "test@example.com"}]  # Missing 'name' field
    api_client.get = MagicMock(return_value=MagicMock(status_code=200, json=lambda: incomplete_user_data))
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users")
    response_json = response.json()
    assert response.status_code == 200
    logger.info(f"Response: {response_json}")

    users = [dict_to_model(User, item) for item in response_json]
    assert len(users) == 1
    first_user = users[0]
    assert first_user.name is None
    logger.error("API returned user data with missing fields")

@pytest.mark.integration
def test_get_all_users(api_client, logger):
 
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users")
    response_json = response.json()
    assert response.status_code == 200
    response_data = response_json



@pytest.mark.integration
def test_get_user_by_id(api_client, logger, userid=1003):
 
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users/"+str(userid))
    response_json = response.json()
    assert response.status_code == 200
    response_data = response_json

