import matplotlib.pyplot as plt

'''x = [2,4,6,8,10]
y = [6,7,8,2,4]

x2 = [1,3,5,7,9]
y2 = [2,4,6,8,10]

plt.bar(x,y,label = "Bar1", color= 'b')
plt.bar(x2,y2,label = "Bar2", color= 'y')'''

population_ages = [11,22,33,44,55,66,77,88,99,110,121,132,122,111,100,90,52,65,77,82,95]

#ids = [x for x in range(len(population_ages))]

#plt.bar(ids, population_ages)
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130,140]
plt.hist(population_ages, bins, histtype= 'bar', rwidth=0.8)


plt.xlabel('x')
plt.ylabel('y')

plt.title('cool graph')
plt.legend()
plt.show()
