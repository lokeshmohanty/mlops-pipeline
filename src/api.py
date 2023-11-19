from typing import Union
from fastapi import FastAPI, File, UploadFile
from src.run import predict, model

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hi, Hello World! CI/CD is working now. Lets improve it further"}

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    filename = ""
    try:
        contents = file.file.read()
        filename = file.filename
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    try:
        return {"message": "Prediction: " + predict(filename, model)}
    except Exception:
        return {"message": "There was an error during prediction"}
    # finally:
    #     return {"message": f"Successfully uploaded {file.filename}"}
