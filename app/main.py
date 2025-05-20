from fastapi import FastAPI
from app.model import load_model, predict_genre
from app.schemas import DescriptionRequest, GenreResponse

app = FastAPI()
model, vectorizer = load_model()

@app.post("/predict", response_model=GenreResponse)
def predict(request: DescriptionRequest):
    genre, confidence = predict_genre(request.description, model, vectorizer)
    return {"genre": genre, "confidence": confidence}