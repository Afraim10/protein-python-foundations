# Afraim10 biopractice: pandas
import pandas as pd


def main():
    print(proteins_tabulated())


def proteins_tabulated():
    peptides_read_df = pd.read_csv("peptides.csv")
    peptides_read_df["mass_da"] = (
        peptides_read_df["residues"]*110)+18.02
    residues_points = [2, 10, 50, 100,
                       500, 2000, 35000, 1000000]
    classification_labals = ["short peptide", "polypeptide", "small protein",
                             "medium protein", "large protein", "mega protein", "macromolecular assembly"]
    peptides_read_df["classification"] = pd.cut(
        peptides_read_df["residues"], bins=residues_points, labels=classification_labals, include_lowest=True)
    peptides_read_df.to_csv("peptides_enriched.csv", index=False)
    # pandas saves row numbers as first col in CSV, False prevents that

    return peptides_read_df


if __name__ == "__main__":
    main()
