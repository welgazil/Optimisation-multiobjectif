library("mco")

# read examplary Pareto front
# (both objectives are to be minimized!!)
pf = as.matrix(read.table("exp_2d_pareto_front.txt", dec="."))

# convert to doubles
pf = pf + 0.0

# read Pareto front approximation found by my favorite algorithm
my_algo <- as.matrix(read.table("test.txt"))
# instead, I just sample the Pareto front
#my_algo = pf[sample(nrow(pf), 100), ]

# plot them
plot(pf)
points(my_algo, col='red')

# reference point
refpoint <- c(max(pf[,1], my_algo[,1]), max(pf[,2], my_algo[,2]))
refpoint <- 1.1 * refpoint

# (inverted) generational distance (lower is better)
a
# [1] 0.000449582

# epsilon indicator (lower is better)
epsilonIndicator(my_algo, pf)
# [1] 2546

# hypervolume (higher is better)
dominatedHypervolume(pf, refpoint)
# [1] 50593041045
dominatedHypervolume(my_algo, refpoint)
# [1] 50421211203

# relative hypervolume difference (lower is better)
(dominatedHypervolume(pf, refpoint) - dominatedHypervolume(my_algo, refpoint)) / dominatedHypervolume(pf, refpoint)
# [1] 0.003396314
