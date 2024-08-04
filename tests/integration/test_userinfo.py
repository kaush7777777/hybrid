import pytest
from src.user_info import User, dict_to_model, generate_random_user
from unittest.mock import MagicMock

@pytest.mark.integration
def test_create_random_user(api_client, logger):
    user_data = generate_random_user()
    response = api_client.post(f"{api_client.base_url}/users", json=user_data)
    response_json = response.json()
    assert response.status_code == 201
    logger.info(f"Created User: {response_json}")

    created_user = dict_to_model(User, response_json)
    assert created_user.name == user_data['name']
    assert created_user.age == user_data['age']
    assert created_user.gender == user_data['gender']
    assert created_user.address == user_data['address']
    assert created_user.zipcode == user_data['zipcode']
    assert created_user.educationlevel == user_data['educationlevel']

@pytest.mark.integration
def test_get_all_users_save_db(api_client, logger, save_users_to_db):
    response = api_client.get(f"{api_client.base_url}/users")
    response_json = response.json()
    assert response.status_code == 200
    logger.info(f"Response: {response_json}")

    users = [dict_to_model(User, item) for item in response_json]
    # save_users_to_db(users)

    for user in users:
        print(user)

    assert len(users) > 0
    first_user = users[0]
    assert first_user.name is not None
    assert isinstance(first_user.name, str)

@pytest.mark.integration
def test_get_all_users_404(api_client, logger):
    api_client.get = MagicMock(return_value=MagicMock(status_code=404, json=lambda: {}))
    response = api_client.get(f"{api_client.base_url}/users")
    assert response.status_code == 404
    

@pytest.mark.integration
def test_get_all_users_500(api_client, logger):
    api_client.get = MagicMock(return_value=MagicMock(status_code=500, json=lambda: {}))
    response = api_client.get(f"{api_client.base_url}/users")
    assert response.status_code == 500


@pytest.mark.integration
def test_get_all_users_empty_response(api_client, logger):
    api_client.get = MagicMock(return_value=MagicMock(status_code=200, json=lambda: []))
    response = api_client.get(f"{api_client.base_url}/users")
    response_json = response.json()
    assert response.status_code == 200
    logger.info(f"Response: {response_json}")
    users = [dict_to_model(User, item) for item in response_json]
    assert len(users) == 0

@pytest.mark.integration
def test_get_all_users_missing_fields(api_client, logger):
    incomplete_user_data = [{"id": "1", "email": "test@abc.com"}]  # Missing 'name' field
    api_client.get = MagicMock(return_value=MagicMock(status_code=200, json=lambda: incomplete_user_data))
    response = api_client.get(f"{api_client.base_url}/users")
    response_json = response.json()
    assert response.status_code == 200
    logger.info(f"Response: {response_json}")

    users = [dict_to_model(User, item) for item in response_json]
    assert len(users) == 1
    first_user = users[0]
    assert first_user.name is None

@pytest.mark.integration
def test_get_all_users(api_client, logger):
    response = api_client.get(f"{api_client.base_url}/users")
    response_json = response.json()
    assert response.status_code == 200
    response_data = response_json

@pytest.mark.integration
def test_get_user_by_id(api_client, logger, userid=2):
    response = api_client.get(f"{api_client.base_url}/users/{userid}")
    response_json = response.json()
    assert response.status_code == 200
    response_data = response_json