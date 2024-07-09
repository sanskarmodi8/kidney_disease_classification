from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from KidneyDiseaseClassifier.pipeline.prediction import PredictionPipeline
import os
import uvicorn

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.get("/")
async def home():
    return {"message": "Welcome to the Kidney Disease prediction API --by Sanskar Modi", "/train" : "go to this route to start the training pipeline", "/docs" : "go to this route to be able to send post request on route /predict for classification"}

@app.get("/train")
async def trainRoute():
    # os.system("python main.py")
    os.system("dvc repro")
    return "Training done successfully!"

@app.post("/predict")
async def predict_route(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open("inputImage.jpg", "wb") as f:
            f.write(contents)
        clApp = ClientApp()
        result = clApp.classifier.predict()
        result = f"{result}"
        return JSONResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    
    uvicorn.run(app, host="0.0.0.0", port=8080)
