FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y \
        wget \
        gnupg \
        libnss3 \
        libnspr4 \
        libdbus-1-3 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdrm2 \
        libatspi2.0-0 \
        libxcomposite1 \
        libxdamage1 \
        libxfixes3 \
        libxrandr2 \
        libgbm1 \
        libxkbcommon0 \
        libasound2 \
        libpango-1.0-0 \
        libcairo2 \
        --no-install-recommends && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY tests/ /app/tests
COPY pytest.ini .
RUN pip install playwright && \
    playwright install

RUN pip install allure-pytest