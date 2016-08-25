#! /usr/bin/python
import numpy as np
import seaborn as sns
plt = sns.plt

#sns.set_context("paper")
#sns.set_style("white")

import f_formations as ff
np.random.seed(0)

poses = []
radius = .6
sigma = 0.2, 0.2, 0.1

# ff.Lshape(poses, (3,3, 0), radius, sigma)
# ff.visAvis(poses, (-3,-3, np.pi/4), radius, sigma)
# ff.circleFormation(3, poses, (2,-3, np.pi/4), radius, sigma)

# ff.Lshape(poses, (-1.3, 1, 0), radius, sigma)
# # ff.visAvis(poses, (-3,-3, np.pi/4), radius, sigma)
# ff.circleFormation(3, poses, (2,0, np.pi/4), radius, sigma)

ff.circleFormation(3, poses, (2,0, np.pi/4), radius, sigma)
ff.Lshape(poses, (-0.5, .4, 2), radius, sigma)


poses = np.array(poses)

from matplotlib.patches import Circle, Ellipse
f, ax = plt.subplots()

ax.axis("equal")
for pose in poses:
    ax.add_artist(Ellipse((pose[0], pose[1]), width=0.3, height=0.6,
                               angle=pose[2]*180/np.pi, color='g', fill=False, lw=1.5,
                               aa=True, zorder=3))
    ax.add_artist(Circle((pose[0]+np.cos(pose[2])*.05, pose[1]+np.sin(pose[2])*.05),
                         radius=0.12, color='g', ec='g', lw=2.5, aa=True, zorder=3))


sig_x = .6
sig_y = .6

# cost function
def costf(X, Y, poses):
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


mins, maxs = np.min(poses, 0), np.max(poses, 0)
offset = 3
X, Y = np.meshgrid(np.arange(mins[0]-offset,maxs[0]+offset,0.1),
                   np.arange(mins[1]-offset,maxs[1]+offset,0.1));
cost = costf(X, Y, poses)
# plt.pcolormesh(X, Y, cost, cmap="viridis")
plt.contour(X, Y, cost, cmap="viridis")
plt.colorbar()
from scipy.ndimage.filters import maximum_filter
neighborhood = np.ones((10,10))
local_max = maximum_filter(cost, footprint=neighborhood)==cost
data_xy=np.where(local_max) # get position of the maximas
groups_center = np.array(zip(X[data_xy], Y[data_xy]))
plt.scatter(groups_center[:,0], groups_center[:,1], marker='o')


groups = []
for group_center in groups_center:
    group = []
    for idx, pose in enumerate(poses):
        if(costf(group_center[0], group_center[1], [pose]) > 0.3):
            group.append(idx)
    groups.append(group)

print("Groups: \n{}".format(groups))
print("Centers: \n{}".format(groups_center))

plt.show()
