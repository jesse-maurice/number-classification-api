from fastapi import HTTPException
from typing import Union, Dict
from utils import validate_input, format_response
import math
import requests

class NumberClassifier:
    def __init__(self):
        self.numbers_api_url = "http://numbersapi.com/"

    def is_prime(self, n: int) -> bool:
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect(self, n: int) -> bool:
        """Check if a number is perfect."""
        if n < 1:
            return False
        sum_divisors = sum(i for i in range(1, n) if n % i == 0)
        return sum_divisors == n

    def is_armstrong(self, n: int) -> bool:
        """Check if a number is an Armstrong number."""
        num_str = str(abs(n))  # Handle negative numbers
        power = len(num_str)
        return sum(int(digit) ** power for digit in num_str) == abs(n)

    def digit_sum(self, n: int) -> int:
        """Calculate the sum of digits."""
        return sum(int(digit) for digit in str(abs(n)))  # Handle negatives

    def get_properties(self, n: int) -> list:
        """Get all properties of a number."""
        properties = []
        
        if n >= 0:  # Exclude negative numbers from these checks
            if self.is_prime(n):
                properties.append("prime")
            if self.is_perfect(n):
                properties.append("perfect")
            if self.is_armstrong(n):
                properties.append("armstrong")

        properties.append("odd" if n % 2 else "even")
        
        return properties

    async def get_fun_fact(self, n: int) -> str:
        """Get a fun fact about the number."""
        try:
            response = requests.get(f"{self.numbers_api_url}{n}/math")
            return response.text
        except:
            return f"{n} is {'even' if n % 2 == 0 else 'odd'}."

    async def classify_number(self, number: Union[str, int, float]) -> Dict:
        """Classify a number and return all its properties."""
        # Validate the input using the utils function
        is_valid, result = validate_input(str(number))  # Convert number to string for validation

        if not is_valid:
            # If input is invalid, format the error response with number field as invalid input
            return format_response({"number": result, "message": "Invalid input"}, status_code=400)

        n = result  # After validation, `result` will be the valid number

        # Generate properties and facts
        properties = self.get_properties(n)
        fun_fact = await self.get_fun_fact(n)

        # Return the formatted successful response
        return format_response({
            "number": n,
            "is_prime": self.is_prime(n),
            "is_perfect": self.is_perfect(n),
            "properties": properties,
            "digit_sum": self.digit_sum(n),
            "fun_fact": fun_fact
        })
