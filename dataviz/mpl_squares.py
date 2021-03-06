import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# plt.plot(input_values, squares, linewidth=5)


plt.scatter(2, 4, s=100)

# Set chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)


plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
