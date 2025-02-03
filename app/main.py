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
        # Convert to float, then truncate to integer
        n = float(number)
        n = int(n)
    except (ValueError, TypeError):
        # Raise HTTPException with status code 400 for invalid input, including the invalid number
        if number.isalpha():  # Check if input is alphabetic
            input_type = "alphabet"
        else:
            input_type = "unknown"  # Fallback for other invalid types (e.g., special characters)


        raise HTTPException(
            status_code=400,
            detail={
                "number": input_type,  # Include the invalid input in the response
                "error": True,
            }
        )
    
    # Classify the number
    result = await classifier.classify_number(n)
    return result
