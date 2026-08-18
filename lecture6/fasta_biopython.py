# Afraim10 biopractice of CS50P: lecture6
from Bio import SeqIO
from Bio import Seq
import sys

# filepath = sys.argv[1]
filepath = "testfasta.fasta"  # for testing
# output = sys.argv[2]
output = "parsedbiopython.fasta"  # for testing


def parser(filepath, format="fasta"):
    parsed = {}
    for record in SeqIO.parse(filepath, format):
        parsed[record.id] = str(record.seq)
    return parsed


def write_fasta(filepath, records):
    with open(filepath, "w") as file:
        for header, sequence in records.items():
            file.write(f">{header}\n")
            file.write(f"{sequence}\n")


def main():
    records = parser(filepath, "fasta")
    write_fasta(output, records)


if __name__ == "__main__":
    main()
