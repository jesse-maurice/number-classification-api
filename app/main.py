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
        # Return 400 Bad Request with invalid number in response
        raise HTTPException(
            status_code=400,
            detail={
                "number": number,  # Keep the invalid input in the response
                "error": True,
                "message": "Invalid input. Please provide a numeric value."
            }
        )
    
    # Classify the number
    result = await classifier.classify_number(n)
    return result
