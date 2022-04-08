import numpy as np

import matplotlib.pyplot as plt
from matplotlib import cm, colors
import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.tri as mtri
from matplotlib.ticker import MultipleLocator


def label_cmap_gen(x1, x2, height, label_color):
    """
    Generates a colormap for the surface of revolution plot.
    Args:
        x1 (float): photoresistor position at the bottom of the label
        x2 (float): photoresistor position at the top of the label
        height (float): Length along the measurement axis
        label_color (str): Color of the label
    """
    # colours of discrete cmap
    col = ['white', label_color, 'white']
    # generate discrete cmap
    cmap = colors.ListedColormap(col)
    # bounds for discrete normalization
    bounds = [0, x1, x2, height]
    # normalize cmap
    norm = colors.BoundaryNorm(bounds, 3)
    return cmap, norm


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


def surface_revolution_plot(r, x1, x2, label_color='red', length=16, rate=2):
    """
    Plots a 3D model of a surface of revolution given a discrete radial array.
    Note: radius = (distance of sensor from central axis) - (depth measurements)
    Args:
        r (float array): Measurements of the surface radius 
        x1 (float): photoresistor position at the bottom of the label
        x2 (float): photoresistor position at the top of the label 
        length (float): Length along the measurement axis
        rate (float): Rate of data collection along measurement axis
    """
    # determine parameters
    dim = len(r)    
    height = length/rate
    
    # initialize figure
    fig = plt.figure()
    plt.rcParams["figure.figsize"] = [7.00, 3.5]
    plt.rcParams["xtick.labelsize"] = 7
    plt.style.use('dark_background')
    plt.rcParams["savefig.facecolor"] = "#0E1117"
    plt.rcParams["axes.facecolor"] = "#0E1117"

    ax = fig.add_subplot(1, 1, 1, projection='3d')

    ax.set_box_aspect((np.ptp(r), np.ptp(r), height)) 

    # create mesh
    u = [np.linspace(0, height, dim)]
    v = np.linspace(0, 2*np.pi, dim)
    U, V = np.meshgrid(u, v)
    # create surface of revolution mapping
    X = U
    Y = r*np.cos(V)
    Z = r*np.sin(V)
    
    # generate label cmap
    cmap, norm = label_cmap_gen(x1, x2, height, label_color)

    # plot using facecolors for correct axis, use discrete normalization function
    ax.plot_surface(X, Y, Z, alpha=1, facecolors=cmap(norm(X)), rstride=1, cstride=1)
    ax.view_init(20,45,'x')
    plt.show()
    return fig


if __name__ == '__main__':
    r = [2.8,2.9,3,3,3,3,3,3,3,3,3,3,3,3,3,2.9,2.8,2.7,2.6,2.7,2.8,2.9,3,3,3,3,3,3,3,3,2.6,2.4,2,1.6,1.2,1,1]
    x1 = 5
    x2 = 6.2
    length = 16
    rate = 2
    surface_revolution_plot(r, x1, x2, length=length, rate=rate)