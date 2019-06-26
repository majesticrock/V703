import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def csv_read(pathToFile, delimiter=";"):
    with open(pathToFile, "r") as f:
        content = []
        for line in f:
            content.append((line.rstrip()).split(delimiter))
    return content

def func(x, a, b):
    return a*x + b

#Messdauer 150s
n=19

werte = csv_read("csv/charak.csv")
xdata = np.zeros(n)
ydata = np.zeros(n)
errY = np.zeros(n)
ignore = True
i=0

for values in werte:
    if(ignore):
        ignore = False
    else:
        xdata[i] = float(values[0])
        ydata[i] = float(values[3])
        errY[i] = np.sqrt(float(values[1]))/150
        #errY[i] = np.sqrt(float(values[2]))
        i+=1

x_line = np.linspace(np.amin(xdata), np.amax(xdata))
plt.errorbar(xdata, ydata, yerr=errY, fmt = ".", label="Messwerte")
popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(x_line, func(x_line, *popt), "r-", label="Fit")

plt.xlabel(r"$U$ / V")
plt.ylabel(r"$\frac{N}{t}$ / $\frac{\symup{1}}{s}$")

print("a = " + str(popt[0]) + " +/- " + str(pcov[0][0]) )
print("b = " + str(popt[1]) + " +/- " + str(pcov[1][1]) )

plt.legend()
plt.tight_layout()
plt.savefig("build/plot_charak.pdf")
