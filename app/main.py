
from .utils import validate_input, format_response
from fastapi import FastAPI, HTTPException
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
    try:
        # Attempt to convert the input to a float first, then to an integer
        n = float(number)
        n = int(n)  # Truncate to integer
    except (ValueError, TypeError):
        # Return 400 for invalid input (non-numeric)
        raise HTTPException(
            status_code=400,
            detail="Invalid input: must be a valid number"
        )
    
    # Classify the number
    result = await classifier.classify_number(n)
    return result