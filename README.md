![course-card](images/usd-card.png)

# University of South Dakota: Phylogenetic Analysis


## Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Getting Started](#getting-started)
- [Software Requirements](#software-requirements)
- [Workflow Diagrams](#workflow-diagrams)
- [Submodule 1 Understanding the Basics of Phylogenetic](#submodule-1-understanding-the-basics-of-phylogenetic)
- [Submodule 2 Collect and Prepare Sequence Data and Analysis](#submodule-2-collect-and-prepare-sequence-data-and-analysis)
- [Submodule 3 Construct Phylogenetic Tree](#submodule-3-construct-phylogenetic-tree)
- [Submodule 4 Analyze Phylogenetic Tree](#submodule-4-analyze-phylogenetic-tree)
- [Data](#data)
- [Troubleshooting](#troubleshooting)
- [Funding](#funding)
- [License for Data](#license-for-data) 


## **Overview**
This README should walk the learner through the background and steps necessary to complete this training module. To use our module, clone this repo using `git clone https://github.com/bicbioeng/nosi-phylogeny-draft.git` and then navigate to the directory for this project.

The study and understanding of phylogenetic trees have become an indispensable part of modern biological research. Phylogenetic trees provide profound insights into the evolutionary relationships between. They also help in understanding the spread of diseases, such as the origin and evolution of pathogens, the time and space distribution of prevalence, and the prediction of pathogen transmission trends. Additionally, phylogenetic trees are used to study the functional genomics of various species, including the emergence of new body plans or metabolism, molecular adaptation, morphological character evolution, and demographic changes in recently diverged species. The advancement of sequencing technologies has greatly contributed to the analysis of phylogenetic trees, allowing for the analysis of large datasets, including whole genomes. Overall, phylogenetic trees play a crucial role in various biological disciplines, providing valuable insights into the evolutionary history and functional genomics of organisms.

This README describes the tutorials in our step-by-step analytic workflow. These submodules cover the end-to-end workflow of a standard phylogenetic analysis, starting at extracting a gene sequence to creating a phylogenetic tree to analyzing the tree.


## **Learning Objectives:**
The phylogenetic analysis modules will serve for undergraduate through graduate level.

L01: Comprehensive Phylogenetic Analysis for Disease Dynamics
This learning objective aims to provide participants with the knowledge and skills needed to utilize phylogenetic trees in understanding the spread of diseases. By the end of this module, participants will be able to trace the origin and evolution of pathogens, analyze the distribution of disease prevalence over time and space, and predict trends in pathogen transmission using phylogenetic analysis.

L02: Phylogenetics in Functional Genomics and Evolutionary Studies
This learning objective is designed to enable participants to apply phylogenetic analysis to study the functional genomics of various species. Participants will learn how to investigate the emergence of new body plans, molecular adaptations, and morphological character evolution, as well as understand demographic changes in recently diverged species through the construction and interpretation of phylogenetic trees.


The course consists of 4 learning submodules:

*Submodule #1: Understanding the Basics of Phylogenetic*  
*Submodule #2: Collect and Prepare Sequence Data and Analysis*  
*Submodule #3: Construct Phylogenetic Tree*  
*Submodule #4: Analyze Phylogenetic Tree* 

## **Software Requirements**

Our Analysis Workflow Toolkits includes the following tools: 
- Jupyther Notebook
- FastQC
- MultiQC
- Trimmomatic
- Blast
- ClustalW
- USHER
- RAxML
- FigTree
- iTOL
- MUMmer
- BEAST

Each dependency will be loaded at the beginning of the module and will allow the user to understand the context in which the package is relevant to our analytic process.

## **Workflow Diagram**

## Bioinformatics Workflow Diagrams

![USD workflow](images/allmodules.png)
Figure 2: Our learning objectives encompass a comprehensive understanding of phylogenetic analysis, from data collection and
preparation to tree construction and interpretation, enabling participants to conduct meaningful analysis in diverse metagenomic
context

## General Overall Process
![general overall process](images/workflow.png)


## Submodule 1 Understanding the Basics of Phylogenetic

A phylogenetic tree is a visual representation that illustrates the evolutionary connections and ancestral relationships among different biological species or organisms. It depicts how closely related these species are based on similarities and differences in their physical traits or genetic makeup. This submodule will expose the learner to fundamental concepts of phylogenetic tree.

## Submodule 2 Collect and Prepare Sequence Data and Analysis

This submodule shows how to collect and prepare gene sequence data for phylogenetic tree analysis

## Submodule 3: Construct Phylogenetic Tree
This includes series of steps to construct phylogenetic tree ranging from sequence alignment to tree reconstruction

## Submodule 4: Analyze Phylogenetic Tree
This submodule includes analyzing the phylogenetic tree for comparative metagenomics and ancestral state reconstruction.

## Data
This training module will use 6 different datasets to cover the diversity of our problem for each of the use cases shown.
- UC1(Covid Epidemiology): --
- UC2(Protein Alignment): --
- UC3(Pan-genomics & Core Genome): --
- UC4(Cancer): --
- UC5(Ecology (NIF Bacteria)): --
- UC6(Protein - IFA - RNASeq): --



## Troubleshooting

Common errors encountered in this workflow include: 
1. Missing file. This error can have multiple causes:
    - Wrong file path: Find the correct file in notebook directories, then update the correct file path.
    - File does not exist: Find path in the provided bucket or notebook and update command.
    - File was not generated: Check previous steps make sure previous step run successfully.
2. ----


## Funding

Funded by the South Dakota INBRE Program NIH/NIGMS P20 GM103443.


## License for Data

All data and download files in STRING-DB are freely available under a 'Creative Commons BY 4.0' license.

Text and materials are licensed under a Creative Commons CC-BY-NC-SA license. The license allows you to copy, remix and redistribute any of our publicly available materials, under the condition that you attribute the work (details in the license) and do not make profits from it. More information is available [here](https://tilburgsciencehub.com/about/#license).

![Creative commons license](https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png)

This work is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-nc-sa/4.0/)

