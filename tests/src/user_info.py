import json

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