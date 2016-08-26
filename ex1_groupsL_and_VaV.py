import f_formations as ff
from group_solver import solve

g1 = ff.Lshape()
g2 = ff.visAvis(center=(2., 2., 0))
gs = g1 + g2

results = solve(gs, plot=True)
print(results)

import seaborn as sns
plt = sns.plt
plt.show()
