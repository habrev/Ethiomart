## Task 1: Data Ingestion and Data Preprocessing
### Objective
Set up a data ingestion system to fetch messages from multiple Ethiopian-based Telegram e-commerce channels and prepare the raw data (text, images) for entity extraction.

### Steps
1. **Channel Selection**:
   - Identify and select at least 5 relevant Telegram channels for data collection.
   - Collaborate and share channel lists to gather diverse datasets for fine-tuning.

2. **Data Ingestion**:
   - Develop a custom scraper to connect to the selected Telegram channels.
   - Implement a message ingestion system to collect text, images, and documents in real time.

3. **Text Preprocessing**:
   - Tokenize and normalize text data.
   - Handle Amharic-specific linguistic features, such as unique characters and grammar rules.

4. **Data Cleaning and Structuring**:
   - Remove duplicates, irrelevant content, and noise from the data.
   - Separate metadata (e.g., sender, timestamp) from message content.
   - Structure the data into a unified format for consistency.

5. **Data Storage**:
   - Store preprocessed data in a structured format (e.g., database, JSON files) for further analysis.


# Task-3: Named Entity Recognition (NER) Fine-Tuning for Amharic Telegram Messages

## Objective

This project aims to fine-tune a Named Entity Recognition (NER) model to extract key entities (e.g., products, prices, and locations) from Amharic Telegram messages. The fine-tuning is done using pre-trained models like `bert-tiny-amharic`, `XLM-Roberta`, or `afroxmlr`, which are well-suited for multilingual tasks, including Amharic.

## Setup

### Requirements

- **Google Colab** or any environment with GPU support for faster training.
- **Python 3.x** (preferably 3.7 or higher)
- **CUDA 10.1 or higher** for GPU support (if using local environment).
- **Hugging Face Transformers**
- **Datasets** library

### Install Dependencies



