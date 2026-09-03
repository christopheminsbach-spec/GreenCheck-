from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GreenCheck AI Service OK"}