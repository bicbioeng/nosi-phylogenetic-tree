'''
Created By: Anushuya Baidya
Date: 7/3/2024
'''
from Bio import SeqIO


def fasta_to_fastq(fasta_file, fastq_file, quality=40):
    with open(fastq_file, "w") as output_handle:
        for record in SeqIO.parse(fasta_file, "fasta"):
            record.letter_annotations["phred_quality"] = [quality] * len(record.seq)
            SeqIO.write(record, output_handle, "fastq")


if __name__ == '__main__':
    fasta_file = "data/kegg/br01553.fasta"
    fastq_file = "data/kegg/br01553.fastq"
    fasta_to_fastq(fasta_file=fasta_file, fastq_file=fastq_file)
