import matplotlib.pyplot as plt
import csv
import numpy as np

# part 1 using csv
'''
x = []
y = []

with open('example.txt','r') as csvfile:
  plots = csv.reader(csvfile, delimiter = ',')
  for row in plots:
    x.append(int(row[0]))
    y.append(int(row[1]))

plt.plot(x,y, label = 'loaded from file with csv')
'''

#part 2 using numpy
x,y = np.loadtxt('example.txt', delimiter = ',', unpack = True)

plt.plot(x,y, label = 'loaded from file with numpy')


plt.xlabel('x')
plt.ylabel('y')
plt.title('cool graph')
plt.legend()
plt.show()
