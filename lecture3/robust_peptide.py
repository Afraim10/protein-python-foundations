# Afraim10 biopractice of CS50P: lecture3
def get_residue_count():
    while True:
        try:
            residues = input("Number of residues: ").replace(" ", "")
            residues = list(residues.split(","))
            for i in range(len(residues)):
                if residues[i].isnumeric() == False or (float(residues[i])/int(residues[i])) != 1:
                    raise ValueError
                else:
                    cleaned = clean_pept(residues[i])
                    print(
                        f"{cleaned[0]} -> {cleaned[1]} -> {cleaned[2]}")
            break
        except ValueError:
            print("Invalid: please enter a whole number.")
            pass

# functions were reused and further improved upon each new practice file


def classify_prot(residues):
    residues = int(residues)
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
    residues = int(residues)
    molecular_weight = (residues * avg_residue_mass) + 18.02
    if molecular_weight > 10000:
        molecular_weight = round(molecular_weight/1000, 2)
        return f"{molecular_weight} KDa"
    else:
        return f"{molecular_weight} Da"


def clean_pept(residues):
    classification = classify_prot(residues)
    estimation = estimate_mass(residues)
    return residues, estimation, classification


get_residue_count()
