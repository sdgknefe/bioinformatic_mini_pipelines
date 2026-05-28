"""
    Returns the reverse complement of a DNA sequence.

    Unknown bases are converted to 'N'.
"""
def reverse_complement(dna: str) ->str:
    
    complement = {
        "A":"T", 
        "T":"A", 
        "G":"C", 
        "C":"G"
    }

    dna = dna.upper()

    return "".join(complement.get(base, "N") for base in dna)[::-1]