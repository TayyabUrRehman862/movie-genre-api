# 🎬 Movie Genre Classifier API
![CI](https://github.com/TayyabUrRehman862/movie-genre-api/actions/workflows/main.yml/badge.svg)
An ML-powered REST API that predicts a movie's genre based on its plot summary. Built with **FastAPI**, **scikit-learn**, and **CI/CD using GitHub Actions**.

---

## 🚀 Features

- ✅ Predicts genre (Action, Comedy, Drama, etc.) from a movie description
- 🧠 Trained on the TMDB 5000 Movie Dataset
- ⚙️ Built with FastAPI + scikit-learn
- 🔁 Includes a model training pipeline.
- 🧪 Unit-tested with pytest.
- 📦 Docker-ready + CI/CD via GitHub Actions.

---

## 📦 Tech Stack

- **Backend**: FastAPI
- **ML Model**: Logistic Regression (scikit-learn)
- **Data**: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **DevOps**: GitHub Actions, Docker (optional)

---

## 📊 Model Overview

- Inputs: Movie `overview` (plot)
- Outputs: Predicted `genre`
- Model: TF-IDF + Logistic Regression

---

## 🛠️ How to Run

### 1. Clone the repo

```bash
git clone https://github.com/TayyabUrRehman862/movie-genre-api.git
cd movie-genre-api

```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Train the model
```bash
python model/train.py
```
### Run the api
```bash
uvicorn app.main:app --reload
```
![image](https://github.com/user-attachments/assets/b7422ce7-3d69-471f-bc85-6778bae0a20f)

### Running tests
```bash
pytest.py
```
### Docker Support
```bash
docker build -t movie-genre-api .
docker run -p 8000:8000 movie-genre-api
```
### Author
Tayyab ur Rehman





