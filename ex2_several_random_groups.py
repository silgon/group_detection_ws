import f_formations as ff
from group_solver import solve
import numpy as np
from copy import copy

n_simulations = 6
options = [ff.Cshape, ff.visAvis, ff.sideBySide, ff.Vshape]
centers = [(-1.6, -1.6, 0), (1.6, -1.6, np.pi/2),
           (1.6, 1.6, np.pi/6), (-1.6, 1.6, 0), (0., 0.,  0.)]
n_groups = np.random.randint(1, 4)

for id_sim in xrange(n_simulations):
    # random selection
    g = []
    for _ in xrange(n_groups):
        cn = copy(centers) # copy of centers
        f = options[np.random.randint(len(options))]
        c = cn.pop(np.random.randint(len(centers)))
        g.append(f(center=c))
    gs=[item for sublist in g for item in sublist]
    results = solve(gs, plot=True)
    print("------------------")
    print("For simulation {}:".format(id_sim))
    print("Centers: {}".format(results[1]))
    print("Group Members: {}".format(results[0]))

import seaborn as sns
plt = sns.plt
plt.show()
