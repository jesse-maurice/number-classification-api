# tests/test_number_classifier.py
import pytest
from app.number_classifier import NumberClassifier

@pytest.fixture
def classifier():
    return NumberClassifier()

@pytest.mark.asyncio
async def test_valid_positive_number(classifier):
    result = await classifier.classify_number("371")
    assert result["number"] == 371
    assert isinstance(result["is_prime"], bool)
    assert isinstance(result["is_perfect"], bool)
    assert isinstance(result["properties"], list)
    assert isinstance(result["digit_sum"], int)
    assert isinstance(result["fun_fact"], str)

@pytest.mark.asyncio
async def test_valid_negative_number(classifier):
    result = await classifier.classify_number("-123")
    assert result["number"] == -123
    assert isinstance(result["is_prime"], bool)
    assert isinstance(result["is_perfect"], bool)
    assert isinstance(result["properties"], list)
    assert isinstance(result["digit_sum"], int)
    assert isinstance(result["fun_fact"], str)

@pytest.mark.asyncio
async def test_invalid_input(classifier):
    result = await classifier.classify_number("abc")
    assert result["number"] == "abc"
    assert result["error"] is True

@pytest.mark.asyncio
async def test_floating_point(classifier):
    result = await classifier.classify_number("12.34")
    assert result["number"] == 12
    assert isinstance(result["is_prime"], bool)
    assert isinstance(result["is_perfect"], bool)
    assert isinstance(result["properties"], list)
    assert isinstance(result["digit_sum"], int)
    assert isinstance(result["fun_fact"], str)

def test_digit_sum(classifier):
    assert classifier.digit_sum(371) == 11
    assert classifier.digit_sum(-371) == 11
    assert classifier.digit_sum(0) == 0

def test_properties(classifier):
    props = classifier.get_properties(371)
    assert isinstance(props, list)
    assert "armstrong" in props
    assert "odd" in props

    props = classifier.get_properties(-371)
    assert isinstance(props, list)
    assert "odd" in props  # Negative number should still be odd