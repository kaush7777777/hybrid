import json
from faker import Faker

class User:
    def __init__(self, name, age, gender, address, zipcode, educationlevel, userid, rawjson, db_id=None):
        self._name = name
        self._age = age
        self._gender = gender
        self._address = address
        self._zipcode = zipcode
        self._educationlevel = educationlevel
        self._id = userid  # `userid` from JSON response
        self._rawjson = rawjson
        self._db_id = db_id  # Primary key for the database

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    @property
    def address(self):
        return self._address

    @property
    def zipcode(self):
        return self._zipcode

    @property
    def educationlevel(self):
        return self._educationlevel

    @property
    def id(self):
        return self._id

    @property
    def rawjson(self):
        return self._rawjson

    @property
    def db_id(self):
        return self._db_id

    @classmethod
    def from_json(cls, json_data):
        data = json.loads(json_data)
        return cls(
            name=data.get("name"),
            age=data.get("age"),
            gender=data.get("gender"),
            address=data.get("address"),
            zipcode=data.get("zipcode"),
            educationlevel=data.get("educationlevel"),
            userid=data.get("id"),
            rawjson=json_data
        )

    def __repr__(self):
        return (f"User(name={self._name}, age={self._age}, gender={self._gender}, "
                f"address={self._address}, zipcode={self._zipcode}, "
                f"educationlevel={self._educationlevel}, userid={self._id}, "
                f"db_id={self._db_id}, rawjson={self._rawjson})")


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

def generate_random_user():

    fake = Faker()

    return {
        "name": fake.name(),
        "age": str(fake.random_int(min=18, max=90)),
        "gender": fake.random_element(elements=("male", "female", "other")),
        "address": fake.address(),
        "zipcode": fake.zipcode(),
        "educationlevel": fake.random_element(elements=("high school", "associate", "bachelor", "master", "doctorate"))
    }