# Afraim10 biopractice of CS50P: lecture3
def main():
    while True:
        try:
            sequence = input("Enter DNA sequence: ")
            cleaned = cleanseq(sequence)
            counted = count(cleaned)
            print(f"A: {round(counted[0], 1)}%")
            print(f"T: {round(counted[1], 1)}%")
            print(f"C: {round(counted[2], 1)}%")
            print(f"G: {round(counted[3], 1)}%")
            break
        except ZeroDivisionError:
            print("Error: cannot compute GC content of an empty sequence.")
            pass
        except ValueError:
            pass


# Reusing cleanseq function from clean_sequence.py from lecture1
def cleanseq(seq: str) -> str:
    return seq.replace(" ", "").upper()


def count(sequence):
    adenine = 0
    cytosine = 0
    guanine = 0
    thymine = 0
    length = len(sequence)
    for n in range(len(sequence)):
        if sequence[n] == "A":
            adenine += 1
        elif sequence[n] == "T":
            thymine += 1
        elif sequence[n] == "C":
            cytosine += 1
        elif sequence[n] == "G":
            guanine += 1
    aden_per = (adenine/length)*100
    thy_per = (thymine/length)*100
    cyto_per = (cytosine/length)*100
    gua_per = (guanine/length)*100
    return aden_per, thy_per, cyto_per, gua_per


main()
