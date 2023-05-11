# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/01_breakdown-proteins-to-fasta.ipynb.

# %% auto 0
__all__ = ['break_proteins_into_fasta_files']

# %% ../../nbs/01_breakdown-proteins-to-fasta.ipynb 3
from Bio import SeqIO
from pathlib import Path
from yaml import safe_load
from tqdm.auto import tqdm

# %% ../../nbs/01_breakdown-proteins-to-fasta.ipynb 5
def break_proteins_into_fasta_files(
    protein_file_path: Path, 
    write_path: Path,
):
    """
    Insert the fasta-annotated sequence records from our reference genome 
    into our sqlite3 database.
    """
    # This only works for fasta files
    sequences = 0
    with protein_file_path.open("r") as f:
        for line in f.readlines():
            if line.startswith(">"):
                sequences += 1
    progress_bar = tqdm(total=sequences)
    for i, seq_record in enumerate(SeqIO.parse(protein_file_path, "fasta")):
        seq_record_write_path = write_path / f"{seq_record.id}.fasta"
        if not seq_record_write_path.exists():
            with seq_record_write_path.open("w+") as out:
                SeqIO.write([seq_record], out, "fasta")
        progress_bar.update(1)
    progress_bar.close()
