"""
GC Content Module
-----------------

Calculates GC content of a DNA sequence.

Formula:
    GC% = (G + C) / length(sequence) * 100

Input:
    DNA sequence (string)

Output:
    float (percentage)
"""

def gc_content(dna):

    if len(dna) == 0:
        return 0.0
    
    return (dna.count("G") + dna.count("C")) / len(dna) * 100

dna = "ATCAGTCGATGCATGCTA"

print(gc_content(dna))