# Afraim10 biopractice: numpy
import numpy as np

sequence = "MRPSGTAGAALLALLAALCPASRALEEKKVCQ"
aminoacids = np.array(["A", "R", "N", "D", "C", "E", "Q", "G",
                       "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"])
hydrophobicity = np.array([1.8, -4.5, -3.5, -3.5, 2.5, -3.5, -3.5,
                           -0.4, -3.2, 4.5, 3.8, -3.9, 1.9, 2.8, -1.6, -0.8, -0.7, -0.9, -1.3, 4.2])

kd_scale = dict(zip(aminoacids, hydrophobicity))


def main():
    peptide_values, mean_intervals, vectorized_interval, identicality = peptide_lookthrough(
        sequence)
    print(
        f"Peptide sequence array: {np.array([sequence])}\n Sequence hydrophobicity values: {peptide_values}\n Loop through sequence hydrophibic mean (w=7): {mean_intervals}\n Convolved through sequence hydrophoic mean (w=7): {vectorized_interval}\n Are both results identical: {identicality}")
    # print(f"{seqKd},\n {np.round(hydrophob_mean,2)}")


def peptide_lookthrough(sequence: str):
    pept_values = np.array([kd_scale[aa] for aa in sequence])
    length = len(pept_values)
    window = 7
    no_windows = (length - window) + 1
    mean_loop_results = []
    for i in range(no_windows):
        sub_window = pept_values[i:window+i]
        mean_loop_results.append(np.mean(sub_window))
    mean_loop_results = np.array(mean_loop_results)

    kernel = np.ones(window) / window
    vectorized_results = np.convolve(
        pept_values, kernel, mode="valid")

    are_identical = np.allclose(mean_loop_results, vectorized_results)

    return pept_values, np.round(mean_loop_results, 3), np.round(vectorized_results, 3), are_identical


if __name__ == "__main__":
    main()
