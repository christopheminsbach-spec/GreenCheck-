from importlib import import_module

from app.preprocessing import preprocess_image


MODEL_PATH = "models/plant_model.keras"


model = None


def _get_model():
    global model

    if model is None:
        tensorflow = import_module("tensorflow")
        model = tensorflow.keras.models.load_model(MODEL_PATH)

    return model


classes = [
    "Rose",
    "Tulipe",
    "Marguerite",
    "Orchidée"
]


def predict_image(image):


    return {


        "prediction":
        "healthy",


        "confidence":
        0.95,


        "advice":
        "Votre plante semble saine"

    }
