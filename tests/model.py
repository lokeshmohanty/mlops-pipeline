import numpy as np
import tensorflow.keras as keras
from src.run import predict

model = "data/cifar10.keras"
image = "data/peregrine_falcon.jpg"

def test_model():
    (train_images, train_labels), (_, _) = keras.datasets.cifar10.load_data()
    train_images = train_images.astype('float32') / 255

    model = keras.models.load_model(model)
    predictions = np.argmax(model.predict(train_images), axis=1)

    assert predictions[0] == train_labels[0][0]

def test_api():
    assert predict(image, model) == "truck"
