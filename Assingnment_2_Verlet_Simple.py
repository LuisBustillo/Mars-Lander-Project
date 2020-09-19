# Numerical Dynamics in Three Dimensions

import numpy as np 
import matplotlib.pyplot as plt
import math

# Defining Variables
G = 6.67e-11
M = 6.42e23
R = 3.3895e6
m = 100

# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
position_list = []
velocity_list = []

#position_matrix = np.zeros(shape=(len(t_array),3))
#velocity_matrix = np.zeros(shape=(len(t_array),3))

# 3-element numpy matrices

position_list.append(np.array([0, 1e7, 0]))
velocity = np.array([np.sqrt((G*M)/np.linalg.norm(position_list[0])), 0, 0])
position = position_list[0] + dt*velocity + 0.5*dt*dt*(-G*M*position_list[0]/math.pow(np.linalg.norm(position_list[0]), 3))


"""

Scenario 1 : vx = 0

Scenario 2 : vx = np.sqrt((G*M)/np.linalg.norm(position_list[0]))

Scenario 3 : vx = 2500

Scenario 4 : vx = np.sqrt((2*G*M)/np.linalg.norm(position_list[0]))

"""

for t in t_array:
    for i in range ( 0, len(t_array) - 1 ) :
        if ( np.linalg.norm(position) >= R ) :
            
            position_list.append(position)
            velocity_list.append(velocity)
            
            # To calculate gravitational acceleration:
            acceleration = (-G*M*position/math.pow(np.linalg.norm(position), 3))

            # To do a Verlet update:
            position = 2*position - position_list[-2] + dt*dt*acceleration 
            velocity = (0.5/dt) * (position - position_list[-2])
            
        else:
            break


position_y_final = []
position_x_final = []

for i in position_list :
    position_y_final.append(i[1])
    position_x_final.append(i[0])



# Scenario 1 : Straight Down Descent
# Set graph to altitude (y) against time
# Set vx variable to 0
"""
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, position_y_final, label='altitude (m)')
plt.legend()
plt.show()

"""

# Scenario 2 : Circular Orbit
# Set graph to y-coordinate against x-coordinate
# Set vx variable to np.sqrt((G*M)/np.linalg.norm(position))

# Scenario 3 : Elliptical Orbit
# Set graph to y-coordinate against x-coordinate
# Set vx variable to anywhere in between Scenarios 2 and 4

# Scenario 4 : Hyperbolic Escape
# Set graph to y-coordinate against x-coordinate
# Set vx variable to np.sqrt((2*G*M)/np.linalg.norm(position))

plt.figure(2)
plt.clf()
plt.xlabel('y-coordinate (m)')
plt.grid()
plt.plot(position_y_final, position_x_final, label='x-coordinate (m)')
plt.legend()
plt.show()




