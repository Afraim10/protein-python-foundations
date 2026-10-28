# Afraim10 biopractice: numpy
import numpy as np


def main():
    rng = np.random.default_rng(seed=42)
    genes_names = np.array(["COX10", "ADA", "MRC2", "SKAP1", "ETNK1"])
    genes_exp = rng.integers(low=1, high=101, size=(5, 4))
    # fmt="%-i" an odd left-justify flag with no width
    np.savetxt("numpy_geneexp.csv", genes_exp, fmt="%d", delimiter=",")
    loaded = np.loadtxt("numpy_geneexp.csv", dtype=int, delimiter=",")

    # Usage of .npy for exact dtype and shape preservation and efficient NumPy storage.
    # ensuring array before saving is the same as newly saved
    print(np.array_equal(genes_exp, loaded))


if __name__ == "__main__":
    main()
