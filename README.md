# dash-vtk

The file we are using for dash-vtk is in a legacy format that was difficult to import using VTK, thus we imported the file using PyVista instead. 

There are some differences between the original data and the data after importing.
    - origin, spacing, and dimensions
However, Pyvista manages to plot the data correctly despite this.

We have having trouble rendering the data using dask-vtk, using the dash_vtk.VolumeDataRepresentation() we are getting an error when passing in the point arrays.