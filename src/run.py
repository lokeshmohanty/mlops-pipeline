import numpy as np
from tensorflow import keras
from PIL import Image

model = "data/cifar10.keras"
labels = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def predict(image, model):
    image = np.array(Image.open(image).resize((32, 32))).reshape(1, 32, 32, 3)
    model = keras.models.load_model(model)
    prediction = np.argmax(model.predict(image), axis=1)
    return labels[prediction[0]]
