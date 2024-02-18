import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

##########################################################################################
## Compares the solutions of a nonlinear and a linearized system using odeint.           #
## It illustrates the difference in dynamics through time series plots of system states. #
##########################################################################################


# Nonlinear system
def nonlinear_system(x, t):
    x1, x2 = x
    u = np.cos(t)
    dx1dt = np.sin(x2)
    dx2dt = -x1**2 + u
    return [dx1dt, dx2dt]

# Linear system (linearized at the base point [0, 0])
def linear_system(x, t):
    x1, x2 = x
    u = np.cos(t)
    dx1dt = x2  # Linearization of sin(x2) at x2 = 0
    dx2dt = -2 * x1 + u  # Linearization of -x1^2 at x1 = 0
    return [dx1dt, dx2dt]

# Initial conditions
x0 = [2, 0]

# Time points
t = np.linspace(0, 5, 100)

# Solve ODEs
sol_nonlinear = odeint(nonlinear_system, x0, t)
sol_linear = odeint(linear_system, x0, t)
print(sol_nonlinear)
print(sol_linear)

# Plotting
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, sol_nonlinear[:, 0], label='Nonlinear x1')
plt.plot(t, sol_nonlinear[:, 1], label='Nonlinear x2')
plt.title('Nonlinear System')
plt.xlabel('Time')
plt.ylabel('x')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, sol_linear[:, 0], label='Linear x1')
plt.plot(t, sol_linear[:, 1], label='Linear x2')
plt.title('Linear System')
plt.xlabel('Time')
plt.ylabel('x')
plt.legend()

plt.tight_layout()
plt.show()
