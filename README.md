# Number Classification API

A RESTful API that analyzes numbers and returns their mathematical properties along with interesting facts.

## Features

- Determines if a number is prime
- Determines if a number is perfect
- Identifies Armstrong numbers
- Calculates digit sum
- Provides odd/even classification
- Includes fun mathematical facts about numbers

## API Endpoint

```
GET /api/classify-number?number=<number>
```

### Success Response (200 OK)

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### Error Response (400 Bad Request)

```json
{
    "number": "alphabet",
    "error": true
}
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn app.main:app --reload
```

## Testing

Run the tests using pytest:
```bash
pytest
```

## Requirements

- Python 3.8+
- FastAPI
- pytest
- requests

## Deployment

The API is deployed at: [Your deployment URL]

## License

MIT License