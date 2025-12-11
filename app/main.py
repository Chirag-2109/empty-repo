from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "FastAPI CI/CD app is running"}

@app.get("/predict")
def predict():
    return {"prediction": "class_A", "confidence": 0.95}
