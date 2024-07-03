import math
"""Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9."""
print('Slope question 1')
m = 2 # slope m
b = -2 # Y-intercept b
x_intercept = -b / m
print(f"Slope (m): {m}")
print(f"Y-intercept (b): {b}")
print(f"X-intercept: {x_intercept}")

print('Question 2')
x1=2
x2=6
y1=2
y2=10
slope = (y2-y1) / (x2-x1)
euclidian = math.sqrt(((x2 - x1)**2) + ((y2 -y1)**2))
print(f'The slope for point (2, 2) and point (6,10) is {slope}.')
print(f'THe Euclidian distance for point (2, 2) and point (6,10) is {euclidian}.')