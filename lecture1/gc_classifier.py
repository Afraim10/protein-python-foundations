# Afraim10 biopractice of CS50P: lecture1
def main():
    seq = input("DNA sequence: ").upper().replace(" ", "")
    gc_calculation = gc_content(seq)
    print(f"GC content: {gc_calculation:.1f}%")
    classified = classify_gc(gc_calculation)
    print(f"Classification: {classified}")


def gc_content(seq):  # updating gc_content function from gc_content.py
    seq_length = len(seq)
    gc_count = (seq.count('C') + seq.count('G'))
    gc_percen = float(gc_content/seq_length) * 100
    # g_count = seq.count('G')#  # If used later on
    # c_count = seq.count('C')#  # If used later on
    return gc_percen


def classify_gc(percentage):
    if percentage > 60:
        return "GC-rich (higher thermostability)"
    elif percentage < 40:
        return "AT-rich (lower thermostability)"
    else:
        return "Balanced GC content"


main()
