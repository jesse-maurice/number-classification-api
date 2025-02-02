from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .number_classifier import NumberClassifier
from .utils import validate_input, format_response

app = FastAPI(title="Number Classification API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

classifier = NumberClassifier()

@app.get("/api/classify-number")
async def classify_number(number: str):
    # Validate the input using the validate_input function from utils
    is_valid, result = validate_input(number)
    
    if not is_valid:
        # If input is invalid, format and return the error response with status code 400
        return format_response({"number": result, "message": "Invalid input"}, status_code=400)
    
    # If input is valid, classify the number and return the result
    result = await classifier.classify_number(result)
    return result
