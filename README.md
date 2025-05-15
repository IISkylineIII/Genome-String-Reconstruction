# Genome-String-Reconstruction

This script reconstructs a genome string from a list of paired (k,d)-mers using greedy overlap merging.

# Function
reconstruct_string(paired_reads)
Reconstructs the original DNA sequence from overlapping paired reads by identifying maximum suffix-prefix matches and merging them iteratively.

# Input
A list of tuples, where each tuple contains a pair of strings representing a (k,d)-mer:

```
paired_reads = [('ACC', 'ATA'), ('ACT', 'ATT'), ..., ('TTC', 'GAA')]
```
# Output

TTCGGACT

Usage 

```
result = reconstruct_string(paired_reads)
print(result)
```
# Application
* This method is used in genome assembly pipelines to reconstruct longer DNA sequences from short sequencing reads, particularly in paired-end sequencing where reads are separated by a known gap. It is useful in:
* Assembling genomes from short reads
* Reconstructing contigs in metagenomic analysis
* Exploring the structure of microbial or viral genomes from fragmented data

# Requirements
*Python 3.x
* No external libraries required


# License
* This project is licensed under the MIT License – see the LICENSE file for more details.
