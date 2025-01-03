# Sentiment Analysis of Product Reviews (Backend)

This repository provides a backend implementation for performing sentiment analysis on product reviews using a Flask-based API. The backend processes user inputs, cleans the text data, and predicts the sentiment (positive or negative) using a pre-trained LSTM model.

---

## Features
- **Flask API**:
  - `/`: Test route that returns a simple "Hello World" message.
  - `/data` (GET): Returns a sample review and prediction.
  - `/predict` (POST): Accepts a product review and returns the sentiment and polarity score.
- **Pre-trained Model**: Uses TensorFlow for sentiment prediction.
- **Custom Text Preprocessing**: Includes stop-word removal, tokenization, and input padding.
- **Singleton Design**: Ensures efficient model and tokenizer loading.

---

## Folder Structure
```plaintext
api/
├── app.py            # Flask API routes
├── data_loader.py    # Model and tokenizer loading
├── data_predict.py   # Text preprocessing and prediction logic
├── requirements.txt  # Python dependencies
├── stop_words.txt    # Custom stopword list
├── tokenizer.pkl     # Pre-trained tokenizer
├── vercel.json       # Deployment configuration (for Vercel)
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd sentiment-analysis-of-product-reviews-backend/api
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
3. Run the Flask app
   ```bash
   python app.py
   ```
   The app will be available at `http://localhost:5000`

---

## API Endpoints

1. `/` (GET): Test endpoint.
- Response :
    ```json
    "Hello World"
    ```
2. `/data` (GET): Returns a sample review and prediction.
- Response :
     ```json
     {
       "review": "sample review",
       "prediction": "negative"
     }
     ```
3. `/predict` (POST): Accepts a product review and returns the sentiment and polarity score.'
- Response :
    ```json
    {
      "review": "your review",
      "prediction": "positive / negative"
    }
    ```
    
