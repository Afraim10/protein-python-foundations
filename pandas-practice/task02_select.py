# Afraim10 biopractice: pandas
import pandas as pd


def main(filepath: str):
    org_series, org_onecol, accession_and_gene, ent_prot_org, ent_prot_org1 = proteins_tabulated(
        filepath)
    print(f"Df Series 'Organism':\n{org_series}\n \nDf 'Organism' One Col:\n{org_onecol}\n \nDf 'Accesion & Gene':\n{accession_and_gene}\n \nDf Sliced via .loc:\n{ent_prot_org}\n \nDf sliced via .iloc\n{ent_prot_org1}")


def proteins_tabulated(filepath):
    read_df = pd.read_csv(filepath)
    org_series = read_df["organism"]
    org_onecol = read_df[["organism"]]
    # one difference noticed in series
    # `Name: organism, dtype: str`

    accession_and_gene = read_df[["accession", "gene_name"]]
    ent_prot_org = read_df.loc[2:5, ["entry_name", "protein_name", "organism"]]
    ent_prot_org1 = read_df.iloc[2:6, 1:4]
    # accessing via iloc `end-exclusive`
    return org_series, org_onecol, accession_and_gene, ent_prot_org, ent_prot_org1


if __name__ == "__main__":
    main("uniprot_organized.csv")
