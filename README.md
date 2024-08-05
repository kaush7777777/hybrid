Author: Charitha Kaushalya Jayasinghe

# Hybrid UI-API Testing


## Project Overview

This project performs end-to-end and integration testing using pytest and Playwright.


### Prerequisites
2. **Install Python dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Install Playwright and its browsers:**

    ```sh
    pip install playwright
    playwright install
    ```

### Running Tests Without Docker
pytest
pytest -m integration
pytest -m end_to_end

### view Test Reports
allure serve allure-results
