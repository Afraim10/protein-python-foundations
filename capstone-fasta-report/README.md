# FASTA Batch Analyzer

A command-line tool that reads a FASTA file containing a mix of DNA and
protein sequences, automatically detects which is which, and generates a
summary report — to the console or as CSV.

## What this is

Real FASTA files often contain multiple sequences of different types in one
file. This tool parses such a file with Biopython, classifies each record,
runs the appropriate analysis (GC content for DNA, estimated mass for
protein) using the same `Biomolecule`/`DNA`/`Protein` classes from this
repo's SQLite capstone, and reports the results.

## Files

- `models.py` — shared with the SQLite capstone
- `analyzer.py` — pure functions, no file I/O: `detect_molecule_type`
  (alphabet-based classification) and `analyze_record` (runs the correct
  analysis based on detected type)
- `cli.py` — `argparse` entry point; parses the FASTA file, calls the
  analyzer, and either prints results or writes them to CSV
- `test_analyzer.py` — tests for both core functions, run independently of
  any file or CLI

## Design notes: a real limitation, stated honestly

`detect_molecule_type` distinguishes DNA from protein by checking whether a
sequence's alphabet fits entirely within `{A, T, C, G, N}`. This has a
genuine, unavoidable edge case: a protein sequence built only from amino
acids that happen to share letters with the DNA alphabet (Ala/A, Thr/T,
Cys/C, Gly/G, Asn/N) is indistinguishable from DNA by alphabet alone, and
the DNA check runs first, so such a sequence is classified as DNA. This is
a real ambiguity in sequence-alphabet-only classification, not a bug to be
fully solved — a more robust approach would need additional context (source
database, sequence length distributions, or an explicit user-provided type
flag), which is out of scope for this tool.

## Usage

```bash
python cli.py --fasta sample_sequences.fasta
python cli.py --fasta sample_sequences.fasta --output results.csv
```