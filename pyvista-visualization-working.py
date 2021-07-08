
import os
import pyvista as pv

# PyVista
cwd = os.getcwd()
turbine_filename = os.path.join(cwd, "test_data", "visualize_curl.vtk")
mesh = pv.read(turbine_filename)
origin_pv = mesh.origin
dimensions_pv = mesh.dimensions
spacing_pv = mesh.spacing

mesh.plot(cmap='cool') 