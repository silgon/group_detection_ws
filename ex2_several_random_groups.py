import f_formations as ff
from group_solver import solve
import numpy as np
from copy import copy

n_simulations = 6
options = [ff.Cshape, ff.visAvis, ff.sideBySide, ff.Vshape]
centers = [(-1.6, -1.6, 0), (1.6, -1.6, np.pi/2),
           (1.6, 1.6, np.pi/6), (-1.6, 1.6, 0), (0., 0.,  0.)]

np.random.seed(5)
for id_sim in xrange(n_simulations):
    # random selection
    g = []
    cn = copy(centers) # copy of centers
    n_groups = np.random.randint(1, 4)
    sc = []
    for _ in xrange(n_groups):
        f = options[np.random.randint(len(options))]
        c = cn.pop(np.random.randint(len(cn)))
        sc.append(c)
        g.append(f(center=c))
    gids = []
    pid = 0
    for ig in g:
        gid = []
        for _ in ig:
          gid.append(pid)
          pid += 1
        gids.append(gid)
    gs=[item for sublist in g for item in sublist]
    results = solve(gs, plot=True)
    print("------------------")
    print("Simulation {}:".format(id_sim+1))
    print("Baseline")
    print("Centers: {}".format(sc))
    print("Group Members: {}".format(gids))
    print("Deduced")
    print("Centers: {}".format(results[1]))
    print("Group Members: {}".format(results[0]))

import seaborn as sns
plt = sns.plt
plt.show()
