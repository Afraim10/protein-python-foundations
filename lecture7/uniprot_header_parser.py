# Afraim10 biopractice of CS50P: lecture7
import re
import sys
from Bio import (SeqIO, Seq, UniProt)
import csv


def main():
    if len(sys.argv) != 3:
        sys.exit("Only input FASTA file and output CSV path allowed.")
    input_fasta = sys.argv[1]
    if not input_fasta.endswith((".fasta", ".fa")):
        sys.exit("Only FASTA input file (UniProt-format headers) is allowed.")
    output_csv = sys.argv[2]
    records_dict = uniprot_parse(input_fasta)
    csv_writing(output_csv, records_dict)


def uniprot_parse(input, format="fasta" or "fa"):
    records = {}
    for record in SeqIO.parse(input, format):
        records[record.id] = record.description
    return records


def csv_writing(output, records):
    with open(output, "w") as file:
        writer = csv.DictWriter(file, fieldnames=[
                                "accession", "entry_name", "protein_name", "organism", "taxonomy_id", "gene_name"])
        writer.writeheader()
        for key, value in records.items():
            checker = re.search(
                r"(?P<db>(?:tr|sp))\|(?P<accession>\w{6})\|(?P<entry>[A-Z0-9_]+)\s(?P<prot_name>.*?)\sOS=(?P<organism>.*?)(?:\sOX=(?P<taxonomy_id>\d+))?(?:\sGN=(?P<gene>\S+))?(?:\sPE=(?P<protein_level>\d))?(?:SV=(?P<seq_ver>\d))?", value)
            if checker:
                writer.writerow({"accession": checker.group("accession"), "entry_name": checker.group("entry"), "protein_name": checker.group("prot_name"), "organism": checker.group(
                    "organism"), "taxonomy_id": checker.group("taxonomy_id") or "", "gene_name": checker.group("gene") or ""})
            else:
                print(
                    f"Warning: Malformed header skipped: {value}", file=sys.stderr)


main()
