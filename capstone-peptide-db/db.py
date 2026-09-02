import sqlite3


def create_connection(db_path="peptides.db"):
    return sqlite3.connect(db_path)


def create_table(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS biomolecules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            molecule_type TEXT NOT NULL,
            sequence TEXT NOT NULL,
            length INTEGER NOT NULL,
            gc_content REAL,
            mass REAL,
            classification TEXT,
            date_added TEXT NOT NULL
        )
    """)
    conn.commit()


def add_record(conn, name, molecule_type, sequence, length,
               gc_content=None, mass=None, classification=None):
    conn.execute("""
        INSERT INTO biomolecules (name, molecule_type, sequence, length,
                                    gc_content, mass, classification, date_added)
        VALUES (?, ?, ?, ?, ?, ?, ?, datetime('now'))
    """, (name, molecule_type, sequence, length, gc_content, mass, classification))
    conn.commit()


def list_records(conn):
    cursor = conn.execute("SELECT * FROM biomolecules")
    return cursor.fetchall()


def query_by_classification(conn, classification):
    cursor = conn.execute(
        "SELECT * FROM biomolecules WHERE classification = ?", (classification,))
    return cursor.fetchall()


def delete_record(conn, record_id):
    cursor = conn.execute(
        "DELETE FROM biomolecules WHERE id = ?", (record_id,))
    conn.commit()
