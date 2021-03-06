#!/usr/bin/python
"""
This file emulates some kinds of F Formations.
"""
import numpy as np
DEFAULT_CENTER = (0., 0., 0.)
DEFAULT_RADIUS = 0.6
DEFAULT_SIGMA = (0.1, 0.1, 0.1)

def Lshape(center=DEFAULT_CENTER, radius=DEFAULT_RADIUS, sigma=DEFAULT_SIGMA):
    """ create F Formation of the type L
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the
    f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    x, y, theta = center
    r = radius
    poses = []
    # person 1
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta)+sg_x, y+r*np.sin(theta)+sg_y, theta+np.pi+sg_th])
    # person 2
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta+np.pi/2)+sg_x, y+r*np.sin(theta+np.pi/2)+sg_y,
                  theta-np.pi/2+sg_th])
    return poses


def visAvis(center=DEFAULT_CENTER, radius=DEFAULT_RADIUS, sigma=DEFAULT_SIGMA):
    """ create F Formation of the type vis-A-vis
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the
    f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    
    return circleFormation(2, center, radius, sigma)

def Vshape(center=DEFAULT_CENTER, radius=DEFAULT_RADIUS, sigma=DEFAULT_SIGMA):
    """ create F Formation of the type V
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the
    f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    x, y, theta = center
    r = radius
    poses = []
    # person 1
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta)+sg_x, y+r*np.sin(theta)+sg_y, theta+np.pi+sg_th])
    # person 2
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta+3*np.pi/4)+sg_x, y+r*np.sin(theta+3*np.pi/4)+sg_y,
                  theta-np.pi/4+sg_th])
    return poses

def Cshape(center=DEFAULT_CENTER, radius=DEFAULT_RADIUS, sigma=DEFAULT_SIGMA):
    """ create F Formation of the type V
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the
    f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    x, y, theta = center
    r = radius
    poses = []
    # person 1
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta)+sg_x, y+r*np.sin(theta)+sg_y, theta+np.pi+sg_th])
    # person 2
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta+np.pi/4)+sg_x, y+r*np.sin(theta+np.pi/4)+sg_y,
                  theta-3*np.pi/4+sg_th])
    return poses


def circleFormation(n=4, center=DEFAULT_CENTER, radius=DEFAULT_RADIUS, sigma=DEFAULT_SIGMA):
    """ create F Formation of the type Circular with N people
    Arguments:
    - `n`: number of humans you want
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the
    f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    x, y, theta = center
    r = radius
    poses = []
    for i in xrange(n):
        # update random variables at each time
        sg_x, sg_y, sg_th = np.random.randn(3)*sigma
        # append pose
        poses.append([x+r*np.cos(theta+i*2*np.pi/n+sg_x),
                      y+r*np.sin(theta+i*2*np.pi/n+sg_y),
                      theta+np.pi*(1+i*2./n)+sg_th])
    return poses


def sideBySide(center=DEFAULT_CENTER, radius=DEFAULT_RADIUS, sigma=DEFAULT_SIGMA):
    """ create F Formation of the type side-by-side
    In this case, the people are not looking to the center of
    the O-space (since they suppose to be walking)
    Arguments:
    - `poses`: the pose where the new humans will be created
    - `center`: list parameter (x,y,theta)
    - `radius`: float parameter distance from the center of the
    f_formation to the human
    - `sigma`: for the error in positions diag(sigma_x,sigma_y,sigma_theta)
    """
    x, y, theta = center
    r = radius
    poses = []
    # person 1
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta)+r*.6*np.cos(np.pi/2+theta)+sg_x,
                  y+r*np.sin(theta)+r*.6*np.sin(np.pi/2+theta)+sg_y,
                  # theta+np.pi+np.pi/9+sg_th])  # with a litte twist
                  theta+np.pi+sg_th])
    # person 2
    sg_x, sg_y, sg_th = np.random.randn(3)*sigma
    poses.append([x+r*np.cos(theta)-r*.6*np.cos(np.pi/2+theta)+sg_x,
                  y+r*np.sin(theta)-r*.6*np.sin(np.pi/2+theta)+sg_y,
                  # theta+np.pi-np.pi/9+sg_th])  # with a little twist
                  theta+np.pi+sg_th])
    return poses
