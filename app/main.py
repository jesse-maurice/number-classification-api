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
        n = float(number)
        n = int(n)  # Convert to integer
    except (ValueError, TypeError):
        raise HTTPException(status_code=400, detail="Invalid input. Must be a numeric value.")

    result = await classifier.classify_number(n)
    return result
