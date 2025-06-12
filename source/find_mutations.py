# Function to identify mutations between two DNA sequences
def find_mutations(ref_seq, tumor_seq):
    mutations = []
    for i, (ref_base, tumor_base) in enumerate(zip(ref_seq, tumor_seq)):
        if ref_base != tumor_base:
            mutations.append((i, ref_base, tumor_base))
    return mutations