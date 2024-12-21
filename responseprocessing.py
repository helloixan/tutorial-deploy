import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
import nltk
import random as rd

# import dataset
dataset = pd.read_csv('./data_sentiment.csv')
# print(dataset.info())

# Preprocessing teks
nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))
def preprocess_text(text):
    words = word_tokenize(text)
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower not in stop_words]
    return ' '.join(filtered_words)

dataset['clean_text'] = dataset['text'].apply(preprocess_text)

# pembagian dataset
x_train, x_test, y_train, y_test = train_test_split(dataset['clean_text'], dataset['sentiment'], test_size=0.2, random_state=42)

#TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
x_train_tfidf = tfidf_vectorizer.fit_transform(x_train)
x_test_tfidf = tfidf_vectorizer.transform(x_test)

# Model Naive Bayes
nb_model = MultinomialNB()
nb_model.fit(x_train_tfidf, y_train)

# Evaluasi model
def evaluate() :
    y_pred = nb_model.predict(x_test_tfidf)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    print(f'Accuracy: {accuracy}')
    print(f'Classification Report: {report}')

def predict_sentiment(text):
    cleaned_text = preprocess_text(text)
    vectorized_text = tfidf_vectorizer.transform([cleaned_text])
    prediction = nb_model.predict(vectorized_text)
    return prediction

def bot_response(sentiment):
    sentiments = json.load(open("./response.json"))['sentiments']
    # print(sentiments)
    for sent in sentiments :
        if sent['sentiment'] == sentiment :
            response = rd.choice(sent['responses'])
            return response

def testing():
    user_input = input("You: ")
    sentiment = predict_sentiment(user_input)
    prediction_output = bot_response(sentiment)
    print(f"Bot: {prediction_output}")

def generate_response(user_input):
    sentiment = predict_sentiment(user_input)
    prediction_output = bot_response(sentiment)
    return prediction_output

# evaluate()
# testing()