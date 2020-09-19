# Numerical Dynamics in Three Dimensions

import numpy as np 
import matplotlib.pyplot as plt

# Defining Variables
G = 6.67e-11
M = 6.42e23
R = 3.3895e6
m = 100

# simulation time, timestep and time
t_max = 30000
dt = 10
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
position_matrix = np.zeros(shape=(len(t_array),3))
velocity_matrix = np.zeros(shape=(len(t_array),3))

# Initial Conditions
x0 = 0
y0 = 1e7
z0 = 0
# Scenario 1
#vx = 0
# Scenario 2
vx = np.sqrt((G*M)/y0)
# Scenario 3
#vx = 2500
# Scenario 4
#vx = np.sqrt((2*G*M)/y0)
vy = 0
vz = 0

# 3-element numpy matrices
position_matrix[0] = ([x0,y0,z0])
velocity_matrix[0] = ([vx,vy,vz])

acceleration = np.zeros(3)
# Counter
i = 0


def Force_div_mass (x,y) :
    r = np.sqrt( (abs(x))**2 + (abs(y))**2 )
    a = -(G*M)/(r**2)
    
    acceleration[0] = a * (x/r)
    acceleration[1] = a * (y/r)
    
    return acceleration

  
for t in t_array:
    for i in range (0,len(t_array)-1):
        if ( np.sqrt( (abs(position_matrix[i][0]))**2 + (abs(position_matrix[i][1]))**2 ) > R ) : 
            
            # calculate new position and velocity
            acceleration = Force_div_mass(position_matrix[i][0], position_matrix[i][1])
            position_matrix[i+1] = position_matrix[i] + (dt * velocity_matrix[i])
            velocity_matrix[i+1] = velocity_matrix[i] + (dt * acceleration)
            i += 1
            
        else:
            break


position_y_final = []
position_x_final = []

for i in position_matrix :
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
# Set vx variable to np.sqrt((G*M)/y0)

# Scenario 3 : Elliptical Orbit
# Set graph to y-coordinate against x-coordinate
# Set vx variable to anywhere in between Scenarios 2 and 4

# Scenario 4 : Hyperbolic Escape
# Set graph to y-coordinate against x-coordinate
# Set vx variable to np.sqrt((2*G*M)/y0)

plt.figure(2)
plt.clf()
plt.xlabel('y-coordinate (m)')
plt.grid()
plt.plot(position_y_final, position_x_final, label='x-coordinate (m)')
plt.legend()
plt.show()

