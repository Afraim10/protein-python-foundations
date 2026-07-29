# Afraim10 biopractice of CS50P#
def cleanseq(s: str) -> str:
    return s.replace(" ", "").upper().lstrip().rstrip()


def main():
    sequence = input("Enter your DNA sequence: ")
    cleaned = cleanseq(sequence)
    print("5'", cleaned, "3'")


main()
