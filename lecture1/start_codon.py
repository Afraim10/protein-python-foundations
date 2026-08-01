# Afraim10 biopractice of CS50P: lecture1
def main():
    sequence = cleanseq(input("Enter DNA sequence: "))
    codon_found = has_start_codon(sequence)
    valid_frame = check_reading_frame(sequence)
    codon_msg = "Start codon found" if codon_found == True else "Start codon not found"
    frame_msg = "Valid ORF (multiple of 3)" if valid_frame == True else "Invalid ORF (not a multiple of 3)"
    print(f"{codon_found}, {frame_msg}")


# Reusing cleanseq function from clean_sequence.py from lecture0
def cleanseq(seq: str) -> str:
    return seq.replace(" ", "").upper().strip()  # Slight update of .strip()


def has_start_codon(seq):
    # code was failing later due to checkign for "AUG" RNA start codon instead of "ATG" on DNA coding strand
    if seq.startswith("ATG") or seq.startswith("atg"):
        return True
    else:
        return False


def check_reading_frame(orf):
    length = len(orf)
    if length % 3 == 0:
        return True
    else:
        return False


main()
