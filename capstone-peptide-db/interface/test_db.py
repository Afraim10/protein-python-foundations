from db import create_connection, create_table, add_record, list_records, query_by_classification, delete_record


def test_add_and_list():
    conn = create_connection(":memory:")
    create_table(conn)
    add_record(conn, "Test-A", "protein", "MKV", 3,
               mass="352.02 Da", classification="short peptide")
    records = list_records(conn)
    assert len(records) == 1
    assert records[0][1] == "Test-A"   # column index 1 = name


def test_query_by_classification():
    conn = create_connection(":memory:")
    create_table(conn)
    add_record(conn, "GeneA", "DNA", "ATCG", 4,
               gc_content=50.0, classification="DNA sequence")
    add_record(conn, "ProtB", "protein", "MKV", 3,
               classification="Protein sequence")
    dna_records = query_by_classification(conn, "DNA sequence")
    assert len(dna_records) == 1
    assert dna_records[0][1] == "GeneA"


def test_delete_record():
    conn = create_connection(":memory:")
    create_table(conn)
    add_record(conn, "GeneA", "DNA", "ATCG", 4,
               gc_content=50.0, classification="DNA sequence")
    records = list_records(conn)
    record_id = records[0][0]
    delete_record(conn, record_id)
    assert len(list_records(conn)) == 0
