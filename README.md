# LLM-RegBERT Log Classifier

This repository contains a log classification system that processes log files using multiple techniques including regex matching, machine learning with BERT embeddings, and language model-based classification. The system exposes a RESTful API built with FastAPI and provides a web interface via Streamlit for file uploads and results download.

## Overview

The Log Classification System is designed to:

- Process CSV files containing log messages.
- Classify each log using three approaches:
  - **Regex-based matching:** Uses predefined patterns to classify logs.
  - **BERT-based classification:** Uses sentence embeddings with a trained logistic regression.
  - **LLM-based classification:** Utilizes **Groq LLM** for contextual classification.
- Uses **DBSCAN clustering** to identify patterns in logs.
- Provide a **FastAPI** endpoint for file uploads and classification.
- Allow users to interact with the service via a **Streamlit** interface.
- Include a training pipeline using **embeddings** and **logistic regression** for model updates.

## Project Structure

```
Log-classification
├── models
│   └── log_classifier.joblib
├── resources
│   ├── test.csv
│   └── workflow.png
├── training
│   ├── dataset
│   │   └── synthetic_logs.csv
│   └── log_classification.ipynb
├── .env
├── .gitignore
├── app.py
├── classify.py
├── output.csv
├── processor_bert.py
├── processor_llm.py
├── processor_regex.py
├── README.md
├── requirements.txt
└── server.py

```

## Prerequisites

- Python 3.11.9
- [pip](https://pip.pypa.io/en/stable/)
- Environment variables set in the `.env` file (e.g., `GROQ_API_KEY` for LLM API access)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/mannan-123/LLM-RegBERT-Log-Classifier.git
   cd LLM-RegBERT-Log-Classifier
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix or MacOS
   source venv/bin/activate
   ```

3. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Running the API Server

Start the FastAPI server using:

```sh
uvicorn server:app
```

The API will be accessible at `http://127.0.0.1:8000`.

### Using the Streamlit Interface

To launch the web interface for file uploads and classification:

```sh
streamlit run app.py
```

### Training and Model Generation

Model training is demonstrated in the Jupyter notebook in the `training` directory ([log_classification.ipynb](training/log_classification.ipynb)). The training pipeline:

- Loads synthetic logs from `training/dataset/synthetic_logs.csv`.
- Generates embeddings using a Sentence Transformer.
- Applies clustering with DBSCAN.
- Splits data for logistic regression training.
- Saves the trained model in `models/log_classifier.joblib`.

## API Endpoints

- **POST /classify/**
  - **Description:** Accepts a CSV file with log messages, processes it, and returns a CSV with an additional `target_label` column.
  - **Expected CSV format:** Must contain `source` and `log_message` columns.

## File Descriptions

- **app.py:** FastAPI application handling CSV uploads and log classification.
- **classify.py:** Main script that combines the processing pipelines.
- **processor_regex.py:** Contains the regex-based classification logic.
- **processor_bert.py:** Uses BERT embeddings for log classification.
- **processor_llm.py:** Integrates an LLM to classify logs for legacy systems.
- **server.py:** An alternative entry point for running the server.
- **models/log_classifier.joblib:** Pre-trained machine learning model used by the BERT processor.
- **training/log_classification.ipynb:** Notebook for training the classification model.
- **resources/test.csv:** Sample input CSV file.
