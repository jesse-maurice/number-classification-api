from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
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
        # Try to convert to float, then truncate to integer
        n = float(number)
        n = int(n)
    except (ValueError, TypeError):
        # Raise an HTTPException with status code 400 for invalid input, include the invalid input
        return JSONResponse(
            status_code=400,
            content={
                "number": number,  # Return the invalid input directly
                "error": True
            }
        )

    # Classify the number
    result = await classifier.classify_number(n)
    return result
