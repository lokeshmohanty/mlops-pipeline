FROM python:3.11

WORKDIR /code

# COPY </path/to/file/local> </path/on/docker-image>
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

EXPOSE 80

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "80"]
