import pytest
from .validation_hosting_preview import validate_hosting_preview_request

def test_empty_payload():
    is_valid, errors = validate_hosting_preview_request({})
    assert not is_valid
    assert "payload" in errors

def test_missing_source():
    is_valid, errors = validate_hosting_preview_request({"config": "test"})
    assert not is_valid
    assert "source" in errors

def test_valid_request():
    is_valid, errors = validate_hosting_preview_request({"source": "github"})
    assert is_valid
    assert not errors
