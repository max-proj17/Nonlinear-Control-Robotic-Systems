import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

###################################################################################
## Generates phase portraits for both linear and nonlinear systems and plots      #
## trajectories for the nonlinear system from different initial conditions.       #
## This script utilizes vector fields and solve_ivp to visualize system dynamics. #
###################################################################################

# B2 plot the phase portrait for the linear system.
def vector_field_linear(X, Y):
    return -X, -Y

x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
u, v = vector_field_linear(x, y)


# C1 plot the phase portrait for the nonlinear system.
def vector_field_nonlinear(X, Y):
    return -X + X**2 * Y, -Y


# Define the differential equation for the nonlinear system (example)
def nonlinear_system(t, X):
    x1, x2 = X
    return [-x1 + x1**2 * x2, -x2]


plt.figure(figsize=(15, 5))  # Set the figure size

# B2: Phase portrait for the linear system
plt.subplot(1, 3, 1)  # 1 row, 3 columns, subplot 1
x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
u, v = vector_field_linear(x, y)
plt.quiver(x, y, u, v, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear System Phase Portrait')
plt.grid()

# C1: Phase portrait for the nonlinear system
plt.subplot(1, 3, 2)  # 1 row, 3 columns, subplot 2
x, y = np.meshgrid(np.linspace(-2, 2, 20), np.linspace(-2, 2, 20))
u, v = vector_field_nonlinear(x, y)
plt.quiver(x, y, u, v, color='r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Nonlinear System Phase Portrait')
plt.grid()

# B3 & C2: Trajectories for the nonlinear system with various initial conditions
plt.subplot(1, 3, 3)  # 1 row, 3 columns, subplot 3
initial_conditions = [[0.5, 0], [1, 0.5], [-0.5, -0.5]]
t_span = [0, 10]
t_eval = np.linspace(t_span[0], t_span[1], 100)
for X0 in initial_conditions:
    sol = solve_ivp(nonlinear_system, t_span, X0, t_eval=t_eval)
    plt.plot(sol.y[0], sol.y[1], label=f'IC: {X0}')
    plt.plot(X0[0], X0[1], 'o')  # Mark the initial condition
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Trajectories for Various Initial Conditions')
plt.legend()
plt.grid()

plt.tight_layout()  # Adjust subplots to fit into the figure area.
plt.show()
