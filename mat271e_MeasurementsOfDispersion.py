from matplotlib import pyplot as plt
import numpy as np
import math
import statistics


def avg(L): #Average
    average = sum(L) / len(L)
    return round(average, 7)

def Var_x(L): #Variance
    average = avg(L)
    datacount = len(L)
    E_sum = 0
    for data in L:
        a = (abs(data - average)) ** 2
        E_sum += a
    Var_x = E_sum / datacount
    return round(Var_x, 7)

def S_x(L): #Standard Deviation
    S_x = math.sqrt(Var_x(L))
    return round(S_x, 7)

def CV_x(L): #Variation Coefficient
    average = avg(L)
    CV_x = S_x(L) / average
    return round(CV_x, 7)

def CS_x(L): #Skewness Coefficient
    average = avg(L)
    datacount = len(L)
    std_dev = float(S_x(L))
    E_sum = 0
    for data in L:
        a = (data - average) ** 3
        E_sum += a
    CS_x = (E_sum / datacount) / (std_dev ** 3)
    return round(CS_x, 7)

def K_x(L): #Kurtosis Coefficient
    average = avg(L)
    datacount = len(L)
    std_dev = float(S_x(L))
    E_sum = 0
    for data in L:
        a = (abs(data - average)) ** 4
        E_sum += a
    K_x = ((E_sum / datacount) / (std_dev ** 4)) - 3
    return round(K_x, 7)

#Data set
dataset = [590, 610, 625, 630, 640,
           640, 665, 675, 680, 685,
           690, 690, 690, 695, 710,
           715, 720, 720, 725, 725,
           730, 730, 730, 735, 735,
           740, 740, 745, 755, 760,
           765, 770, 780, 795, 805,
           815, 825, 825, 835, 875]

#Using the .statistics Module
mean = statistics.mean(dataset)
hmean = statistics.harmonic_mean(dataset)
mode = statistics.mode(dataset)
median = statistics.median(dataset)
variance = statistics.pvariance(dataset)
stdev = statistics.pstdev(dataset)

#Results of Dispersion Measurements
print()
print("Sum                  :", sum(dataset))
print("Mean                 :", mean)
print("Harmonic Mean        :", hmean)
print("Mode                 :", mode)
print("Median               :", median)
print("Variance             :", Var_x(dataset))
print("Standard Deviation   :", S_x(dataset))
print("Variance Coefficient :", CV_x(dataset))
print("Skewness Coefficient :", CS_x(dataset))
print("Kurtosis Coefficient :", K_x(dataset))
print()
"""print("--statistics module--")
print("Mean                 :", mean)
print("Harmonic Mean        :", hmean)
print("Mode                 :", mode)
print("Median               :", median)
print("Variance             :", variance)
print("Standard Deviation   :", stdev)
print()"""

#Histograms
 #Histogram
plt.figure(figsize=(7,5.5))
plt.title("Histogram", fontsize=15, fontweight="bold")
plt.xlabel("flood discharge (m^3/s)", fontsize=13)
plt.ylabel("counts", fontsize=13)
plt.xticks(np.arange(580,881,50))
plt.yticks(np.arange(0,16,1))
plt.grid(axis="y", ls="--", fillstyle="left")
plt.hist(dataset, bins=6, range=(580,881), color="#4473c4", rwidth=0.975)
plt.show()

 #Frequency Histogram
plt.figure(figsize=(7,5.5))
plt.title("Frequency Histogram", fontsize=15, fontweight ="bold")
plt.xlabel("flood discharge (m^3/s)", fontsize=12)
plt.ylabel("frequency(%)", fontsize=12)
plt.xticks(np.arange(580,881,50))
plt.yticks(np.arange(0,36,2.5))
plt.grid(axis="y", ls="--", fillstyle="left")
plt.hist(dataset, bins=6, range=(580,881), color="#4473c4", rwidth=0.975,
         weights=(np.ones(len(dataset)) / len(dataset))*100)
plt.show()

 #Cumulative Frequency Histogram
cfh_x = dataset
cfh_y = []
cml_sum = 0
for data in dataset:
    cml_sum += data
    cml_frq = cml_sum / sum(dataset)
    cfh_y.append(cml_frq)

plt.figure(figsize=(7,5.5))
plt.title("Cumulative Frequency Histogram", fontsize=15, fontweight ="bold")
plt.xlabel("flood discharge (m^3/s)", fontsize=12)
plt.ylabel("cumulative frequency", fontsize=12)
plt.xticks(np.arange(580,881,50))
plt.yticks(np.arange(0,1.05,0.05), fontsize=9)
plt.grid(axis="y", ls="--", fillstyle="left")
plt.hist(dataset, bins=6, range=(580,881), color="#4473c4", rwidth=0.975,
         density=True, cumulative=True, weights=dataset)
plt.plot(cfh_x, cfh_y, color="r")
plt.show()
