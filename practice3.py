import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [2,3,4,5,6,7,8,9]

plt.scatter(x,y,label ='skitscat', color= 'k',marker= "X", s =  100)


plt.xlabel('x')
plt.ylabel('y')

plt.title('cool graph\nCheck it out sonny')
plt.legend()
plt.show()
