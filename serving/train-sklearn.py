from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_blobs
from joblib import dump
from clearml import Task

task = Task.init(project_name="CIFAR10",
                 task_name="train sklearn model",
                 output_uri=True)

X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)
model = LogisticRegression()
model.fit(X, y)

dump(model, filename="sklearn-model.pkl", compress=9)
