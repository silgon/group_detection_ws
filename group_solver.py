#! /usr/bin/python
import numpy as np
from scipy.ndimage.filters import maximum_filter

import seaborn as sns
plt = sns.plt
from matplotlib.patches import Circle, Ellipse


def solve(poses, sigma=(.6,.6), plot=True, plot_offset=3., resolution=0.1,
          local_footprint=1., radius=0.6):
    poses = np.array(poses)
    mins, maxs = np.min(poses, 0), np.max(poses, 0)
    offset = plot_offset
    X, Y = np.meshgrid(np.arange(mins[0]-offset, maxs[0]+offset, resolution),
                       np.arange(mins[1]-offset, maxs[1]+offset, resolution));

    cost = costf(X, Y, poses, radius, sigma)
    fp = local_footprint/resolution
    neighborhood = np.ones((fp,fp))
    local_max = maximum_filter(cost, footprint=neighborhood)==cost
    data_xy=np.where(local_max) # get position of the maximas
    groups_center = np.array(zip(X[data_xy], Y[data_xy]))
    groups = []
    for group_center in groups_center:
        group = []
        for idx, pose in enumerate(poses):
            if(costf(group_center[0], group_center[1], [pose], radius, sigma) > 0.3):
                group.append(idx)
        groups.append(group)

    if plot:
        f, ax = plt.subplots()        
        ax.axis("equal")
        plotPeople(poses, ax)
        # plt.pcolormesh(X, Y, cost, cmap="viridis")
        plt.contour(X, Y, cost, cmap="viridis")
        plt.colorbar()
        plt.scatter(groups_center[:,0], groups_center[:,1], marker='o')
        plt.show()
    return groups, groups_center



def plotPeople(poses, ax):
    for pose in poses:
        ax.add_artist(Ellipse((pose[0], pose[1]), width=0.3, height=0.6,
                                   angle=pose[2]*180/np.pi, color='g', fill=False, lw=1.5,
                                   aa=True, zorder=3))
        ax.add_artist(Circle((pose[0]+np.cos(pose[2])*.05, pose[1]+np.sin(pose[2])*.05),
                             radius=0.12, color='g', ec='g', lw=2.5, aa=True, zorder=3))



# cost function
def costf(X, Y, poses, radius, sigma):
    sig_x, sig_y = sigma
    if type(X) is np.ndarray:
        cost = np.zeros(X.shape)
    else:
        cost = 0
    for pose in poses:
        x, y, theta = pose
        x_mu, y_mu = x+radius*np.cos(theta), y+radius*np.sin(theta)
        a = np.cos(theta)**2/(2*sig_x**2) + np.sin(theta)**2/(2*sig_y**2)
        b = -np.sin(2*theta)/(4*sig_x**2) + np.sin(2*theta)/(4*sig_y**2)
        c = np.sin(theta)**2/(2*sig_x**2) + np.cos(theta)**2/(2*sig_y**2)
        cost += np.exp(-(a*(X-x_mu)**2 - 2*b*(X-x_mu)*(Y-y_mu) + c*(Y-y_mu)**2))
    return cost
