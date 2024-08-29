import numpy as np
import math
import json

# Prepare data export function
def export_data(filename, *data_sets):
    all_data = []
    for data in data_sets:
        sensor_data = []
        for i in range(len(data[0])):
            sensor_data.append({
                'x': data[0][i],
                'y': data[1][i],
                'z': data[2][i],
                'color': data[3]  # Color assigned to the sensor data
            })
        all_data.append(sensor_data)
    
    with open(filename, 'w') as file:
        json.dump(all_data, file, indent=4)

# Velodyne Sensor
origin = [[0.0, 0.0, 1.83]]
d = 100.0

x, y, z = [], [], []
x_temp, y_temp, z_temp = [], [], []
vel_layers = np.linspace(-15.0, 15.0, num=16)
vel_angles = np.linspace(0.0, 2*math.pi, 100)

for i in range(len(vel_layers)):
    vel_layers[i] = math.radians(vel_layers[i])
    x_temp.append(origin[0][0] + d*math.cos(vel_layers[i]))
    y_temp.append(0.0)
    z_temp.append(origin[0][2] + d*math.sin(vel_layers[i]))

for i in range(len(vel_angles)):
    for j in range(len(x_temp)):
        current_cos = math.cos(vel_angles[i])
        current_sin = math.sin(vel_angles[i])
        current_x = current_cos*x_temp[j] - current_sin*y_temp[j]
        current_y = current_sin*x_temp[j] + current_cos*y_temp[j]
        current_z = z_temp[j] if z_temp[j] >= 0 else 0.0

        x.append(current_x)
        y.append(current_y)
        z.append(current_z)

# Hokuyo Sensor
origin.append([0.0, 0.0, 0.12])
d = 5.0

x_temp, y_temp, z_temp = [], [], []
hok_angles = np.linspace(-math.pi/2, math.pi/2, num=50)

x_temp.append(origin[0][0] + d*math.cos(0.0))
y_temp.append(0.0)
z_temp.append(origin[1][2])

for i in range(len(hok_angles)):
    for j in range(len(x_temp)):
        current_cos = math.cos(hok_angles[i])
        current_sin = math.sin(hok_angles[i])
        current_x = current_cos*x_temp[j] - current_sin*y_temp[j]
        current_y = current_sin*x_temp[j] + current_cos*y_temp[j]
        current_z = z_temp[j] if z_temp[j] >= 0 else 0.0

        x.append(current_x)
        y.append(current_y)
        z.append(current_z)

# Camera Sensor
origin.append([0.0, 0.0, 0.35])
d = 20.0

cam_layers = np.linspace(math.radians(-37.0), math.radians(37.0), num=20)
cam_angles = np.linspace(math.radians(-31.0), math.radians(31.0), num=20)

x_temp, y_temp, z_temp = [], [], []
for i in range(len(cam_layers)):
    x_temp.append(origin[2][0] + d*math.cos(cam_layers[i]))
    y_temp.append(0.0)
    z_temp.append(origin[2][2])

for k in range(len(cam_layers)):
    for i in range(len(cam_angles)):
        for j in range(len(x_temp)):
            current_cos = math.cos(cam_angles[i])
            current_sin = math.sin(cam_angles[i])
            current_x = current_cos*x_temp[j] - current_sin*y_temp[j]
            current_y = current_sin*x_temp[j] + current_cos*y_temp[j]
            current_z = z_temp[j] + d*math.sin(cam_layers[k]) if z_temp[j] + d*math.sin(cam_layers[k]) >= 0 else 0.0

            x.append(current_x)
            y.append(current_y)
            z.append(current_z)

# Export data
velodyne_data = (x, y, z, "yellow")
hokuyo_data = (x, y, z, "green")
camera_data = (x, y, z, "blue")

export_data('sensor_data.json', velodyne_data, hokuyo_data, camera_data)