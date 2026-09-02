import argparse
import csv
from Bio import SeqIO
from analyzer import analyze_record, detect_molecule_type


def main():
    parser = argparse.ArgumentParser(
        description="Multi-sequence FASTA batch analyzer + Report generator")
    parser.add_argument("--fasta", required=True, type=str)
    parser.add_argument("--output", required=False, type=str, default=None)
    args = parser.parse_args()

    data_list = [analyze_record(record_id, seq)
                 for record_id, seq in bio_parser(args.fasta).items()]

    if args.output:
        save_results(args.output, data_list)
    else:
        for row in data_list:
            print(row)


def bio_parser(filepath, format="fasta"):
    parsed = {}
    for record in SeqIO.parse(filepath, format):
        parsed[record.id] = str(record.seq)
    return parsed


def save_results(outputpath, results):
    with open(outputpath, "w") as file:
        writer = csv.DictWriter(
            file, fieldnames=["name", "type", "length", "gc_content", "mass"])
        writer.writeheader()
        for row in results:
            writer.writerow(row)


main()
