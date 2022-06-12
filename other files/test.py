import numpy as np
import random

n = 10
theta = np.array(sorted(np.random.rand(n) * (2 * np.pi)))
print(theta)

x = []
y = []
radii = random.randrange(0, 1000)
for i in range(n):
    x.append(radii * np.cos(theta[i]))
    y.append(radii * np.sin(theta[i]))
    offset = random.randrange(100, 200)
    radii = random.randrange(radii - offset, radii + offset)

coordinates = list(zip(x, y))

text = "POLYGON (("
for i in range(len(coordinates)):
    text = text + str(coordinates[i][0])+" " + str(coordinates[i][1]) + ", "
text += str(coordinates[0][0]) + " " + str(coordinates[0][1]) + "))"
print(text)
