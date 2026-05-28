# Provides base counts (A/T/G/C), percentage distribution,

def base_stats(dna: str):
    
    dna = dna.upper()
    total = len(dna)

    counts = {
        base: dna.count(base)
        for base in ["A", "T", "G", "C"]
    }

    percentages = {
        base: (count / total) * 100
        for base, count in counts.items()
    }

    return counts, percentages