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
origin = [[0.0, 0.0, 1.83]]
d = 100.0

x, y, z = [], [], []
x_temp, y_temp, z_temp = [], [], []
x_to_plot, y_to_plot, z_to_plot = [origin[0][0], 0.0], [origin[0][1], 0.0], [origin[0][2], 0.0]


vel_layers = np.linspace(-15.0, 15.0, num=16)
vel_angles = np.linspace(0.0, 2*math.pi, 100) #TODO: Change to 900 (for 0.4 degree acurracy)

# finding points at given distance from origin
for i in range(len(vel_layers)):
    vel_layers[i] = math.radians(vel_layers[i])
    x_temp.append(origin[0][0] + d*math.cos(vel_layers[i]))
    y_temp.append(0.0)
    z_temp.append(origin[0][2] + d*math.sin(vel_layers[i]))

# pivoting about the z axis
for i in range(len(vel_angles)):
    for j in range(len(x_temp)):

        current_cos = math.cos(vel_angles[i])
        current_sin = math.sin(vel_angles[i])

        current_x = current_cos*x_temp[j] - current_sin*y_temp[j]
        current_y = current_sin*x_temp[j] + current_cos*y_temp[j]
        current_z = z_temp[j] if z_temp[j]>=0 else 0.0

        x.append(current_x)
        y.append(current_y)
        z.append(current_z)

        x_to_plot[1] = current_x
        y_to_plot[1] = current_y
        z_to_plot[1] = current_z

        ax.plot3D(x_to_plot, y_to_plot, z_to_plot, color="y")

# plotting output
ax.scatter(x, y, z, color="y")
ax.scatter(origin[0][0], origin[0][1], origin[0][2], color="r")

############
#  Hokuyo  #
############

origin.append([0.0, 0.0, 0.12])
dir = [0.0, 0.0, 0.0]
d = 5.0

x, y, z = [], [], []
x_temp, y_temp, z_temp = [], [], []
x_to_plot, y_to_plot, z_to_plot = [origin[1][0], 0.0], [origin[1][1], 0.0], [origin[1][2], 0.0]
hok_angles = np.linspace(dir[1]-4.7128898/2, dir[1]+4.7128898/2, num=50)

x_temp.append(origin[0][0] + d*math.cos(dir[0]))
y_temp.append(0.0)
z_temp.append(origin[1][2])

# pivoting about the z axis
for i in range(len(hok_angles)):
    for j in range(len(x_temp)):

        current_cos = math.cos(hok_angles[i])
        current_sin = math.sin(hok_angles[i])

        current_x = current_cos*x_temp[j] - current_sin*y_temp[j]
        current_y = current_sin*x_temp[j] + current_cos*y_temp[j]
        current_z = z_temp[j] if z_temp[j]>=0 else 0.0

        x.append(current_x)
        y.append(current_y)
        z.append(current_z)

        x_to_plot[1] = current_x
        y_to_plot[1] = current_y
        z_to_plot[1] = current_z

        ax.plot3D(x_to_plot, y_to_plot, z_to_plot, color="g")

ax.scatter(x, y, z, color="g")
ax.scatter(origin[1][0], origin[1][1], origin[1][2], color="r")

############
#  Camera  #
############

origin.append([0.0, 0.0, 0.35])
dir = [0.0, 0.0, 0.0]
d = 20.0

cam_layers = np.linspace(math.radians(-37.0), math.radians(37.0), num=20)
cam_angles = np.linspace(math.radians(-31.0), math.radians(31.0), num=20)

x, y, z = [], [], []
x_temp, y_temp, z_temp = [], [], []
x_to_plot, y_to_plot, z_to_plot = [origin[2][0], 0.0], [origin[2][1], 0.0], [origin[2][2], 0.0]

# finding points at given distance from origin
for i in range(10):
    cam_layers[i] = math.radians(cam_layers[i])
    x_temp.append(origin[2][0] + d*math.cos(cam_layers[i]))
    y_temp.append(0.0)
    z_temp.append(origin[2][2])

# pivoting about the z axis
for k in range(len(cam_layers)):
    for i in range(len(cam_angles)):
        for j in range(len(x_temp)):
            current_cos = math.cos(cam_angles[i])
            current_sin = math.sin(cam_angles[i])

            current_x = current_cos*x_temp[j] - current_sin*y_temp[j]
            current_y = current_sin*x_temp[j] + current_cos*y_temp[j]
            current_z = z_temp[j] + d*math.sin(cam_layers[k]) if z_temp[j] + d*math.sin(cam_layers[k])>=0 else 0.0

            x.append(current_x)
            y.append(current_y)
            z.append(current_z)

            x_to_plot[1] = current_x
            y_to_plot[1] = current_y
            z_to_plot[1] = current_z

            ax.plot3D(x_to_plot, y_to_plot, z_to_plot, color="b")

# plotting output
ax.scatter(x, y, z, color="b")
ax.scatter(origin[2][0], origin[2][1], origin[2][2], color="r")

x = [row[0] for row in origin]
y = [row[1] for row in origin]
z = [row[2] for row in origin]

ax.plot3D(x, y, z)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()