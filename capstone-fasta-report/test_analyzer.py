from analyzer import detect_molecule_type, analyze_record
import pytest


def test_detect_dna():
    assert detect_molecule_type("ATCGATCG") == "DNA sequence"
    assert detect_molecule_type("CGATAGCCGATTGACATCGATCG") == "DNA sequence"
    with pytest.raises(ValueError):
        detect_molecule_type("ATTCCAGTAATGFACCGATAGAJACTACCGG")


def test_detect_protein():
    assert detect_molecule_type("MKVLQP") == "Protein sequence"
    assert detect_molecule_type("MLTRSKVQ") == "Protein sequence"
    with pytest.raises(ValueError):
        detect_molecule_type("MKAZZXRSKVZXBX")


def test_analyze_records():
    assert analyze_record("seq3_DNA", "ATGTCACCACAAACAGAGACTAAAGCAAGTGTTGGATT") == {
        "name": "seq3_DNA", "type": "DNA sequence", "length": len("ATGTCACCACAAACAGAGACTAAAGCAAGTGTTGGATT"), "gc_content": 39.47, "mass": None}
    assert analyze_record(">seq2_Protein", "MKLLTFASAQAAPVAASVGAPVQSQTDAAVLYQPVLFFLLTFGAPQTDAPVAS") == {
        "name": ">seq2_Protein", "type": "Protein sequence", "length": len("MKLLTFASAQAAPVAASVGAPVQSQTDAAVLYQPVLFFLLTFGAPQTDAPVAS"), "gc_content": None, "mass": 5848.02}
