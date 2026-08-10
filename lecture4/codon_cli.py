# Afraim10 biopractice of CS50P: lecture4
import sys


def main():
    bases = ['A', 'C', 'T', 'G']
    if len(sys.argv) > 2 or len(sys.argv) < 2:
        print("Usage: python codon_cli.py SEQUENCE.")
        sys.exit(1)
    sequence = sys.argv[1].upper().strip()
    if len(sequence) % 3 != 0:
        print('Error: sequence length must be a multiple of 3.')
        sys.exit(1)
    for i in range(len(sequence)):
        if sequence[i] not in bases:
            print("Invalid: Only DNA bases are allowed.")
            sys.exit(1)
    else:
        n = 0
        cleaned = []
        while n in range(len(sequence)):
            if sequence[n:n+3] not in cleaned:
                cleaned.append(sequence[n:n+3])
            n += 3
        print(f"Codons: {', '.join(cleaned)}")


main()
