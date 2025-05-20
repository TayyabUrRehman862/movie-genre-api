import joblib
import os
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def load_model():
    model = joblib.load("model/model.pkl")
    vectorizer = joblib.load("model/vectorizer.pkl")
    return model, vectorizer

def predict_genre(text, model, vectorizer):
    X = vectorizer.transform([text])
    probs = model.predict_proba(X)[0]
    genre = model.classes_[np.argmax(probs)]
    confidence = float(np.max(probs))
    return genre, confidence