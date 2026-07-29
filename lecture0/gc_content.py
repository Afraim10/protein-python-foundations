def main():
    sequence = input("Enter DNA Sequence: ").replace(
        " ", "").upper()
    length = len(sequence)
    gc_count = gc_content(sequence)
    gc_count = float(gc_count)
    gc_percen = ((gc_count/length)*100)
    print(f"GC content:{gc_percen:,.1f}%")


def gc_content(seq):
    return (seq.count('C') + seq.count('G'))


main()
