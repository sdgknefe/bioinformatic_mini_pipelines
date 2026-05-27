'''

'''

def gc_content(dna):

    if len(dna) == 0:
        return 0.0
    
    return (dna.count("G") + dna.count("C")) / len(dna) * 100

dna = "ATCAGTCGATGCATGCTA"

print(gc_content(dna))