
from .utils import validate_input, format_response
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .number_classifier import NumberClassifier

app = FastAPI(title="Number Classification API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

classifier = NumberClassifier()

@app.get("/api/classify-number")
async def classify_number(number: str):
    result = await classifier.classify_number(number)
    if "error" in result:
        return result, 400
    return result