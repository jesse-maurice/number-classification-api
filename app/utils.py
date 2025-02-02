from typing import Union, Dict, Any

def validate_input(number: str) -> tuple[bool, Union[int, str]]:
    try:
        num = int(number)
        if abs(num) > 1000000:  # Optional: limit very large numbers
            return False, "Number must be between -1000000 and 1000000"
        return True, num
    except ValueError:
        return False, "Input must be a valid integer"

def format_response(data: Dict[str, Any], status_code: int = 200) -> Dict[str, Any]:
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
        "class_sum": data["class_sum"],
        "fun_fact": data["fun_fact"]
    }

def get_cache_key(number: int) -> str:
    return f"number_classification_{number}"