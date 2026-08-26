# Afraim10 biopractice of CS50P: lecture8
class DNASequence:
    def __init__(self, raw_sequence):
        self.sequence = raw_sequence.replace(" ", "").upper().strip()

    def gc_content(self):
        seq_length = len(self)
        gc_count = self.sequence.count('C') + self.sequence.count('G')
        gc_percen = float(gc_count/seq_length) * 100
        return f"{round(gc_percen,2)}%"

    def base_counts(self):
        adenine = 0
        cytosine = 0
        guanine = 0
        thymine = 0
        for n in range(len(self)):
            if self.sequence[n] == "A":
                adenine += 1
            elif self.sequence[n] == "T":
                thymine += 1
            elif self.sequence[n] == "C":
                cytosine += 1
            elif self.sequence[n] == "G":
                guanine += 1
        return {"A": adenine, "T": thymine, "C": cytosine, "G": guanine}

    def __len__(self):
        return int(len(self.sequence))


def main():
    seq = DNASequence("atgc gcta")
    print(len(seq))
    print(seq.gc_content())


if __name__ == "__main__":
    main()
