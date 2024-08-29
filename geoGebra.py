import numpy as np
import math
import requests

# Define the GeoGebra HTTP API URL
GEOGEBRA_URL = "http://localhost:5000/api"

# Function to add points to GeoGebra
def add_point_to_geogebra(x, y, z, name):
    command = f"Point({x}, {y}, {z})"
    requests.post(f"{GEOGEBRA_URL}/commands", json={"commands": [f"{name} = {command}"]})

# Function to add lines between two points in GeoGebra
def add_line_to_geogebra(x1, y1, z1, x2, y2, z2, name):
    command = f"Line((Point({x1}, {y1}, {z1})), (Point({x2}, {y2}, {z2})))"
    requests.post(f"{GEOGEBRA_URL}/commands", json={"commands": [f"{name} = {command}"]})

# Define origins
origin = [[0.0, 0.0, 1.83], [0.0, 0.0, 0.12], [0.0, 0.0, 0.35]]

# Distance parameters
d_velodyne = 100.0
d_hokuyo = 5.0
d_camera = 20.0

# Sensor angles
vel_layers = np.linspace(-15.0, 15.0, num=16)
vel_angles = np.linspace(0.0, 2 * math.pi, 100)
hok_angles = np.linspace(-4.7128898/2, 4.7128898/2, 50)
cam_layers = np.linspace(math.radians(-37.0), math.radians(37.0), 20)
cam_angles = np.linspace(math.radians(-31.0), math.radians(31.0), 20)

# Velodyne Points
for layer in vel_layers:
    x_temp = origin[0][0] + d_velodyne * math.cos(math.radians(layer))
    y_temp = 0.0
    z_temp = origin[0][2] + d_velodyne * math.sin(math.radians(layer))
    
    for angle in vel_angles:
        x = x_temp * math.cos(angle)
        y = x_temp * math.sin(angle)
        z = max(z_temp, 0.0)
        point_name = f"Velodyne{layer}_{angle}"
        add_point_to_geogebra(x, y, z, point_name)
        # Add line from origin to point
        add_line_to_geogebra(origin[0][0], origin[0][1], origin[0][2], x, y, z, f"Line_{point_name}")

# Hokuyo Points
for layer in hok_angles:
    x_temp = origin[1][0] + d_hokuyo * math.cos(0.0)
    y_temp = 0.0
    z_temp = origin[1][2]
    
    x = x_temp * math.cos(layer)
    y = x_temp * math.sin(layer)
    z = max(z_temp, 0.0)
    point_name = f"Hokuyo_{layer}"
    add_point_to_geogebra(x, y, z, point_name)
    # Add line from origin to point
    add_line_to_geogebra(origin[1][0], origin[1][1], origin[1][2], x, y, z, f"Line_{point_name}")

# Camera Points
for k, layer in enumerate(cam_layers):
    x_temp = origin[2][0] + d_camera * math.cos(layer)
    y_temp = 0.0
    z_temp = origin[2][2]
    
    for angle in cam_angles:
        x = x_temp * math.cos(angle)
        y = x_temp * math.sin(angle)
        z = z_temp + d_camera * math.sin(layer)
        point_name = f"Camera{k}_{angle}"
        add_point_to_geogebra(x, y, max(z, 0.0), point_name)
        # Add line from origin to point
        add_line_to_geogebra(origin[2][0], origin[2][1], origin[2][2], x, y, max(z, 0.0), f"Line_{point_name}")
