
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import pickle

app = FastAPI()

# Load templates
templates = Jinja2Templates(directory="templates")

# Load ML model safely
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    text = data.get("text", "")

    if not text.strip():
        return JSONResponse({"prediction": "No text provided"})

    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]

    result = "Fake News" if prediction == 0 else "Real News"

    return JSONResponse({"prediction": result})
