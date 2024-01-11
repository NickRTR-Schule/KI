import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y, group):
        self.x = x
        self.y = y
        self.distance = 0
        self.group = group

def plot_points(title):
    plt.title(title)
    plt.scatter([i.x for i in group1], [i.y for i in group1], color="blue")
    plt.scatter([i.x for i in group2], [i.y for i in group2], color="red")
    plt.scatter(point.x, point.y, color="green")
    plt.show()

def calculate_distance(p1, p2):
    return np.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

# Variables
group1 = [Point(np.random.randint(0, 10), np.random.randint(0, 10), 1) for i in range(10)]
group2 = [Point(np.random.randint(0, 10), np.random.randint(0, 10), 2) for i in range(10)]
point = Point(np.random.randint(0, 10), np.random.randint(0, 10), 0)
k = 3

# Calculate distances for all points in both groups
for group in (group1, group2):
    for p in group:
        p.distance = calculate_distance(point, p)

neighbors = group1 + group2
neighbors.sort(key=lambda p: p.distance)

# Count the number of neighbors from each group
group1_count = sum(1 for neighbor in neighbors[:k] if neighbor.group == 1)
group2_count = sum(1 for neighbor in neighbors[:k] if neighbor.group == 2)

# Determine which group the point belongs to
group = "blue" if group1_count > group2_count else "red"

plot_points(f"(K={k}) - Green Point belongs to group {group}")