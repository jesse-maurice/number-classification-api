# app/number_classifier.py
from typing import List, Dict, Union
import math
import requests

class NumberClassifier:
    def __init__(self):
        self.numbers_api_url = "http://numbersapi.com/"

    def is_prime(self, n: int) -> bool:
        """Check if a number is prime."""
        if n <= 1:  # Handle negative numbers and 1
            return False
        for i in range(2, int(math.sqrt(abs(n))) + 1):
            if abs(n) % i == 0:
                return False
        return True

    def is_perfect(self, n: int) -> bool:
        """Check if a number is perfect."""
        if n <= 1:  # Handle negative numbers and 1
            return False
        sum_divisors = sum(i for i in range(1, abs(n)) if abs(n) % i == 0)
        return sum_divisors == abs(n)

    def is_armstrong(self, n: int) -> bool:
        """Check if a number is an Armstrong number."""
        num_str = str(abs(n))  # Handle negative numbers
        power = len(num_str)
        return sum(int(digit) ** power for digit in num_str) == abs(n)

    def digit_sum(self, n: int) -> int:
        """Calculate the sum of digits."""
        return sum(int(digit) for digit in str(abs(n)))

    def get_properties(self, n: int) -> List[str]:
        """Get all properties of a number."""
        properties = []
        
        # Check Armstrong (only for positive numbers)
        if n > 0 and self.is_armstrong(n):
            properties.append("armstrong")
        
        # Check odd/even
        properties.append("odd" if abs(n) % 2 else "even")
        
        return properties

    async def get_fun_fact(self, n: int) -> str:
        """Get a fun fact about the number."""
        try:
            response = requests.get(f"{self.numbers_api_url}{abs(n)}/math")
            if response.status_code == 200:
                return response.text
        except:
            pass
        
        # Fallback fun facts
        if n > 0 and self.is_armstrong(n):
            digits = str(n)
            calc = " + ".join(f"{d}^{len(digits)}" for d in digits)
            return f"{n} is an Armstrong number because {calc} = {n}"
        return f"The number {n} is {'even' if n % 2 == 0 else 'odd'}"

    async def classify_number(self, number: Union[str, int, float]) -> Dict:
        """Classify a number and return all its properties."""
        try:
            n = int(float(number))
            return {
                "number": n,
                "is_prime": self.is_prime(n),
                "is_perfect": self.is_perfect(n),
                "properties": self.get_properties(n),
                "digit_sum": self.digit_sum(n),
                "fun_fact": await self.get_fun_fact(n)
            }
        except (ValueError, TypeError):
            return {
                "number": str(number),
                "error": True
            }