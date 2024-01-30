import numpy as np
import matplotlib.pyplot as plt

# Set up initial conditions
m = 0.05 # mass of projectile (kg)
g = 9.81 # acceleration due to gravity (m/s^2)
k = 0.1 # air resistance coefficient (kg/m)
v0 = 30 # initial velocity (m/s)
theta = np.radians(45) # launch angle (radians)
x0 = 0 # initial horizontal position (m)
y0 = 0.1 # initial vertical position (m)
dt = 0.01 # time step (s)
t_max = 5 # maximum time (s)

# Calculate initial velocities in x and y directions
vx0 = v0*np.cos(theta)
vy0 = v0*np.sin(theta)

# Initialize arrays to store positions and velocities
t = np.arange(0, t_max+dt, dt)
x = np.zeros_like(t)
y = np.zeros_like(t)
vx = np.zeros_like(t)
vy = np.zeros_like(t)

# Set initial positions and velocities
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

# Iterate over time steps and calculate positions and velocities
for i in range(1, t.size):
    # Calculate forces in x and y directions due to air resistance and gravity
    fx = -k*vx[i-1]
    fy = -k*vy[i-1] - m*g
    
    # Calculate accelerations in x and y directions
    ax = fx/m
    ay = fy/m
    
    # Calculate new velocities in x and y directions
    vx[i] = vx[i-1] + ax*dt
    vy[i] = vy[i-1] + ay*dt
    
    # Calculate new positions in x and y directions
    x[i] = x[i-1] + vx[i]*dt
    y[i] = y[i-1] + vy[i]*dt
    
    # Stop iterating if the projectile hits the ground
    if y[i] < 0:
        break

# Plot the trajectory of the projectile
plt.plot(x[:i], y[:i])
plt.xlabel('Horizontal position (m)')
plt.ylabel('Vertical position (m)')
plt.title('Projectile Motion with Air Resistance')
plt.show()
