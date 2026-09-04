from fastapi import FastAPI, UploadFile, File  # pyright: ignore[reportMissingImports]

from app.predict import predict_image


app = FastAPI(

title="GreenCheck AI API",

version="1.0"

)



@app.get("/")
def home():

    return {

        "status":
        "GreenCheck AI running"

    }



@app.post("/predict")
async def predict(

    image:UploadFile = File(...)

):


    result = predict_image(image)


    return result