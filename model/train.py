import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset (replace path as needed)
df = pd.read_csv('D:\\AI\\movie-genre-api\\tmdb-movies.csv')
df['genres'] = df['genres'].apply(lambda x: x.split('|')[0] if isinstance(x, str) and x else 'Unknown')
df = df[df['genres'] != 'Unknown']
df = df[['overview', 'genres']].dropna()

X = df['overview']
y = df['genres']

vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression(max_iter=1000)
model.fit(X_vec, y)

os.makedirs('model', exist_ok=True)
joblib.dump(model, 'model/model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')