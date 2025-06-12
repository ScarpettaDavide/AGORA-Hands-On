import pytest

@pytest.fixture
def single_mutation():
    ref = "ACCGT"
    alt = "ACCAT"
    return ref, alt

# Define your fixtures here!

@pytest.fixture
def multiple_mutations():
    # Define a fixture for multiple mutations
    pass
