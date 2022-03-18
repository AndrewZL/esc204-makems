from stl import mesh

import numpy as np

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.tri as mtri
from matplotlib.ticker import MultipleLocator

def surface_to_stl(x, y, z, out_file='bottle.stl'):
    """
    Generates stl 3D model from surface plot.
    Args:
        x (array), y (array), z (array): Surface plot arrays. 
        out_file (str, optional): Output filename path. Defaults to 'bottle.stl'.
    """
    tri=mtri.triangulation(x,y,z)
    base = np.zeros(len(tri.triangles), dtype=mesh.Mesh.dtype)
    mesh = mesh.Mesh(base, remove_empty_areas=False)
    mesh.x[:] = x[tri.triangles]
    mesh.y[:] = y[tri.triangles]
    mesh.z[:] = z[tri.triangles]
    mesh.save(out_file)

def surface_revolution_plot(r, length, rate):
    """
    Plots a 3D model of a surface of revolution given a discrete radial array.
    Note: radius = (distance of sensor from central axis) - (depth measurements)
    Args:
        radius (float array): Measurements of the surface radius 
        length (float): Length along the measurement axis
        rate (float): Rate of data collection along measurement axis
    """
    # initialize figure
    fig = plt.figure()
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.set_box_aspect((height, np.ptp(r), np.ptp(r))) 
    # determine parameters
    dim = len(r)    
    height = length/rate
    # create mesh
    u = [np.linspace(0, height, dim)]
    v = np.linspace(0, 2*np.pi, dim)
    U, V = np.meshgrid(u, v)
    # create surface of revolution mapping
    X = U
    Y = r*np.cos(V)
    Z = r*np.sin(V)
    # plot
    ax.plot_surface(X, Y, Z, alpha=1, color='gray', rstride=1, cstride=1)
    plt.show()

