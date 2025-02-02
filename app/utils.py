"""
Utility functions for the Number Classification API.
"""
from typing import Union, Dict, Any

def validate_input(number: str) -> tuple[bool, Union[int, str]]:
    """
    Validate and convert input string to integer.
    
    Args:
        number: The input string to validate
        
    Returns:
        tuple: (is_valid, converted_number or error_message)
    """
    try:
        num = int(number)
        if abs(num) > 1000000:  # Optional: limit very large numbers
            return False, "Number must be between -1000000 and 1000000"
        return True, num
    except ValueError:
        return False, "Input must be a valid integer"

def format_response(data: Dict[str, Any], status_code: int = 200) -> Dict[str, Any]:
    """
    Format the API response.
    
    Args:
        data: The data to format
        status_code: HTTP status code
        
    Returns:
        dict: Formatted response
    """
    if status_code == 400:
        return {
            "number": data.get("number", ""),
            "error": True,
            "message": data.get("message", "Invalid input")
        }
    
    return {
        "number": data["number"],
        "is_prime": data["is_prime"],
        "is_perfect": data["is_perfect"],
        "properties": data["properties"],
        "digit_sum": data["digit_sum"],
        "fun_fact": data["fun_fact"]
    }

def get_cache_key(number: int) -> str:
    """
    Generate a cache key for a given number.
    
    Args:
        number: The number to generate a cache key for
        
    Returns:
        str: Cache key
    """
    return f"number_classification_{number}"