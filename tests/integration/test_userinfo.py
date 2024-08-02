import pytest
from src.user_info import User
import requests
import json


@pytest.mark.integration
def test_get_all_users_save_db(api_client, logger, save_users_to_db):
    response = api_client.get("https://66a5dbb423b29e17a1a11afc.mockapi.io/v1/users")
    response_json = response.json()
    assert response.status_code == 200
    logger.info(f"API Response: {response_json}")

    users = [dict_to_model(User, item) for item in response_json]

    save_users_to_db(users)

    for user in users:
        print(user)

    assert len(users) > 0 

    first_user = users[0]
    assert first_user.name is not None 
    assert isinstance(first_user.name, str) 

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

def dict_to_model(model_class, data_dict):
    """ Convert a dictionary to an instance of the given model class. """
    model_args = {
        'name': data_dict.get('name'),
        'age': data_dict.get('age'),
        'gender': data_dict.get('gender'),
        'address': data_dict.get('address'),
        'zipcode': data_dict.get('zipcode'),
        'educationlevel': data_dict.get('educationlevel'),
        'userid': data_dict.get('id'),  
        'rawjson': json.dumps(data_dict)
    }
    return model_class(**model_args)