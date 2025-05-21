import scipy.stats
import numpy as np


patinetA_Left_venn = input("**important**: make sure that when setting up your morisita distance Venn diagrams that the earlier timepoint goes in the left venn, and the later timepoints goes in the right venn! please enter the value in the left venn for patient A")
patinetA_center = input("please enter the value in the center of the venns for patient A")
patinetA_Right_venn = input("please enter the value in the right venn for patient A")


patinetB_Left_venn = input("please enter the value in the left venn for patient B")
patinetB_center = input("please enter the value in the center of the venns for patient B")
patinetB_Right_venn = input("Please enter the value in the right venn for patient B")

PatientA = [int(patinetA_Left_venn),int(patinetA_center),int(patinetA_Right_venn)]
PatientB = [int(patinetB_Left_venn),int(patinetB_center),int(patinetB_Right_venn)]
data = np.array([PatientA,PatientB])
answer = scipy.stats.contingency.chi2_contingency(data)
textanswer = [str(answer[0]), str(answer[1])]
if answer[1]<=0.05:
    print("Success!: Your patients have significantly different distributions according to their morisita distance venn diagrams accoring to a Chi-Square Test \n Your Chi-Square Test Statistic is: " + textanswer[0] + " and the associated p-value is: " + textanswer[1])
elif answer[1] > 0.05:
    print("Although your patients do not have significantly different distributions of morisita distance vennsl, the chi-square test statistic is: " + textanswer[0] + " and the associated p-value is: " + textanswer[1])
