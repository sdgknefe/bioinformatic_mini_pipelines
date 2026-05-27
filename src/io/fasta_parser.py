"""
FASTA Parser Module
--------------------

Part of bioinformatics-mini-pipelines project.

Parses multi-FASTA files into a dictionary.

Author: Doğukan EFE
"""
def fasta_parser(path_file: str) -> dict:

    data = {}
    header = None
    sequence = ""

    with open(path_file) as file:
        
        for line in file:
            line = line.strip()
            
            if not line:
                continue
            
            elif line.startswith(">"):
                
                if header != None:
                    data[header] = sequence
                
                header = line[1:]
                sequence = ""

            else:
                sequence += line

        if header is not None:
            data[header] = sequence

    return data

