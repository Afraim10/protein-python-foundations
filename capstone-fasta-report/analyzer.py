import re
from models import DNA, Protein


def detect_molecule_type(sequence: str):
    dna_seq = re.fullmatch(r"([ATCGN]+)", sequence, flags=re.IGNORECASE)
    prot_seq = re.fullmatch(r"[ARNDCEQGHILKMFPSTWYV]+",
                            sequence, flags=re.IGNORECASE)
    if dna_seq:
        return "DNA sequence"
    elif prot_seq:
        return "Protein sequence"
    else:
        raise ValueError("Invalid sequence.")


def analyze_record(name, sequence):
    molecule_type = detect_molecule_type(sequence)
    if molecule_type == "DNA sequence":
        d = DNA(sequence)
        d = d.gc_content()
        p = None
    elif molecule_type == "Protein sequence":
        p = Protein(sequence)
        p = p.estimate_mass()
        d = None
    return {"name": name, "type": molecule_type, "length": len(sequence), "gc_content": d, "mass": p}
