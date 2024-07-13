'''
Created By: Anushuya Baidya
Date: 7/12/2024
'''
import subprocess

# Define the paths
fasta_file = "data/kegg/br01553.fasta"
clustalw_exe = "C:\\Program Files (x86)\\ClustalW2\\clustalw2.exe"
seq_algn_file = "data/kegg/br01553.aln"
# Run ClustalW for multiple sequence alignment using subprocess
try:
    subprocess.run([clustalw_exe, "-INFILE=" + fasta_file, "-OUTFILE=" + seq_algn_file, "-OUTPUT=FASTA"], check=True)
except subprocess.CalledProcessError as e:
    print("Error running ClustalW:", e)
    exit(1)
