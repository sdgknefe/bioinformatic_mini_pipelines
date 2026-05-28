"""
    Runs full DNA sequence analysis pipeline:
    - base composition
    - GC content
    - reverse complement
"""

from src.io_layer.fasta_parser import fasta_parser
from src.core.gc_content import gc_content
from src.core.base_stats import base_stats
from src.core.reverse_complement import reverse_complement


def run_pipeline(file_path: str) -> dict:

    data = fasta_parser(file_path)

    results = {}

    for header, seq in data.items():

        results[header] = {
            "gc_content": gc_content(seq),
            "base_stats": base_stats(seq),
            "reverse_complement": reverse_complement(seq)
        }

    return results