import argparse
from db import (create_connection, create_table, add_record,
                list_records, query_by_classification, delete_record)
from models import DNA, Protein


def main():
    parser = argparse.ArgumentParser(description="Peptide/sequence database")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--name", required=True)
    add_parser.add_argument("--sequence", required=True)
    add_parser.add_argument(
        "--type", choices=["DNA", "protein"], required=True)

    subparsers.add_parser("list")
    query_parser = subparsers.add_parser("query")
    query_parser.add_argument("--classification", required=True)
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", type=int, required=True)

    args = parser.parse_args()
    conn = create_connection()
    create_table(conn)

    if args.command == "add":
        if args.type == "DNA":
            obj = DNA(args.sequence)
            gc = obj.gc_content()
            mass = None
            classification = "DNA sequence"
        elif args.type == "protein":
            obj = Protein(args.sequence)
            gc = None
            mass = obj.estimate_mass()
            classification = "Protein sequence"

        add_record(
            conn,
            name=args.name,
            molecule_type=args.type,
            sequence=obj.sequence,
            length=len(obj),
            gc_content=gc,
            mass=mass,
            classification=classification
        )
        print("Record added.")

    elif args.command == "list":
        records = list_records(conn)
        if records:
            for row in records:
                print(row)
            print(f"\n{len(list_records(conn))} record(s) listed.")
        else:
            print(f"\nNo records listed. Table is empty.")

    elif args.command == "query":
        records = query_by_classification(conn, args.classification)

        if records:
            for row in records:
                print(row)
            print(f"\n{len(records)} classified record(s) listed.")
        else:
            print("No classified records found.")

    elif args.command == "delete":
        deleted = delete_record(conn, args.id)
        if deleted:
            print(f"Record {args.id} deleted.")
        else:
            print("No record found.")


if __name__ == "__main__":
    main()
