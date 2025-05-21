# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from scipy.stats import chi2_contingency
import os
import numpy as np
import re
import fnmatch
import pandas as pd
#we start by getting the name of the patient, the filename and working directory for the file we want to collect the clones of 
Patient = input(
    "Please insert the name of the patient we are collecting clones of: ")
working_directory = input(
    "Please enter the working directory for which the fasta file (that has been turned into an excel) is stored, removing quotation marks if you are on a windows computer: ")
os.chdir(working_directory)
filename = input(
    "Please enter the filepath for the fasta turned excel file, removing quation marks if you are on a windows computer: ")
df = pd.read_excel(filename)




def Chianalysis (Venn1,Venn2,a):

 
    # defining the table
    data = [Venn1,Venn2]
    stat, p, dof, expected = chi2_contingency(data)
 
    # interpret p-value
    alpha = 0.05
    print("p value is " + str(p))
    if p <= alpha:
       # print('Dependent (reject H0)')\
        q = {a,str(p),"Dependent (reject H0)"}
        return(pd.DataFrame({"Comparison":[a],"p":[str(p)],"conclusion": ["Dependent (reject H0)"]}))
    else:
       # print('Independent (H0 holds true)')
       q = {a,str(p),"Dependent (reject H0)"}
       return(pd.DataFrame({"Comparison":[a],"p":[str(p)],"conclusion":["Independent (H0 holds true)"]}))
    return()
Q = {"A","a"}

dfq = pd.DataFrame(columns =["Comparison", "p", "conclusion"])
for inda in df.index:
    if pd.isna(df["Participant.Year1.Year2.Proviral"][inda]) == False:
                    print (df["Participant.Year1.Year2.Proviral"][inda])
                    print ("vs")
                    print(df["Participant.Year1.Year2.TCR"][inda])
                    Venn1 =[df["Left Venn"][inda]+df["Center Venn"][inda],df["Right Venn"][inda]]
                    Venn2 =[df["Left Venn.1"][inda]+df["Center Venn.1"][inda],df["Right Venn.1"][inda]]
                    a = df["Participant.Year1.Year2.Proviral"][inda] + " VS " + df["Participant.Year1.Year2.TCR"][inda]
                    dfq = pd.concat([dfq,Chianalysis(Venn1, Venn2,a)])
                    Patient = str(Patient)
dfq.to_excel(working_directory+ '\Patient'+"CHId.xlsx")
            
        
        