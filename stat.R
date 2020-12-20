# read solution quality (to be minimized) from 30 runs of algo1 on instance1
data_instance1_algo1 = scan(file = "instance1_algo1_min.30")

# descriptive statistics
mean(data_instance1_algo1)
median(data_instance1_algo1)
min(data_instance1_algo1)
max(data_instance1_algo1)


# read solution quality (to be minimized) from 30 runs of algo2 on instance1
data_instance1_algo2 = scan(file = "instance1_algo2_min.30")

# descriptive statistics
mean(data_instance1_algo2)
median(data_instance1_algo2)
min(data_instance1_algo2)
max(data_instance1_algo2)

# plot solution quality for both algorithms
boxplot(data_instance1_algo1, data_instance1_algo2, ylab = "solution quality (lower is better)", names = c("algo 1", "algo 2"))

# Wilcoxon signed-rank test for paired samples, alpha = 0.01
wilcox.test(data_instance1_algo1, data_instance1_algo2, paired = TRUE, conf.level = 0.99)
