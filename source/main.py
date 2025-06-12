# Function to identify mutations between two DNA sequences
def find_mutations(ref_seq, tumor_seq):
    """
    Identify mutations between a reference DNA sequence and a tumor DNA sequence.
    Returns a list of tuples (position, ref_base, tumor_base) for each mutation.
    """
    mutations = []
    for i, (ref_base, tumor_base) in enumerate(zip(ref_seq, tumor_seq)):
        if ref_base != tumor_base:
            mutations.append((i, ref_base, tumor_base))
    return mutations

# Function to calculate GC content of a DNA sequence
def gc_content(seq):
    """
    Return the GC content percentage of the given DNA sequence.
    Non-ACGT characters are ignored in the length calculation.
    """
    # make uppercase for consistency
    seq = seq.upper()
    # count G and C
    gc_count = seq.count('G') + seq.count('C')
    # count only valid bases for length
    valid_bases = sum(seq.count(b) for b in "ACGT")
    if valid_bases == 0:
        return 0.0
    return (gc_count / valid_bases) * 100