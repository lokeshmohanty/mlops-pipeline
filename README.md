# MLOps : Machine Learning Operations

## Contents

  - Version Control System for Source Code ([git](https://git-scm.com/doc), [github](https://docs.github.com/en))
  - CI/CD ([github-actions](https://docs.github.com/en/actions), [docker](https://docs.docker.com/), [docker-compose](https://docs.docker.com/compose/), [jenkins](https://www.jenkins.io/doc/))
  - Experiment Tracking ([dvc](https://dvc.org/doc), [mlflow](https://mlflow.org/docs/latest/index.html), [wandb](https://docs.wandb.ai/), [clearml](https://clear.ml/docs/latest/docs/))
  - Data VCS ([git-lfs](https://github.com/git-lfs/git-lfs/wiki?utm_source=gitlfs_site&utm_medium=wiki_link&utm_campaign=gitlfs), [dvc](https://dvc.org/doc), [clearml](https://clear.ml/docs/latest/docs/))
  - Model Serving and Monitoring ([grafana](https://grafana.com/docs/grafana/latest/), [prometheus](https://prometheus.io/), [tensorboard](https://www.tensorflow.org/tensorboard))

## Github Actions

**Documentation**: <https://docs.github.com/en/actions>

```yaml
    name: unit-test
    
    on: pull_request
    
    jobs:
      build:
      name: test-pipeline
      runs-on: ubuntu-latest
    
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-python@v4
          with:
            python-version: '3.11'
    
        - name: install deps
          run: pip install flake8 black pytest numpy tensorflow
    
        - name: format
          run: black --check src/
    
        - name: lint
          run: flake8 src/
    
        - name: test
          run: pytest src/tests/*
```

## Simple python app

### Data Collection

Data: <https://keras.io/api/datasets/cifar10/>

### Pre-processing and Model Training

```python
    from tensorflow import keras
    from tensorflow.keras import Sequential, layers
    
    model_filepath = "cifar10.keras"
    
    (train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()
    train_images = train_images.astype('float32') / 255
    test_images = test_images.astype('float32') / 255
    
    num_classes = 10
    train_labels = keras.utils.to_categorical(train_labels, num_classes)
    test_labels = keras.utils.to_categorical(test_labels, num_classes)
    
    model = Sequential()
    
    model.add(layers.Conv2D(32, (3,3), padding='same', activation='relu', input_shape=(32,32,3)))
    model.add(layers.BatchNormalization())
    model.add(layers.Conv2D(32, (3,3), padding='same', activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2,2)))
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(num_classes, activation='softmax'))
    
    model.summary()
    
    model.compile(optimizer='adam', loss=keras.losses.categorical_crossentropy, metrics=['accuracy'])
    
    history = model.fit(train_images, train_labels, batch_size=64, epochs=100,
                        validation_data=(test_images, test_labels))
    
    model.save(model_filepath)
```

### Model Testing

A simple `pytest` example

```python
    def test_always_passes():
        assert True
    
    def test_2_equals_2():
        assert 2 == 2
```

Test model

```python
    import numpy as np
    import tensorflow.keras as keras
    
    model_filepath = "cifar10.keras"
    
    def test_model():
        (_, _), (test_images, test_labels) = keras.datasets.cifar10.load_data()
        test_images = test_images.astype('float32') / 255
        test_labels = keras.utils.to_categorical(test_labels, 10)
    
        model = keras.models.load_model(model_filepath)
        predictions = np.argmax(model.predict(test_images), axis=1)
    
        assert predictions[predictions[0]] == 1
```

### Model Serving

Use fastapi to serve the model

### Model Deployment

Use docker to deploy the application

## Others

  - [Setup docker](./docker.md)
  - [Setup a virtual environment using AWS EC2](./cloud-aws.md)
  - [Use ClearML](./clearml.md)
  - [Setup kubernetes](./kubernetes.md)
