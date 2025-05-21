# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 19:06:28 2024

@author: liams
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 14:53:57 2022

@author: Liam
"""
import numpy as np
import pandas as pd
import os as os

    #to start you gotta measure simpson
def Simpson(app):
    n = app.sum()
    top = np.multiply(app, app-1)
    top = top.sum()
    Bottom = n*n-1
    return (top/Bottom)

#now we will use these simpson scores to calculate the Morisita Distance
def Morisita_Dist(Patient):
    cwd = input("Please enter the location on your computer that your .xlsx file you would like to compute Morisita Distance with can be found. For instance, if the file is stored on your desktop, please enter the filepath up to the word desktop, (if on a windows computer, remember to remove quotation marks!): ")
    os.chdir(cwd)
    Patient = input("please paste your full filepath, making sure to delete any quotation marks: ")
    sheet = input("please enter the name of the sheet the patient is on:")
    sheet = str(sheet)
    T1 = input("please enter a year to analyze: ")
    T2 = input("please enter the other year to analyze: ")
    xls = pd.ExcelFile(Patient)
    Timepoint1 = pd.read_excel(xls, sheet, index_col=(0), header=(0))
    print(Timepoint1)
    Timepoint1.dropna()
    T1 = int(T1)
    T2 = int(T2)
    #Timepoint1 = Timepoint1[T1]
    Timepoint1 = Timepoint1.loc[T1]
    Timepoint2 = pd.read_excel(xls, sheet, index_col=(0), header=(0))
    Timepoint2.dropna()
    #Timepoint2 = Timepoint2[T2]
    Timepoint2 = Timepoint2.loc[T2]
    D1 = Simpson(Timepoint1)
    D2 = Simpson(Timepoint2)
    BothTimes = np.multiply(Timepoint1, Timepoint2)
    BothTimes = BothTimes.sum()
    T1Size = Timepoint1.sum()
    T2Size = Timepoint2.sum()
    TOP = 2*BothTimes
    BOTTOM = T1Size*T2Size
    Center = TOP/BOTTOM
    ans = np.squeeze((D1+D2)/(D1+D2+Center))
    normCoeff = 1/(D1+D2+Center)
    D1norm = normCoeff*D1
    D2norm = normCoeff*D2
    CenterNorm = normCoeff*Center
    print("the Left Flank is: ")
    print(D1)
    print("the Right Flank is: ")
    print(D2)
    print('and the center is: ')
    print(Center)
    print("the normalized Left Flank is: ")
    print(D1norm)
    print("the normalized Right Flank is: ")
    print(D2norm)
    print('and the normalized center is: ')
    print(CenterNorm)
    print("Your Morisita Distance is: ")
    return print(ans)
 
