import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math

fig = plt.figure()
ax = plt.axes(projection='3d')

############
# Velodyne #
############

# finding lines in 2D (x-z plane)
origin = [0.0, 1.83, 0.0]
r = 100
d = np.linspace(0.0, 100.0, num=900)
x, y, z = [], [], []
x_temp, y_temp, z_temp = [], [], []


vel_angles = np.linspace(-15.0, 15.0, num=16)
angles = np.linspace(0.0, 2*math.pi, 20)

# finding points at given distance from origin
for i in range(len(vel_angles)):
    vel_angles[i] = math.radians(vel_angles[i])
    for j in range(len(d)):
        x_temp.append(origin[0] + d[j]*math.cos(vel_angles[i]))
        y_temp.append(0.0)
        z_temp.append(origin[2] + d[j]*math.sin(vel_angles[i]))

# pivoting about the z axis
for i in range(len(angles)):
    for j in range(len(x_temp)):
        current_cos = math.cos(angles[i])
        current_sin = math.sin(angles[i])
        x.append(current_cos*x_temp[j] - current_sin*y_temp[j])
        y.append(current_sin*x_temp[j] + current_cos*y_temp[j])
        z.append(z_temp[j])

# plotting output
ax.plot3D(x, y, z)
ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

plt.show()