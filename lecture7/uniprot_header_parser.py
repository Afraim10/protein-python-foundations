# Afraim10 biopractice of CS50P: lecture7
import re
import sys
from Bio import (SeqIO, Seq, UniProt)
import csv


def main():
    if sys.argv != 3:
        sys.exit("Only input FASTA file and an output CSV path allowed.")
    input_fasta = sys.argv[1]
    if not input_fasta.endswith((".fasta", ".fa")):
        sys.exit("Only FASTA input file (UniProt-format headers) is allowed.")
    output_csv = sys.argv[2]
    records_dict = uniprot_parse(input_fasta)
    csv_writing(output_csv, records_dict)


def uniprot_parse(input, format="fasta" or "fa"):
    records = {}
    for record in SeqIO.parse(input, format):
        records[record.id] = {record.description}
    return records


def csv_writing(output, records):
    with open
    ...


if __name__ == "__main__":
    main()
