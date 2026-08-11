# Afraim10 biopractice of CS50P: lecture5
import sys


def main():
    try:
        while True:
            sequence = input("Enter Sequence: ")
            print(split_codons(sequence))
            break
    except ValueError:
        pass


def split_codons(sequence):
    bases = ['A', 'C', 'T', 'G']
    length = len(sequence)
    if length % 3 != 0:
        raise ValueError

    for i in range(length):
        if sequence[i] not in bases:
            raise ValueError
        else:
            continue

    n = 0
    cleaned = []
    while n in range(len(sequence)):
        cleaned.append(sequence[n:n+3])
        n += 3
    return cleaned


if __name__ == "__main__":
    main()
