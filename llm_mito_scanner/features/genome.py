# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01_insert-genome-into-db.ipynb.

# %% auto 0
__all__ = ['insert_genome_into_sqlite']

# %% ../../nbs/01_insert-genome-into-db.ipynb 3
from pathlib import Path
from Bio import SeqIO
import sqlite3
from . import database

# %% ../../nbs/01_insert-genome-into-db.ipynb 8
def insert_genome_into_sqlite(
    genome_file_path: Path, 
    sqlite_connection: sqlite3.Connection, 
    insert_batch_size: int = 10
):
    """
    Insert the fasta-annotated sequence records from our reference genome 
    into our sqlite3 database.
    """
    records = []
    for i, seq_record in enumerate(SeqIO.parse(genome_file_path, "fasta")):
        records.append(seq_record)
        if i % insert_batch_size == 0:
            database.insert_sequences(records, sqlite_connection)
            records = []
    if len(records) > 0:
        database.insert_sequences(records, sqlite_connection)
