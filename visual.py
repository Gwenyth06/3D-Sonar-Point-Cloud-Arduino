import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the points from the file
points = []

with open("points.txt", "r") as file:
    for line in file:
        x, y, z = map(float, line.strip().split(','))
        points.append((x, y, z))

# Separate the points into x, y, and z lists
xs, ys, zs = zip(*points)

# Plot the points
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xs, ys, zs, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()