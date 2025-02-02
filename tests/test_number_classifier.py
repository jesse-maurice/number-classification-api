import pytest
from app.number_classifier import NumberClassifier

@pytest.fixture
def classifier():
    return NumberClassifier()

def test_is_prime(classifier):
    assert classifier.is_prime(2) == True
    assert classifier.is_prime(17) == True
    assert classifier.is_prime(4) == False
    assert classifier.is_prime(1) == False

def test_is_perfect(classifier):
    assert classifier.is_perfect(6) == True  # 1 + 2 + 3 = 6
    assert classifier.is_perfect(28) == True  # 1 + 2 + 4 + 7 + 14 = 28
    assert classifier.is_perfect(12) == False

def test_is_armstrong(classifier):
    assert classifier.is_armstrong(371) == True  # 3^3 + 7^3 + 1^3 = 371
    assert classifier.is_armstrong(153) == True  # 1^3 + 5^3 + 3^3 = 153
    assert classifier.is_armstrong(123) == False

def test_digit_sum(classifier):
    assert classifier.digit_sum(371) == 11
    assert classifier.digit_sum(123) == 6
    assert classifier.digit_sum(1000) == 1
    assert classifier.digit_sum(-123) == 6  # Test negative number

@pytest.mark.asyncio
async def test_classify_number(classifier):
    result = await classifier.classify_number(371)
    assert result["number"] == 371
    assert result["is_prime"] == False
    assert "armstrong" in result["properties"]
    assert "odd" in result["properties"]
    assert result["digit_sum"] == 11

@pytest.mark.asyncio
async def test_invalid_input(classifier):
    result = await classifier.classify_number("abc")
    assert result["error"] == True

@pytest.mark.asyncio
async def test_negative_number(classifier):
    result = await classifier.classify_number(-123)
    assert result["number"] == -123
    assert result["digit_sum"] == 6

@pytest.mark.asyncio
async def test_floating_point_number(classifier):
    result = await classifier.classify_number(12.34)
    assert result["number"] == 12