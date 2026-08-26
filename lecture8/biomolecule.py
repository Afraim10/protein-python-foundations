# Afraim10 biopractice of CS50P: lecture8
class Biomolecule:
    def __init__(self, sequence):
        self.sequence = sequence.strip().upper()

    def __len__(self):
        return len(self.sequence)


class DNA(Biomolecule):
    def gc_content(self):
        seq_length = len(self)
        gc_count = self.sequence.count('C') + self.sequence.count('G')
        gc_percen = float(gc_count/seq_length) * 100
        return f"{round(gc_percen,2)}%"


class Protein(Biomolecule):
    def estimate_mass(self, avg_residue_mass=110.0):
        if len(self) <= 0:
            raise ValueError
        self.avg_residue_mass = avg_residue_mass
        calculated_mass = (len(self) * self.avg_residue_mass) + 18.02
        if calculated_mass > 10000:
            calculated_mass = round(calculated_mass/1000, 2)
            return f"{calculated_mass} KDa"
        else:
            return f"{calculated_mass} Da"


def main():
    d = DNA("atgcgcta")
    p = Protein("MKV")
    print(len(d), len(p))
    print(d.gc_content())
    print(p.estimate_mass())


if __name__ == "__main__":
    main()
