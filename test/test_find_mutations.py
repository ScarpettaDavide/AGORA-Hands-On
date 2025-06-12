from source.find_mutations import find_mutations

def test_find_mutations_single(single_mutation):
    ref, alt = single_mutation
    expected = [(3, "G", "A")]
    assert find_mutations(ref, alt) == expected

# Add your tests! 

def test_find_mutations_multiple():
    # Complete this test!
    pass

def test_find_mutations_no_mutations():
    # Complete this test!
    pass