# Afraim10 biopractice: numpy
import numpy as np

aminoacids = np.array(["A", "R", "N", "D", "C", "E", "Q", "G",
                       "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"])
hydrophobicity = np.array([1.8, -4.5, -3.5, -3.5, 2.5, -3.5, -3.5,
                           -0.4, -3.2, 4.5, 3.8, -3.9, 1.9, 2.8, -1.6, -0.8, -0.7, -0.9, -1.3, 4.2])


def main():
    count, below_minus_three, interval_mask_aa = hydrophobic_calculations(
        aminoacids, hydrophobicity)
    print(
        f"Number of hydrophobic residues 'KD-scale': {count},\n Residues with KD values below −3 are: {below_minus_three},\n Mask between -1 to 1 valued residues: {interval_mask_aa}")


def hydrophobic_calculations(aminoacids, hydrophobicity):
    # no_hydrophobic_residues = len(hydrophobicity[hydrophobicity > 0]) "alternative"
    no_hydrophobic_residues = (hydrophobicity > 0).sum()
    residues_below_neg3 = aminoacids[hydrophobicity < -3]
    # semi_neutral_residues = aminoacids[(
    # hydrophobicity > -1) & (hydrophobicity < 1)]
    interval_mask = (hydrophobicity > -1) & (hydrophobicity <
                                             1)  # boolean-array `and` requires one truth value per array; `&` combines elements pairwise.
    return (no_hydrophobic_residues, residues_below_neg3, aminoacids[interval_mask])


if __name__ == "__main__":
    main()
