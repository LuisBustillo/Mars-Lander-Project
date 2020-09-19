# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# simulation time, timestep and time
t_max = 100
dt = 0.1
t_array = np.arange(0, t_max, dt)


# initialise empty lists to record trajectories
x_list = []
v_list = []

# Euler integration :
for t in t_array:

    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a

# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array_euler = np.array(x_list)
v_array_euler = np.array(v_list)


# Verlet Integration :

x_verlet = []
v_verlet = []
x_verlet.append(0)
x_t = np.sin(0 + dt)
v_verlet.append(1)
v_v = (x_t - x_verlet[0])/dt

for i in range (0, len(t_array)-1) :
    
    # append current state to trajectories
    x_verlet.append(x_t)
    v_verlet.append(v_v)

    # calculate new position and velocity
    a_v = -k * x_t / m
    x_t = 2*x_t - x_verlet[-2] + (dt**2)*a_v
    v_v = (0.5/dt)*(x_t - x_verlet[-2])
    
x_array_verlet = np.array(x_verlet)
v_array_verlet = np.array(v_verlet)

# Analytical Solution :

x_anal = []
v_anal = []
x_a = 0
v_a = 1
i = 0

for t in t_array:

    # append current state to trajectories
    x_anal.append(x_a)
    v_anal.append(v_a)
    
    # calculate new position and velocity
    x_a = np.sin(t_array[i])
    v_a = np.cos(t_array[i])
    i += 1
    
    

x_array_anal = np.array(x_anal)
v_array_anal = np.array(v_anal)



# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array_euler, label='x_euler (m)')
plt.plot(t_array, x_array_verlet, label='x_verlet (m)')
plt.plot(t_array, x_array_anal, label='x_analytical (m)')
plt.legend()
plt.show()


# plot the velocity-time graph
plt.figure(2)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, v_array_euler, label='v_euler (m/s)')
plt.plot(t_array, v_array_verlet, label='v_verlet (m/s)')
plt.plot(t_array, v_array_anal, label='v_analytical (m/s)')
plt.legend()
plt.show()


