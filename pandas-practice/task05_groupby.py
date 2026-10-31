# Afraim10 biopractice: pandas
import pandas as pd

data = {
    "gene": ["ACTB", "GAPDH", "MYC", "TP53", "EGFR", "BCL2"] * 6,
    "condition": ["control"] * 18 +
    ["treated"] * 18,
    "expression": [
        12.5, 45.2, 3.1, 8.7, 22.4, 5.9,     # control, replicate 1
        12.9, 44.8, 3.4, 9.0, 22.8, 6.2,     # control, replicate 2
        12.1, 45.6, 2.8, 8.4, 22.0, 5.6,     # control, replicate 3
        15.8, 44.1, 9.6, 4.2, 31.7, 11.3,    # treated, replicate 1
        16.2, 44.5, 9.9, 4.5, 32.1, 11.6,    # treated, replicate 2
        15.4, 43.7, 9.3, 3.9, 31.3, 11.0,    # treated, replicate 3
    ],
}

genes_df = pd.DataFrame(data)


def main():
    cond_mean, cond_std, gene_mean_wide, gene_std_wide = genes_stat(genes_df)
    for name, t in [("mean per condition", cond_mean), ("std per condition", cond_std),
                    ("mean gene*condition (wide)", gene_mean_wide),
                    ("std gene*condition (wide)", gene_std_wide)]:
        print(f"\n{name}:\n{t}")


def genes_stat(dataframe):
    conditioned_genes_mean = dataframe.groupby(
        "condition")["expression"].mean()
    conditioned_genes_std = dataframe.groupby("condition")["expression"].std()

    per_gene_mean = dataframe.groupby(["gene", "condition"])[
        "expression"].mean()
    per_gene_std = dataframe.groupby(["gene", "condition"])[
        "expression"].std()  # std(ddof=0) is possible if there were no replicates `forced`

    unstacked_mean_gene = per_gene_mean.unstack("condition")
    unstacked_std_gene = per_gene_std.unstack("condition")

    return conditioned_genes_mean, conditioned_genes_std, unstacked_mean_gene, unstacked_std_gene


if __name__ == "__main__":
    main()
