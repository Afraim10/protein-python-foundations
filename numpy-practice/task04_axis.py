# Afraim10 biopractice: numpy
import numpy as np
rng = np.random.default_rng(seed=42)
# np.set_printoptions(legacy='1.25') - helps with the `np.float_()` but not worth using globally


def main():
    genes_names = np.array(["COX10", "ADA", "MRC2", "SKAP1", "ETNK1"])
    # don't wrap the rng into [] which creates 3D

    # don't put a generator into each row, instead specialzie the size directly
    genes_exp = rng.integers(low=1, high=101, size=(5, 4))

    mpg, mps, cn = expression_statistics(genes_exp)
    print("Raw expression matrix (5x4):\n", genes_exp)
    print("Mean expression per gene (axis=1):\n", dict(
        zip(genes_names.tolist(), np.round(mpg, 2).tolist())))  # using .tolist() to prevent `np.str_()`
    # .tolist() can be used on `np_floats()` for dict values
    print("Mean expression per sample (axis=0):\n", np.round(
        mps, 2))  # don't `zip` 5 genes to 4 samples
    print("Column-Normalized Copy:\n", np.round(cn, 3))


def expression_statistics(genes_exp):
    mean_per_sample = np.mean(genes_exp, axis=0)
    mean_per_gene = np.mean(genes_exp, axis=1)
    sample_sum = np.sum(genes_exp, axis=0)
    col_normalized = genes_exp / sample_sum
    return mean_per_gene, mean_per_sample, col_normalized


if __name__ == "__main__":
    main()
