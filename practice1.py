import matplotlib.pyplot as plt

x = [1,2,3]
y= [5,4,7]

x2 = [1,2,3]
y2 = [10,11,12]

plt.plot(x,y,label = "First")
plt.plot(x2,y2,label = "Second")


plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('cool graph')
plt.legend()
plt.show()
