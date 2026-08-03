# Afraim10 biopractice of CS50P: lecture2
def main():
    sequence = cleanseq(input("Enter DNA Sequence: "))
    counted = count_invalid_bases(sequence)
    if counted != 0:
        print(
            f"Invalid bases found: {counted}")
    else:
        print("Valid.")

    if counted != 0:
        position_invalids(sequence)


# Reusing cleanseq function from clean_sequence.py from lecture1
def cleanseq(seq: str) -> str:
    return seq.replace(" ", "").upper().strip()


def count_invalid_bases(seq):
    bases = ['A', 'T', 'G', 'C']
    invalid = 0
    for i in range(len(seq)):
        if seq[i] not in bases:
            invalid += 1
    return invalid


def position_invalids(seq):
    for i in range(len(seq)):
        bases = ['A', 'T', 'G', 'C']
        alert = ""
        if seq[i] not in bases:
            alert = (f"Found: {seq[i]} at {i}")
            print(alert)


main()
