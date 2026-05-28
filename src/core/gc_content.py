"""
    Calculates GC content percentage of a DNA sequence.
"""

def gc_content(dna: str) -> float:

    dna = dna.upper()

    if len(dna) == 0:
        return 0.0

    return (dna.count("G") + dna.count("C")) / len(dna) * 100