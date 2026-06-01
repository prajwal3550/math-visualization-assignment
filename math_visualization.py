import numpy as np
import matplotlib.pyplot as plt

# Task 1 - Mathematical Function Visualization
x = np.linspace(-10, 10, 500)

y1 = x
y2 = x**2
y3 = np.sin(x)
y4 = np.exp(-0.1 * x) * np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='y = x', linestyle='-')
plt.plot(x, y2, label='y = x²', linestyle='--')
plt.plot(x, y3, label='y = sin(x)', linestyle=':')
plt.plot(x, y4, label='y = e^(-0.1x)cos(x)', marker='.', markevery=20)

plt.title("Mathematical Function Visualization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)

plt.savefig("function_plot.png")
plt.close()

# Task 2 - Own Equation

# Mixed equation combining cubic, trigonometric, and exponential terms
y_own = 0.03 * x**3 - 0.4 * x**2 + np.sin(x) + 2 * np.exp(-0.05 * x)

plt.figure(figsize=(10, 6))
plt.plot(x, y_own, color='purple')

plt.title("My Custom Equation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.savefig("own_equation.png")
plt.close()

# Task 3 - Student Score Visualization
students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

midterm = np.array([85, 72, 90, 66, 78,
                    92, 60, 74, 88, 95])

final = np.array([80, 70, 94, 68, 75,
                  90, 65, 72, 84, 96])

total = 0.4 * midterm + 0.6 * final

#Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(midterm, final, color='blue')
plt.title("Midterm vs Final Scores")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.grid(True)

plt.savefig("score_scatter.png")
plt.close()

#Histogram
plt.figure(figsize=(8, 6))
plt.hist(total, bins=5, color='green', edgecolor='black')
plt.title("Distribution of Total Scores")
plt.xlabel("Total Score")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("score_histogram.png")
plt.close()

#Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(students, total, color='orange')

plt.title("Student Total Scores")
plt.xlabel("Students")
plt.ylabel("Total Score")
plt.grid(axis='y')

plt.savefig("score_bar_chart.png")
plt.close()

# Task 4 - Best-Fit Line / Prediction
slope, intercept = np.polyfit(midterm, final, 1)

x_fit = np.linspace(min(midterm), max(midterm), 100)
y_fit = slope * x_fit + intercept

plt.figure(figsize=(8, 6))
plt.scatter(midterm, final, color='blue', label='Actual Data')
plt.plot(x_fit, y_fit, color='red', linewidth=2,
         label='Best-Fit Line')

plt.title("Final Score Prediction from Midterm Score")
plt.xlabel("Midterm Score")
plt.ylabel("Final Score")
plt.legend()
plt.grid(True)

plt.savefig("score_prediction.png")
plt.close()

# Prediction Examples
for score in [50, 75, 100]:
    predicted = slope * score + intercept
    print(f"Predicted final score for midterm {score}: "
          f"{predicted:.2f}")
