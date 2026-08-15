# Afraim10 biopractice of CS50P: lecture6
import sys


def main():
    records = parse_fasta(sys.argv[1])
    write_fasta(sys.argv[2], records)


def parse_fasta(filepath):
    formatted = {}
    with open(filepath) as file:
        reader = file.readlines()
        for line in reader:
            line = line.strip()
            if line.startswith(">"):
                current_header = line.strip(">")
                formatted[current_header] = ""
            elif not line.startswith(">"):
                formatted[current_header] += line
    return formatted


def write_fasta(filepath, records):
    with open(f"{filepath}.fasta", "w") as file:
        for header, sequence in records.items():
            file.write(f">{header}\n")
            file.write(f"{sequence}\n")


if __name__ == "__main__":
    main()
