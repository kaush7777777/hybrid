import pytest
import logging
from playwright.sync_api import sync_playwright
import requests
import sqlite3

def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )

setup_logging()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging", help="Environment to run tests against: staging, sandbox, production")

@pytest.fixture(scope="session")
def env(request):
    return request.config.getoption("--env")

@pytest.fixture(scope="session")
def logger():
    return logging.getLogger("pytest")

@pytest.fixture(scope="function")
def playwright_browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def home_page(playwright_browser, env):
    urls = {
        "staging": "https://openweathermap.org/",
        "sandbox": "https://sandbox.openweathermap.org/",
        "production": "https://openweathermap.org/"
    }
    page = playwright_browser.new_page()
    page.goto(urls[env])
    yield page
    page.close()

@pytest.fixture(scope="function")
def api_client(env):
    base_urls = {
        "staging": "https://66a5dbb423b29e17a1a11afc.mockapi.io/v1",
        "sandbox": "https://sandbox-api.example.com/v1",
        "production": "https://production-api.example.com/v1"
    }
    client = requests.Session()
    client.base_url = base_urls[env]
    return client

@pytest.fixture(scope="function")
def setup_db():
    """Fixture to setup database connection and schema."""
    conn = sqlite3.connect('ckdb.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            db_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age TEXT,
            gender TEXT,
            address TEXT,
            zipcode TEXT,
            educationlevel TEXT,
            userid TEXT UNIQUE,
            rawjson TEXT
        )
    ''')
    conn.commit()
    yield conn
    conn.close()

@pytest.fixture(scope="function")
def save_users_to_db(setup_db):
    """Fixture to save users to the database."""
    conn = setup_db
    cursor = conn.cursor()

    def save_users(users):
        try:
            for user in users:
                cursor.execute("""
                    INSERT INTO user (name, age, gender, address, zipcode, educationlevel, userid, rawjson)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (user.name, user.age, user.gender, user.address, user.zipcode, 
                      user.educationlevel, user.id, user.rawjson))
            conn.commit()
        except Exception as e:
            logging.error(f"Error saving users to DB: {e}")
            conn.rollback()
    
    return save_users