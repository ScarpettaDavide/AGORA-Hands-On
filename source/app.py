import streamlit as st
from main import find_mutations, gc_content

st.title("🧬 Agora Hands On!")
st.write(" ## Mutation Finder")
st.write("Enter a reference DNA sequence and a tumor DNA sequence to find mutations:")

# Input fields for sequences
ref_input = st.text_input("Reference DNA sequence", value="ACCGT")
tumor_input = st.text_input("Tumor DNA sequence", value="ACCAT")

# Button to trigger analysis
if st.button("Identify Mutations"):
    mutations = find_mutations(ref_input, tumor_input)
    if mutations:
        st.subheader("Found Mutations:")
        # Display results as a table
        st.table([{"Position": pos, "Ref Base": ref, "Alt Base": tum} for (pos, ref, tum) in mutations])
    else:
        st.subheader("Found Mutations:")
        st.write("None ✅ (the sequences are identical)")

st.markdown("---")
st.write("## GC‐content Calculator")
# Try to create your own GC content calculator app!