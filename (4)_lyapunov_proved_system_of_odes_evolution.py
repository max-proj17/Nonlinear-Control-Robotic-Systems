from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

##############################################################################################
# Solves a system of ODEs representing the dynamics of three interconnected variables.       #
# It plots the evolution of these variables over time, highlighting their interdependencies. #
# Determined stability by hand via Lyapunov function candidate.                              #
##############################################################################################

# Constants
k = 2

# Define the system of ODEs
def system_of_odes(t, x):
    x1, x2, x3 = x
    dx1dt = -k * x1
    dx2dt = -x3**2 - x2
    dx3dt = x3 * x2
    return [dx1dt, dx2dt, dx3dt]

# Initial conditions
x0 = [1, 1, 1]  # Initial conditions for x1, x2, x3

# Time span
t_span = (0, 10)
t_eval = np.linspace(*t_span, 300)

# Solve the system of ODEs
solution = solve_ivp(system_of_odes, t_span, x0, t_eval=t_eval)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label='$x_1(t)$')
plt.plot(solution.t, solution.y[1], label='$x_2(t)$')
plt.plot(solution.t, solution.y[2], label='$x_3(t)$')
plt.title('System Evolution Over Time')
plt.xlabel('Time')
plt.ylabel('State Variables')
plt.legend()
plt.grid(True)
plt.show()
