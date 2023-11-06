# Parking Prediction API

This repository contains a machine learning model for predicting parking space occupancy and a FastAPI application to serve predictions over HTTP.

## Overview

The `analysis` directory contains all the notebooks, scripts, and data necessary for exploratory data analysis, preprocessing, and model training.

The `app` directory houses the FastAPI application that serves predictions using the trained machine learning model.

## Project Structure

```plaintext
.
├── analysis
│   ├── dataset.csv
│   ├── eda.ipynb
│   ├── feature_names.joblib
│   ├── figures
│   │   ├── occupancy_boxplot.png
│   │   ├── occupancy_by_hour.png
│   │   ├── occupancy_by_weekday.png
│   │   ├── occupancy_distribution.png
│   │   └── occupancy_time_series.png
│   ├── __init__.py
│   ├── model_training.py
│   ├── parking_prediction_model.joblib
│   ├── preprocessing.py
│   ├── preprocessor.joblib
│   ├── test_preprocessed.csv
│   └── train_preprocessed.csv
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── __init__.py
│   │       └── prediction
│   │           ├── __init__.py
│   │           ├── models.py
│   │           ├── routes.py
│   │           └── schemas.py
│   ├── core
│   │   ├── config.py
│   │   ├── __init__.py
│   │   └── logging_config.py
│   ├── db
│   │   ├── base.py
│   │   ├── engine.py
│   │   ├── __init__.py
│   │   └── session.py
│   ├── exceptions
│   │   ├── custom_exceptions.py
│   │   ├── handlers.py
│   │   ├── __init__.py
│   │   └── models.py
│   ├── health
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── __init__.py
│   └── main.py
├── logs
│   ├── error.log
│   ├── info.log
│   └── warning.log
└── requirements.txt


## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL 13+
- Docker and Docker Compose (optional)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/nickmabz/parking-prediction-model.git
    cd fastapi-app-starter-kit
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Copy the .env.example file to .env and update the environment variables:
    ```bash 
    cp .env.example .env
    nano .env  # Or use your favorite text editor
    ```
5. Run the application:
     ```bash 
    uvicorn app.main:app --reload