# Afraim10 biopractice of CS50P: lecture7
import re
import sys
from Bio import SeqIO
from Bio import Seq


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith((".fasta", ".fa")):
        sys.exit("Open only one FASTA file at a time.")
    input_fasta = sys.argv[1]
    sequences_dict = parser(input_fasta)
    valid_aa(sequences_dict)


def valid_aa(input):
    for id, seq in input.items():
        invalid_amino = ""
        for amino in seq:
            invalid = re.search(
                r"([^ACDEFGHIKLMNPQRSTVWY])", amino, flags=re.IGNORECASE)
            if invalid:
                invalid_amino += invalid.group(1)
        if invalid_amino:
            print(f"{id}: Invalid amino acids: {invalid_amino}", file=sys.stderr)
            print()
        else:
            print(f"{id} Results: \n{find_motif(seq)}")
            print()


def parser(filepath, format="fasta"):
    try:
        parsed = {}
        for record in SeqIO.parse(filepath, format):
            parsed[record.id] = str(record.seq)
        return parsed
    except FileNotFoundError:
        sys.exit("File was not found.")


def find_motif(seq):
    matches = []
    for motif in re.finditer(r"(?=(N[^P][ST][^P]))", seq, flags=re.IGNORECASE):
        catched = motif.group(1)
        position = motif.start()+1
        matches.append(f"Found: {catched} at position: {position}")
    if not matches:
        return "No motifs found"
    return f"Total Motifs: {len(matches)}\n({','.join(matches)})"


if __name__ == "__main__":
    main()
