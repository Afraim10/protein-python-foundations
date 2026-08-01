# Afraim10 biopractice of CS50P: lecture1
def main():
    residues = int(input("Number of residues: ").replace(
        # works by coincidence and frustrates
        " ", "").strip("abcdefghijklmnopqrstvuwxyz"))
    mass = estimate_mass(residues)
    classification = classify_prot(residues)
    print(f"Estimated mass: {mass}")
    print(f"Classification: {classification}")


def classify_prot(residues):
    if residues < 20:
        return "short peptide"
    elif residues >= 20 and residues <= 50:
        return "peptide"
    elif residues >= 51 and residues <= 300:
        return "small protein"
    elif residues >= 301:
        return "large protein"


def estimate_mass(residues, avg_residue_mass=110.0):
    # one water added back for the two chain termini "dehydrated amino acid"
    molecular_weight = (residues * avg_residue_mass) + 18.02
    if molecular_weight > 10000:
        molecular_weight = round(molecular_weight/1000, 2)
        return f"{molecular_weight} KDa"
    else:
        return f"{molecular_weight} Da"


main()
