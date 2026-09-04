from PIL import Image
import numpy as np


IMG_SIZE = 224


def preprocess_image(image):

    img = Image.open(image).convert("RGB")

    img = img.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(img)

    # normalisation TensorFlow
    img_array = img_array / 255.0

    # ajout dimension batch
    img_array = np.expand_dims(img_array, axis=0)

    return img_array