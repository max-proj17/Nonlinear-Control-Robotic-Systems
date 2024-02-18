import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

####################################################################################
## Solves a differential equation using odeint and compares the numerical solution #
## with an exact solution. Features include plotting the solution over time        #
## and analyzing the behavior of a simple ODE model.                               #
####################################################################################

###################
### Question 1
###################

# Define the ODE
def model(x, t):
    return -5*x + np.cos(2*t)

def g(t):
    return 2 * np.exp(-5 * t) + (1 / 25 * np.cos(2 * t)) + 2 * np.exp(-5 * t) * np.sin(2 * t) - ( 1 / 25 * np.exp(-5 * t))
# Initial condition
x0 = [2.0]
t0 = 0.0

# scipy for solving IVP
t1=5.0
n=15 # number of points
t = np.linspace(t0, t1, n) # points where the solutions are solved at
sol = odeint(model, x0, t) # x= sol[:,0]
plt.figure(figsize=(6,3))
plt.ylim(-2, 5)
plt.plot(t, sol[:,0], 'x', label='ODE solver', linewidth =2)
plt.plot(t, g(t), 'k-', label='Exact solution', linewidth =2)
plt.legend( loc='best', scatterpoints=1, fontsize=15, frameon=False, labelspacing=0.5)
plt.ylabel("x", size=15)
plt.xlabel('Time', size=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()

###################
### Question 2
###################

# Define the system of first-order ODEs
def model(x, t):
    x1, x2 = x
    du1dt = x2
    du2dt = 4*x2 - 4*x1
    return [du1dt, du2dt]

def g(t):
    return (2 - 4*t) * np.exp(2*t)

#t0 = 0.0
x0 = [2.0, 0.0]
# scipy for solving IVP
t1=1.0
n=15 # number of points
t = np.linspace(t0, t1, n) # points where the solutions are solved at
sol = odeint(model, x0, t)
plt.figure(figsize=(6,3))
plt.ylim(-2, 5)
plt.plot(t, sol[:,0], 'x', label='ODE solver', linewidth =2)
plt.plot(t, g(t), 'k-', label='Exact solution', linewidth =2)
plt.legend( loc='best', scatterpoints=1, fontsize=15, frameon=False, labelspacing=0.5)
plt.ylabel("x", size=15)
plt.xlabel('Time', size=15)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.show()