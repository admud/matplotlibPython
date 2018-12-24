import matplotlib.pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,7,10,8]
eating = [2,3,4,3,2]
working = [7,8,7,8,8]
playing = [3,4,5,2,6]

slices = [7,2,2,13]

activities = ['sleeping','eating','working','playing']

plt.pie(slices,
labels = activities,
  colors= ['m','c','r','b'],
   startangle= 90,
    shadow  = True,
     explode= (0,0,.1,0),
     autopct = '%1.1f%%')

#plt.xlabel('x')
#plt.ylabel('y')
plt.title('cool graph')
#plt.legend()
plt.show()
