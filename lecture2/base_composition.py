# Afraim10 biopractice of CS50P: lecture2
def main():
    sequence = input("Enter DNA sequence: ")
    # a, t, c, g = count(cleaned) is a consideration as well but i am keeping this
    cleaned = cleanseq(sequence)
    print(f"A: {round(count(cleaned)[0], 1)}%")
    print(f"T: {round(count(cleaned)[1], 1)}%")
    print(f"C: {round(count(cleaned)[2], 1)}%")
    print(f"G: {round(count(cleaned)[3], 1)}%")


# Reusing cleanseq function from clean_sequence.py from lecture1
def cleanseq(seq: str) -> str:
    return seq.replace(" ", "").upper().strip()


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
