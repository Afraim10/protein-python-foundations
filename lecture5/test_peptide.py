# Afraim10 biopractice of CS50P: lecture5
from peptide_classifier import estimate_mass, classify_prot
import pytest


def test_short_peptide():
    assert classify_prot('10') == "short peptide"


def test_boundary_19_vs_20():
    assert classify_prot('19') == "short peptide"
    assert classify_prot('20') == "peptide"


def test_boundary_50_vs_51():
    assert classify_prot('50') == "peptide"
    assert classify_prot('51') == "small protein"


def test_small_protein():
    assert classify_prot('60') == "small protein"
    assert classify_prot('150') == "small protein"


def test_boundary_300_vs_301():
    assert classify_prot('300') == "small protein"
    assert classify_prot('301') == "large protein"


def test_large_protein():
    assert classify_prot('504') == "large protein"
    assert classify_prot('325') == "large protein"


def test_0_residues():
    with pytest.raises(ValueError):
        classify_prot('0')
    with pytest.raises(ValueError):
        estimate_mass('-5')


def test_estimate_mass():
    assert estimate_mass('504') == "55.46 KDa"
    assert estimate_mass('20') == "2218.02 Da"


def test_str():
    with pytest.raises(ValueError):
        estimate_mass("cat")
    with pytest.raises(ValueError):
        classify_prot("cat")
