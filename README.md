# ODoherty-Lab
Welcome
Code used by the O'Doherty Laboratory at Emory University (www.odohertylab.com)

Below is a short description of each of the projects that are stored in this repository. 

**Standalone Morisita Analyses**

This project contains two standalone files which can be run by an end user to do all the morisita based analyses for the paper. There are two versions which can be used depending on if you have input data in the comma-seperated-values (csv) or excel (xlsx) file format
includes: Morisita_Dist_Code_CSV.py, Morisita_Dist_Code_ExcelFile.py

**Chi-Square analysis of Venn Diagram**

This project takes two individual's venn diagrams of turnover, and determines if the venn diagrams are differently distributed. Since so much of this program is up to user input, it can be used to also compare two different venn diagrams within an individual (for instance, TCR vs proviruses).
includes: venndiagramsChiSquare.py

**Automated Chi-Square Analyses**

This project focuses on various ways to automate the Chi-Square analyses from Weissman and Ginda et al 2025. 
this file takes a series of fasta turned to excel inputs (which report the following as a column: "Participant.Year1.Year2.Proviral" and "Participant.Year1.Year2.TCR")
This project goes through every participant provided, and for each year combination, it compares if the TCR and proviral venn diagrams are different distributed according to a Chi-Square analysis.
includes: Automated Chi Square.py
