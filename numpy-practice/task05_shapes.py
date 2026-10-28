# Afraim10 biopractice: numpy
import numpy as np


def main():
    rng = np.random.default_rng(seed=42)  # seed for reproducibility
    charge = np.round(rng.uniform(-1.0, 1.0, size=10), 2)
    b_factor = np.round(rng.uniform(10.0, 50.0, size=10), 1)
    accessibility = np.round(rng.uniform(0, 100, size=10), 1)
    atomistic_prop = np.vstack((charge, b_factor, accessibility))
    atomistic_prop2 = np.array([charge, b_factor, accessibility])
    print("Atomistic Properties array creation methods match?",
          np.array_equal(atomistic_prop, atomistic_prop2))  # np.allclose() allows small numerical difference tolerance

    residues_sliced, last_col, every_2nd_col = slicing_arrays(atomistic_prop)
    print(
        f"residues 3-7 of row 2:\n {residues_sliced} \nthe last column:\n {last_col} \nevery second column:\n {every_2nd_col}")


def slicing_arrays(atomistic_prop):
    residues_sliced = atomistic_prop[1, 2:7]
    last_col = atomistic_prop[:, -1]  # or last col 9
    every_2nd_col = atomistic_prop[:, 1::2]
    return residues_sliced, last_col, every_2nd_col


if __name__ == "__main__":
    main()
