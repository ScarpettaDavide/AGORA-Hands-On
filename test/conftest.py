import pytest

@pytest.fixture
def single_mutation():
    ref = "ACCGT"
    alt = "ACCAT"
    return ref, alt
