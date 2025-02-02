# tests/test_number_classifier.py
import pytest
from app.number_classifier import NumberClassifier

@pytest.fixture
def classifier():
    return NumberClassifier()

@pytest.mark.asyncio
async def test_armstrong_number(classifier):
    result = await classifier.classify_number("371")
    assert result["properties"] == ["armstrong", "odd"]

@pytest.mark.asyncio
async def test_regular_odd_number(classifier):
    result = await classifier.classify_number("123")
    assert result["properties"] == ["odd"]

@pytest.mark.asyncio
async def test_regular_even_number(classifier):
    result = await classifier.classify_number("124")
    assert result["properties"] == ["even"]

@pytest.mark.asyncio
async def test_negative_number(classifier):
    result = await classifier.classify_number("-123")
    assert result["properties"] == ["odd"]

@pytest.mark.asyncio
async def test_invalid_input(classifier):
    result = await classifier.classify_number("abc")
    assert "error" in result
    assert result["number"] == "abc"