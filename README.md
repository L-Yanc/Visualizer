# Visualizer Repository
This repository contains Python and JavaScript/HTML code to visualize the fieilds of view of the sensors in the Bottobo Robot. The code simulates the point clouds for all three sensors on the robot in both Python Matplotlib and GeoGebra.

## How to Use
The code should run in any system setup that has Python 3 and the numpy, math, json, matplotlib and mpl_toolkits packages installed. 
*Important note*: the only change needed for the code to run accurately is that sensor_data.json (and geoGebra.py since it creates sensor_data.json) and geoGebra.html need to be in the same directory, as it is in this repository. Otherwise the relevant path in geoGebra.html must be adjusted.

## File Contents
This repository contains 5 files:

1. **visualizer.py**: generates a point cloud output connected to the relevant origins of the sensors by lines in matplotlib. Is quite slow and the number of points is currently not accurate since the number of points was reduced to suit the capabilities of the laptop during testing. Adjust as necessary.

2. **visualizer_lines.py**: this file only generates the point cloud for the Velodyne sensor as lines starting from its relative origin. 

3. **geoGebra.py**: generates the same point cloud and line output as visualizer.py but stores the output into sensor_data.json for use in the html file. 

4. **sensor_data.json**: contains the points as a set of x, y, z and color.

5. **geoGebra.html**: outputs the points in sensor_data.json to a webpage using the GeoGebra API. *This is currently not working* as it needs further work.
