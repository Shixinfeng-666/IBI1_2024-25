import numpy as np
import matplotlib.pyplot as plt

# define initial conditions
num_population = 10000
num_I = 1
num_S = num_population-num_I
num_R = 0
# define parameters
beta = 0.3
gamma = 0.05
# Initialize arrays to track the evolution over time
time_steps = 1000
S = np.zeros(time_steps)
I = np.zeros(time_steps)
R = np.zeros(time_steps)
# set begining values of arrays
S[0] = num_S
I[0] = num_I
R[0] = num_R
# begin time loop with 'beta 0.3' and 'gamma 0.05'

for i in range(time_steps-1):
    new_beta = beta* num_I/ num_population
    new_I = sum(np.random.choice(range(2),num_S,p = [1-new_beta,new_beta]))
    new_R = sum(np.random.choice(range(2),num_I,p = [1-gamma,gamma]))
    num_S = num_S-new_I
    num_I = num_I+new_I-new_R
    num_R = num_R+new_R
    
# Update the number of susceptible, infected, and recovered individuals
    S[i+1] = num_S
    I[i+1] = num_I
    R[i+1] = num_R

# output the plot
plt.figure(figsize=(10, 6))
plt.plot(S, label='Susceptible')
plt.plot(I, label='Infected')
plt.plot(R, label='Recovered')
plt.xlabel('Time step')
plt.ylabel('Number of individuals')
plt.title('Simulation of Infection Spread')
plt.legend()
plt.show()