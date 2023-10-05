import numpy as np
import tensorflow.keras as keras

model_filepath = "cifar10.keras"


def test_model():
    (_, _), (test_images, test_labels) = keras.datasets.cifar10.load_data()
    test_images = test_images.astype('float32') / 255

    model = keras.models.load_model(model_filepath)
    predictions = np.argmax(model.predict(test_images), axis=1)

    assert predictions[0] == test_labels[0][0]
