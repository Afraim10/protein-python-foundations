# Afraim10 biopractice of CS50P
def main():
    residues = int(input("Number of residues: ").upper().replace(" ", ""))
    print('Estimated mass (based on avg amino acid molecular weight):',
          estimate_mass(residues,), "Da")


def estimate_mass(residues, avg_residue_mass=110.0):
    # one water added back for the two chain termini
    molecular_weight = (residues * avg_residue_mass) + 18.02
    return molecular_weight


main()
