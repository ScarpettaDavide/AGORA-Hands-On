# Function to identify mutations between two DNA sequences
def find_mutations(ref_seq, tumor_seq):
    mutations = []
    for i, (ref_base, tumor_base) in enumerate(zip(ref_seq, tumor_seq)):
        if ref_base != tumor_base:
            mutations.append((i, ref_base, tumor_base))
    return mutations

# Example usage
if __name__ == "__main__":
    ref_sequence = "ACGTACGTGACG"
    alt_sequence = "ACGTTCGTGATG"
    
    mutations = find_mutations(ref_sequence, alt_sequence)
    for pos, ref_base, alt_base in mutations:
        print(f"Position: {pos}, Ref Base: {ref_base}, Alt Base: {alt_base}")