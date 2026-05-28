"""
    Runs full DNA sequence analysis pipeline:
    - base composition
    - GC content
    - reverse complement
"""

from io.fasta_parser import parse_fasta
from core.gc_content import gc_content
from core.base_count import base_stats
from core.reverse_complement import reverse_complement


def run_pipeline(file_path: str) -> dict:

    data = parse_fasta(file_path)

    results = {}

    for header, seq in data.items():

        results[header] = {
            "gc_content": gc_content(seq),
            "base_stats": base_stats(seq),
            "reverse_complement": reverse_complement(seq)
        }

    return results