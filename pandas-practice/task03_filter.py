# Afraim10 biopractice: pandas
import pandas as pd


def main(filepath: str):
    ...


def proteins_tabulated(filepath):
    read_df = pd.read_csv(filepath)
    ...


if __name__ == "__main__":
    main("testedpeptidefile.csv")
