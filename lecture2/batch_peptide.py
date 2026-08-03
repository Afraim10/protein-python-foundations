# Afraim10 biopractice of CS50P: lecture2
def main():
    residues = input(
        "Enter residue counts (comma-separated): ").strip().replace(" ", "")
    clean_pept(residues)


def classify_prot(residues):  # reused from lecture1
    resd = int(residues.strip().replace(" ", ""))
    if resd < 20:
        return "short peptide"
    elif resd >= 20 and resd <= 50:
        return "peptide"
    elif resd >= 51 and resd <= 300:
        return "small protein"
    elif resd >= 301:
        return "large protein"


def estimate_mass(residues, avg_residue_mass=110.0):
    # one water added back for the two chain termini "dehydrated amino acid"
    resd = int(residues.strip().replace(" ", ""))
    molecular_weight = (resd * avg_residue_mass) + 18.02
    if molecular_weight > 10000:
        molecular_weight = round(molecular_weight/1000, 2)
        return f"{molecular_weight} KDa"
    else:
        return f"{molecular_weight} Da"


def clean_pept(residues):
    resd = residues.strip().replace(" ", "")
    for n in resd.split(","):
        classification = classify_prot(n)
        estimation = estimate_mass(n)
        print(f"{n} residues -> {estimation} -> {classification}")


main()
