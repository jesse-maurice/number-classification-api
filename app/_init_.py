"""
Number Classification API
A FastAPI application that analyzes numbers and returns their mathematical properties.
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__description__ = "A REST API for number classification and analysis"

from .number_classifier import NumberClassifier
from .utils import validate_input, format_response

__all__ = ['NumberClassifier', 'validate_input', 'format_response']