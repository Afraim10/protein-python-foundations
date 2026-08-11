# Afraim10 biopractice of CS50P: lecture5
import pytest
from codon_cli import split_codons


def test_no_repeated_codons_lost():
    assert split_codons("ATGATG") == ["ATG", "ATG"]
    assert split_codons("GGCGGCGGCATCATCCGACGA") == [
        'GGC', 'GGC', 'GGC', 'ATC', 'ATC', 'CGA', 'CGA']


def test_simple_sequence():
    assert split_codons("ATGGCCTAA") == ["ATG", "GCC", "TAA"]


def test_empty_sequence():
    assert split_codons("") == []


def test_nonDNA_bases():
    with pytest.raises(ValueError):
        split_codons("ATCTACATAXATACTGAGATA")


def test_unsuitable_length():
    with pytest.raises(ValueError):
        split_codons("ACTACACGTACGTCCGTACGATGATCGG")
