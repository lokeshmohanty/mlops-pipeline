FROM python:3.11

WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

WORKDIR /code/src
COPY ./src/train.py .
RUN cd ../ && python src/train.py
COPY ["src/api.py", "src/run.py", "src/__init__.py", "./"]

EXPOSE 8080
WORKDIR /code
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8080"]
