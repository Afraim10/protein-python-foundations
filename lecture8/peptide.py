# Afraim10 biopractice of CS50P: lecture8
class Peptide:
    def __init__(self, residues, avg_residue_mass=110.0):
        if type(residues) != int:
            raise ValueError
        elif int(residues) <= 0:
            raise ValueError
        self.residues = residues
        self.avg_residue_mass = avg_residue_mass

    def mass(self):
        calculated_mass = (self.residues * self.avg_residue_mass) + 18.02
        if calculated_mass > 10000:
            calculated_mass = round(calculated_mass/1000, 2)
            return f"{calculated_mass} KDa"
        else:
            return f"{calculated_mass} Da"

    def classification(self):
        if self.residues < 20:
            return "short peptide"
        elif self.residues >= 20 and self.residues <= 50:
            return "peptide"
        elif self.residues >= 51 and self.residues <= 300:
            return "small protein"
        elif self.residues >= 301:
            return "large protein"

    def __str__(self):
        return f"Peptide({self.residues} residues, {self.classification()})"


def main():
    p = Peptide(150)
    print(p.mass())
    print(p.classification())
    print(p)


if __name__ == "__main__":
    main()
