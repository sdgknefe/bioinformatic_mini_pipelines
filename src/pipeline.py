from io.fasta_parser import fasta_parser
from core.gc_content import gc_content

def run_pipeline(file_path: str) -> dict:
    
    data = fasta_parser(file_path)
    results = {}

    for header, seq in data.items():
        gc = gc_content(seq)
        results[header] = gc

    return results