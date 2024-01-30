# Projectile Motion
Projectile motion is a fundamental concept in physics that describes the motion of an object through
the air under the influence of gravity. When air resistance is considered, the equations of motion for a
projectile become more complex, requiring numerical or analytical solutions to be obtained. In this
report, we present a Python simulation that solves the equations of motion for a projectile with air
resistance and visualizes the resulting trajectory.
F x = -kvx
F y = -kvy - mg
m * dv x / dt = -kvx
m * dv y /dt = -kvy - mg
where F x and F y are the forces acting on the projectile in the x and y directions, respectively; v x and v y
are the velocities of the projectile in the x and y directions, respectively; m is the mass of the
projectile; g is the acceleration due to gravity; and k is a constant that describes the air resistance
coefficient.
When air resistance is negligible, these equations reduce to the simpler equations of motion for a
projectile in the absence of air resistance:
d^2x/dt^2 = 0
d^2y/dt^2 = -mg
which have the solutions:
x = x 0 + vx 0 *t
y = y 0 + vy 0 *t - 1/2 * g * t^2
where x 0 and y 0 are the initial positions of the projectile in the x and y directions, respectively; vx 0 and
vy 0 are the initial velocities of the projectile in the x and y directions, respectively; and tis the time
elapsed since the projectile was launched.
Methods
To solve the equations of motion for a projectile with air resistance, we used Python to implement a
numerical method that approximates the solutions over a range of time steps.
Why do we use ‘time steps’ in physics simulations?
In physics simulations, we often need to approximate the behaviour of a system over a range
of time. This can be done by dividing the total time into small, discrete intervals called time
steps. Each time step represents a small amount of time, and the simulation calculates the
behavior of the system at the end of each time step based on its behavior at the beginning of
the time step. By repeating this process for many time steps, we can approximate the behavior
of the system over a larger range of time.
To take this project as an example, we hope to simulate the motion of a ball through the air.
you are simulating the motion of a ball thrown through the air, we may divide the total time
into small time steps, say 0.01 seconds each. Then, at the beginning of each time step, you
would calculate the position and velocity of the ball based on its position and velocity at the
previous time step, as well as any external forces acting on the ball, such as gravity or air
resistance.
By repeating this process for many time steps, you can track the motion of the ball over a
longer period, such as several seconds or even minutes. The smaller the time step, the more
accurate the simulation will be,

We chose a time step of 0.01 seconds and a maximum time of 5 seconds. We also used the following
initial conditions:


 mass of the projectile, m = 0.05 kg
 acceleration due to gravity, g = 9.81 m/s^2
 air resistance coefficient, k = 0.1 kg/m
 initial velocity, v 0 = 30 m/s
 launch angle, theta = 45 degrees
 initial horizontal position, x 0 = 0 m
 initial vertical position, y 0 = 0.1 m
We then used the numerical method to approximate the velocities and positions of the projectile at
each time step, taking into account the forces due to air resistance and gravity. We stored the results in
arrays and plotted the trajectory of the projectile using the matplotlib library in Python.
