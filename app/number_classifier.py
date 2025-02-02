from typing import List, Dict, Union
from .utils import validate_input, format_response
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
        num_str = str(n)
        power = len(num_str)
        return sum(int(digit) ** power for digit in num_str) == n

    def digit_sum(self, n: int) -> int:
        """Calculate the sum of digits."""
        return sum(int(digit) for digit in str(n))

    def get_properties(self, n: int) -> List[str]:
        """Get all properties of a number."""
        properties = []
        
        # Check Armstrong
        if self.is_armstrong(n):
            properties.append("armstrong")
        
        # Check odd/even
        properties.append("odd" if n % 2 else "even")
        
        return properties

    async def get_fun_fact(self, n: int) -> str:
        """Get a fun fact about the number."""
        try:
            response = requests.get(f"{self.numbers_api_url}{n}/math")
            return response.text
        except:
            # Fallback fun fact if API is unavailable
            if self.is_armstrong(n):
                digits = str(n)
                calc = " + ".join(f"{d}^{len(digits)}" for d in digits)
                return f"{n} is an Armstrong number because {calc} = {n}"
            return f"The number {n} is {'even' if n % 2 == 0 else 'odd'}"

    async def classify_number(self, number: Union[str, int]) -> Dict:
        """Classify a number and return all its properties."""
        try:
            n = int(number)
            properties = self.get_properties(n)
            
            return {
                "number": n,
                "is_prime": self.is_prime(n),
                "is_perfect": self.is_perfect(n),
                "properties": properties,
                "digit_sum": self.digit_sum(n),
                "fun_fact": await self.get_fun_fact(n)
            }
        except ValueError:
            return {
                "number": str(number),
                "error": True
            }