from typing import Union, Dict, Any

def validate_input(number: str) -> tuple[bool, Union[int, str]]:
    try:
        num = int(number)
        if abs(num) > 1000000:  # Optional: limit very large numbers
            return False, "Number must be between -1000000 and 1000000"
        return True, num
    except ValueError:
        # Return the original input value (string) when validation fails
        return False, number  # Pass the invalid input directly as a string

def format_response(data: Dict[str, Any], status_code: int = 200) -> Dict[str, Any]:
    if status_code == 400:
        return {
            "number": data.get("number", ""),  # Return the invalid input in the response
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
    return f"number_classification_{number}"
