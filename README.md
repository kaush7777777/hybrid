Author: Charitha Kaushalya Jayasinghe

# Hybrid UI-API Testing


## Project Overview

This project performs end-to-end and integration testing for a hybrid UI-API system using `pytest` and Playwright.


### Prerequisites

- Python 3.8+
- Docker (optional)

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/hybrid-ui-api.git
    cd hybrid-ui-api
    ```

2. **Install Python dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

### Running Tests

#### Without Docker

Run the tests locally:

```sh
pytest --env=<environment> --alluredir=./allure-results