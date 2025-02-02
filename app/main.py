# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .number_classifier import NumberClassifier

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
    try:
        # Attempt to convert the input to a float first, then to an integer
        n = float(number)
        n = int(n)  # Truncate to integer
    except (ValueError, TypeError):
        # Return 400 for invalid input (non-numeric)
        return {
            "number": number,  # Invalid input, return as string
            "error": True
        }
    
    # Classify the number
    result = await classifier.classify_number(n)
    return result