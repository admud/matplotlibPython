import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,7,10,8]
eating = [2,3,4,3,2]
working = [7,8,7,8,8]
playing = [3,4,5,2,6]

#fake labels as stack plot does not allow labels :(
plt.plot([],[], color = 'm', label = 'Sleeping', linewidth = 10)
plt.plot([],[], color = 'c', label = 'Eating', linewidth = 10)
plt.plot([],[], color = 'r', label = 'Working', linewidth = 10)
plt.plot([],[], color = 'b', label = 'Playing', linewidth = 10)


plt.stackplot(days,sleeping, eating , working, playing, colors= ['m','c','r','b'])

plt.xlabel('x')
plt.ylabel('y')
plt.title('cool graph')
plt.legend()
plt.show()
