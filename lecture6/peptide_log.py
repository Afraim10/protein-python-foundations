# Afraim10 biopractice of CS50P: lecture6
import sys
import csv
from peptide_classifier import classify_prot, estimate_mass


def load_and_classify(filepath):
    try:
        with open(filepath) as file:
            reader = csv.DictReader(file)
            results = []
            reader = list(reader)
            for row in reader:
                name = row["name"]
                residues = row["residues"]
                results.append({"name": name, "residues": residues, "mass": estimate_mass(
                    residues), "classification": classify_prot(residues)})
            return results
    except FileNotFoundError:
        print(f"Couldn't find {filepath}")


def save_results(filepath, results):
    with open(filepath, "w") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "residues", "mass", "classification"])
        writer.writeheader()
        for row in results:
            file.write(
                f"{row['name']},{row['residues']},{row['mass']},{row['classification']}\n")


results = load_and_classify("peptides.csv")
save_results("testedpeptidefile.csv", results)
