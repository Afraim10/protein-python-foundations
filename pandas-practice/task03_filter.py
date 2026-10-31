# Afraim10 biopractice: pandas
import pandas as pd


def main():
    above_100, mega_proteins, bovine_corona = proteins_tabulated()
    print(
        f"Above 100 residues peptides:\n{above_100}\n \nMegaproteins table:\n{mega_proteins}\n \nOrganisms filtered 'Bovine coronavirus':\n{bovine_corona}\n")


def proteins_tabulated():
    peptides_read_df = pd.read_csv("testedpeptidefile.csv")
    above_100 = peptides_read_df[peptides_read_df["residues"] > 100]
    mega_proteins = peptides_read_df[(peptides_read_df["residues"] > 1100) & (
        peptides_read_df["classification"] == "megaprotein")]
    # using `bitwise AND` with `and` ValueError occurs
    # Series value is ambiguous

    unit_prot_read = pd.read_csv("uniprot_organized.csv")
    bovine_corona = unit_prot_read[unit_prot_read["organism"].str.contains(
        "Bovine coronavirus", na=False)]  # defensively assigning NA
    # returns 4 rows with 'Bovine coronavirus
    return above_100, mega_proteins, bovine_corona


if __name__ == "__main__":
    main()
