# Import the random module.
import random 
import numpy as np
import timeit
%timeit np.random.uniform(-90.000, 90.000, size=1500)
random.randint(-90, 90)
print(random.randint(-90, 90))

x = 1
latitudes = []
while x < 11:
    random_lat = random.randint(-90, 90) + random.random()
    latitudes.append(random_lat)
    x += 1
print(latitudes)

random.randrange(-90, 90, step=1)

np.random.uniform(low=-90, high=90)
np.random.uniform(-90.000, 90.000)
%timeit np.random.uniform(-90.000, 90.000, size=1500) #print(np.random.uniform(-90.000, 90.000, size=50))
