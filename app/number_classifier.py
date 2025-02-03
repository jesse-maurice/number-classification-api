from typing import List, Dict, Union
import math
from fastapi import HTTPException
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

    def get_properties(self, n: int) -> List[str]:
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
        try:
            n = int(float(number))
            properties = self.get_properties(n)

            return {
                "number": n,
                "is_prime": self.is_prime(n) if n >= 0 else False,
                "is_perfect": self.is_perfect(n) if n >= 0 else False,
                "properties": properties,
                "digit_sum": self.digit_sum(n),
                "fun_fact": await self.get_fun_fact(n)
            }
        except (ValueError, TypeError):
            raise HTTPException(
                status_code=400, 
                detail={
                    "number": number,  # Include the invalid input
                    "error": True,
                    "message": "Invalid input. Must be a numeric value."
                }
            )
