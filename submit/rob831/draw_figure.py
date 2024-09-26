import matplotlib.pyplot as plt
import numpy as np

iterations = np.arange(1, 11)  # Iteration numbers from 1 to 10
# Dagger
# Ant-v2
# --eval_batch_size 2000 --num_agent_train_steps_per_iter 1500
eval_avg = [3509.39, 4614.27, 4613.77, 4774.76, 4511.81, 4642.19, 4678.36, 4859.95,4635.03, 4792.39]
std_avg = [99.80, 31.36, 32.50, 96.92, 5.75, 44.97, 48.81, 2.75, 24.70, 93.47]

# Expert data
expert_avg = 4713.65
expert_std = 12.20

# Plot with both eval and expert
plt.figure(figsize=(8, 6))

# Plot for evaluation data
plt.errorbar(iterations, eval_avg, yerr=std_avg, fmt='-o', capsize=5, capthick=2, label='Ant-v2 BC Agent')

# Plot for expert data (horizontal line)
plt.hlines(expert_avg, xmin=1, xmax=10, colors='r', linestyles='--', label=f'Ant-v2 Expert')
plt.fill_between(iterations, expert_avg - expert_std, expert_avg + expert_std, color='r', alpha=0.2)

# Titles and labels
plt.title('BC Agent and Expert Performance on Ant-v2 Task')
plt.xlabel('Iteration Number')
plt.ylabel('Average Performance')
plt.xticks(iterations)
plt.grid(True)
plt.legend(loc='lower right')

# Save the plot
plt.savefig("./dagger_ant_eval.png")


# Hopper-v2
# --eval_batch_size 2000 --num_agent_train_steps_per_iter 1500
eval_avg = [817.69, 1917.60, 3483.79, 2170.29, 3752.76, 3747.64, 3742.26, 3770.88, 3779.56, 3776.64]
std_avg = [349.63, 634.25, 57.58, 527.61, 6.06, 6.13, 39.34, 2.94, 2.93, 3.85]

# Expert data
expert_avg = 10344.52
expert_std = 20.98

# Plot with both eval and expert
plt.figure(figsize=(8, 6))

# Plot for evaluation data
plt.errorbar(iterations, eval_avg, yerr=std_avg, fmt='-o', capsize=5, capthick=2, label='Hopper-v2 BC Agent')

# Plot for expert data (horizontal line)
plt.hlines(expert_avg, xmin=1, xmax=10, colors='r', linestyles='--', label=f'Hopper-v2 Expert')
plt.fill_between(iterations, expert_avg - expert_std, expert_avg + expert_std, color='r', alpha=0.2)

# Titles and labels
plt.title('BC Agent and Expert Performance on Hopper-v2 Task')
plt.xlabel('Iteration Number')
plt.ylabel('Average Performance')
plt.xticks(iterations)
plt.grid(True)
plt.legend(loc='lower right')

# Save the plot
plt.savefig("./dagger_hopper_eval.png")



# BC parameter curve on Ant-v2
# --eval_batch_size 2000 --num_agent_train_steps_per_iter 1500
eval_avg = [635.41, 932.30, 1355.76, 2215.09, 3030.75, 3077.04, 3888.95, 4162.28, 4335.61, 3964.71]
std_avg = [382.38, 369.20, 788.86, 1025.52, 406.50, 1179.32, 281.84, 62.91, 111.89, 574.46]
num_agent_train_steps_per_iter = [500, 700, 900, 1100, 1300, 1500, 1700, 1900, 2100, 2300]

# Plot with both eval and expert
plt.figure(figsize=(8, 6))

# Plot for evaluation data
plt.errorbar(num_agent_train_steps_per_iter, eval_avg, yerr=std_avg, fmt='-o', capsize=5, capthick=2, label='Ant-v2')

# Titles and labels
plt.title('BC Agent Performance with Different Params on Ant-v2')
plt.xlabel('Num Agent Train Steps Per Iter')
plt.ylabel('Average Performance')
plt.xticks(num_agent_train_steps_per_iter)
plt.grid(True)
plt.legend(loc='lower right')

# Save the plot
plt.savefig("./param-ant-v2.png")