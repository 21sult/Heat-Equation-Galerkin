import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.size': 14})

def readfile(filename):
    file = open(filename)
    next(file)
    x = []
    y = []
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))
    return {'x':x, 'y':y}

def analitica(x_list):
    v = []
    for x in x_list:
        v.append( (np.exp(x) - np.exp(20 - x)) / (1 - np.exp(20)) )
    return v

x_an = np.linspace(0, 10, 100000)
y_an = analitica(x_an)

plot1 = readfile('data1.txt')
x_n1 = plot1['x']
y_n1 = plot1['y']

plot2 = readfile('data2.txt')
x_n2 = plot2['x']
y_n2 = plot2['y']

plot3 = readfile('data3.txt')
x_n3 = plot3['x']
y_n3 = plot3['y']

plot4 = readfile('data4.txt')
x_n4 = plot4['x']
y_n4 = plot4['y']

plot5 = readfile('data5.txt')
x_n5 = plot5['x']
y_n5 = plot5['y']

plt.title(r'$u(x)$ analítico e aproximado da equação do calor')
plt.xlabel(r'$ x $')
plt.ylabel(r'$ u(x) $')
plt.plot(x_an, y_an, label = "Sol. Analítica.", color = 'navy', alpha = 0.5)
plt.plot(x_n1, y_n1, label = r'$\Delta x = 1.0$' , color = "red"   , linestyle = '--')
plt.plot(x_n2, y_n2, label = r'$\Delta x = 0.5$' , color = "green" , linestyle = '--')
plt.plot(x_n3, y_n3, label = r'$\Delta x = 0.1$' , color = "blue"  , linestyle = '--')
plt.plot(x_n4, y_n4, label = r'$\Delta x = 0.01$', color = "magenta", linestyle = '--')
plt.plot(x_n5, y_n5, label = r'$\Delta x = 0.001$', color = "brown", linestyle = '--')
plt.legend()

plt.show()