Bioinformatics Mini Pipeline

A modular Python pipeline for basic DNA sequence analysis using real FASTA data from NCBI.

Project Goal

To build a simple bioinformatics pipeline that processes real genomic FASTA files and performs basic DNA sequence analysis using a modular Python structure.

Data source: National Center for Biotechnology Information (NCBI)

Features

- FASTA file parsing (multi-sequence support)
- Nucleotide counting (A, T, G, C)
- GC content calculation
- Reverse complement generation
- Modular pipeline architecture

How to Run

python main.py data/mecA.fasta

Pipeline Flow

FASTA file
→ Parser (IO layer)
→ Core analysis
→ Output results

Project Structure

src/
  core/
  io/
  pipeline.py

main.py
data/
tests/

Use Case

Analysis of bacterial antibiotic resistance genes (e.g. mecA) related to MRSA.

Author

Doğukan EFE