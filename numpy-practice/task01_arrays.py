# Afraim10 biopractice: numpy
import numpy as np

# aa_hydrophob = np.array([["A", "R", "N", "D", "C", "E", "Q", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"], [
# 1.8, -4.5, -3.5, -3.5, 2.5, -3.5, -3.5, -0.4, -3.2, 4.5, 3.8, -3.9, 1.0, 2.8, -1.6, -0.8, -0.7, -0.9, -1.3, 4.2]])
# aa = np.vstack((aminoacids, hydrophobicity))
# vstack converted the whole array to strings (<U32) which caused errors later using stat functions
# print(f"Respectively hydorphobic values mean, median, standard deviation: {aa_hydrophob[1,:].mean()}, {aa_hydrophob[1,:].median()}, {aa_hydrophob[1,:].std()}") -> TypeError

aminoacids = np.array(["A", "R", "N", "D", "C", "E", "Q", "G",
                       "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"])
hydrophobicity = np.array([1.8, -4.5, -3.5, -3.5, 2.5, -3.5, -3.5,
                           -0.4, -3.2, 4.5, 3.8, -3.9, 1.9, 2.8, -1.6, -0.8, -0.7, -0.9, -1.3, 4.2])


def main():
    print("Amino Acids letters array:\n", aminoacids)  # letters
    print("Amino Acids with Hydrophobicity values array:\n",
          hydrophobicity)  # hydrophobic array values

    print("Amino Acids with Hydrophobicity values array shape:",
          hydrophobicity.shape)  # shape
    print("Amino Acids with Hydrophobicity values type:",
          hydrophobicity.dtype)  # data type
    print("Amino Acids with Hydrophobicity values array dimensions:",
          hydrophobicity.ndim)  # number of dimensions
    status = aminoacids_status(aminoacids, hydrophobicity)
    aa1, value1 = status[3]
    aa2, value2 = status[4]
    print(f"Respectively, hydrophobic values mean, median, standarddeviation, "
          f"most hydrophobic, most hydrophilic: {status[0]}, {status[1]}, {status[2]}, {str(aa1)} = {value1},{str(aa2)} = {value2}")


def aminoacids_status(aminoacids, hydrophobicity):
    mean_value = np.round(hydrophobicity.mean(), 3)
    median_value = np.round(np.median(hydrophobicity), 3)
    # np.std() is the population SD (ddof=0)
    standard_deviation = np.round(hydrophobicity.std(), 3)

    max_index = (hydrophobicity.argmax())
    min_index = (hydrophobicity.argmin())

    hydrophobic_aa = (aminoacids[max_index],
                      (hydrophobicity[max_index]))
    hydrophilic_aa = (aminoacids[min_index],
                      (hydrophobicity[min_index]))
    return (mean_value, median_value, standard_deviation, hydrophobic_aa, hydrophilic_aa)

#     return("Most hydrophobic residue 'KD-scale':"
#           aa_hydrophob[0, (aa_hydrophob[1, :].argmax())], aa_hydrophob[1, (aa_hydrophob[1, 0:].argmax())])
#     return("Most hydrophilic residue 'KD-scale':",
#           aa_hydrophob[0, (aa_hydrophob[1, :].argmin())], aa_hydrophob[1, (aa_hydrophob[1, :].argmin())])


if __name__ == "__main__":
    main()
