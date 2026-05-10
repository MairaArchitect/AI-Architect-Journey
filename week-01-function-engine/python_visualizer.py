import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles

# This is your position . Can change this to any function you want.
def f(x):
    return x**2 - 2*x**2 + x
# Measure change at point x , h=0.0001 is a tiny step enough for accuracy.
def derivative(f, x, h=0.0001):
    return (f(x+h) - f(x)) / h
# 1000 evenly spaced dots from -2 to 3. Like a very fine ruler.
x_values = np.linspace (-2, 3, 1000)
# position at every dot
y_values = f(x_values)
# For every x in my ruler calculate the derivative.Store all answers in a list.
# In other words speed at every dot
dy_values = [derivative(f,x) for x in x_values]
plt.figure(figsize=(10,6))
# plt.plot = Draw a line through these points. Like connecting dots in a coloring book.
plt.plot(x_values, y_values, label ='f(x)= x**2 - 2*x**2 + x ', color ='blue')
plt.plot(x_values, dy_values,label = "f'(x) approx", color ='red', linestyle ='--')
plt.axhline(y=0, color ='black',linestyle='-',linewidth=0.5)
plt.axvline(x=0, color ='black',linestyle='-',linewidth=0.5)
#  label = The name tag on the  line . so you know which line is the function and which is the derivative.
plt.xlabel('x')
plt.ylabel('y')
plt.title('Function and Its Derivative')
plt.legend()
plt.grid(True)
# plt.show = Open the window and show me the picture now.
plt.show()
critical_points = []
for i in range(len(dy_values) - 1):
    if dy_values[i]* dy_values [i+1] < 0:
       critical_points.append(x_values[i])
print("Approximate critical points (where derivative = 0):")
for cp in critical_points:
    print(f"x={cp:.4f}, f(x) = {f(cp): .4f}")
# Note:
# Where red crosses black (y=0) = critical points.
#If derivative changes from positive to negative (or reverse), it crossed zero.
# This finds peaks and valleys without you guessing.


