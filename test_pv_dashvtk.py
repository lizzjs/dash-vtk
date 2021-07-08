import os
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import numpy as np

import floris.tools as wfct
import pyvista as pv
import dash_vtk

cwd = os.getcwd()

#Calculated dimensions, origin and spacing based on floris flow data
floris_input_json = os.path.join(cwd, "data", "example_input.json")
fi = wfct.floris_interface.FlorisInterface(floris_input_json)
fd = fi.get_flow_data()

origin = [axis.mean().round().astype(int) for axis in [fd.x, fd.y, fd.z]]
ranges = np.array([axis.ptp().round().astype(int) for axis in [fd.x, fd.y, fd.z]])
dimensions = np.array([np.unique(axis).shape[0] for axis in [fd.x, fd.y, fd.z]])
x, y, z = dimensions
spacing = np.round(ranges / dimensions).astype(int)


# PyVista
flow_filename = os.path.join(cwd, "data", "visualize_curl.vtk")
mesh = pv.read(flow_filename)
origin_pv = mesh.origin
dimensions_pv = mesh.dimensions
spacing_pv = mesh.spacing

#Floris calculated vs PyVista
# print(dir(mesh))
print("floris:", origin, "| pyvista:", origin_pv)
print("floris:", dimensions, "| pyvista:", dimensions_pv)
print("floris:", spacing, "| pyvista:", spacing_pv)
print("pyvista scalars: \n", mesh.point_arrays['UAvg'])

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

vtk_view = dash_vtk.View(
    id="vtk-view",
    children=[
        dash_vtk.VolumeDataRepresentation(
            spacing=spacing_pv,
            dimensions=dimensions_pv,
            origin=origin_pv,
            scalars=mesh.point_arrays['UAvg'], #error here
            rescaleColorMap=False,
        ),
    ]   
)

app.layout = html.Div(
    style={"height": "calc(100vh - 16px)"},
    children=[
        html.Div(children=vtk_view, style={"height": "100%", "width": "100%"})
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)