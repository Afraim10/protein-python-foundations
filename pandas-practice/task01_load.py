# Afraim10 biopractice: pandas
import pandas as pd


def main(filepath: str):
    shape, dtype, header, description = proteins_tabulated(
        filepath)
    print(
        f"\nShape:{shape}\n \nData Types:{dtype}\n \nFirst 5 records:{header}\n \nDataFrame description:{description}\n")
    # taxonomy_id was read as int64 correctly, IDs are numeric
    # accessions were read as object (string) correctly


def proteins_tabulated(filepath):
    read_seq = pd.read_csv(filepath)
    read_seq.info()
    return read_seq.shape, read_seq.dtypes, read_seq.head(), read_seq.describe()


if __name__ == "__main__":
    main("uniprot_organized.csv")
