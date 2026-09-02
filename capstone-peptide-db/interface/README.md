# Peptide/Sequence Database (SQLite)

A small command-line tool for persistently storing and querying DNA and protein
sequence records, built on Python's built-in `sqlite3` module.

## What this is

A CRUD-style CLI over a single SQLite table (`biomolecules`), using the
`Biomolecule`/`DNA`/`Protein` class hierarchy from Lecture 8 as the analysis
layer. Add a sequence, and it's automatically classified and analyzed (GC
content for DNA, estimated mass for protein) before being stored.

## What this is not

Not a general-purpose database tool, and not a SQL tutorial. SQL was
genuinely new territory for me going into this — I researched syntax online
while designing the schema and query logic myself. The design decisions
(single-table inheritance mapping directly onto the `Biomolecule` class
hierarchy, parameterized queries to avoid SQL injection) are mine; the exact
keyword syntax for things like `CREATE TABLE` and `GROUP BY` I looked up
rather than already knowing.

## Files

- `models.py` — the `Biomolecule`/`DNA`/`Protein` classes (shared with the
  FASTA batch analyzer capstone in this same repo)
- `db.py` — schema creation and all database operations: `add_record`,
  `list_records`, `query_by_classification`, `delete_record`. Every query
  uses `?` placeholders with bound parameters, never raw string formatting,
  to avoid SQL injection.
- `cli.py` — `argparse`-based entry point (`add`, `list` subcommands)
- `test_db.py` — tests using `sqlite3.connect(":memory:")`, a real but
  disposable in-RAM database, so tests never touch a real data file

## Design notes

The schema is a single table rather than separate `dna`/`protein` tables —
a pattern called single-table inheritance, chosen because it directly
mirrors the Python class hierarchy already in `models.py`: one table for
anything that's fundamentally "a sequence with a length," with
type-specific columns (`gc_content`, `mass`) simply `NULL` when they don't
apply to a given row.

## Usage

```bash
python cli.py add --name "EGFR-fragment" --sequence "ATGGCC..." --type DNA
python cli.py list
```
