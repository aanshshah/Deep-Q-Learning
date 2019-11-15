import matplotlib.pyplot as plt
lines = open("mean_q_test_score.csv").readlines()
rewards = []
q_values = []
for line in lines:
	reward, q_value = line.strip().split()
	rewards.append(reward)
	q_values.append(q_value)
plt.scatter(rewards, q_values)
plt.xlabel("Test Episode Score")
plt.ylabel("Mean Q Values Across All Test Episodes")
plt.show()

