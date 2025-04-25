import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

N_list = []

# define initial conditions
for j in range(11):
    num_population = 10000
    prt_vaccination = 0.1*j  # assume various percent of the population are vaccinated
    num_I = 1
    num_S = int(num_population - num_I - num_population*prt_vaccination)
    num_R = 0
    num_V = num_population*prt_vaccination # add the definition of vaccinated people
    
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
        
        # calculate the actual probabilities of infection
        if num_S > 0:
            new_I = sum(np.random.choice(range(2),num_S,p = [1-new_beta,new_beta]))
        else:
            new_I = 0
       
        if num_I > 0:
            new_R = sum(np.random.choice(range(2),num_I,p = [1-gamma,gamma]))
        else:
            new_R = 0
        
        # update the value of each group
        num_S = max(num_S-new_I, 0)
        num_I = max(num_I+new_I-new_R, 0)
        num_R = max(num_R+new_R, 0)
        
    # Update the number of susceptible, infected, and recovered individuals
        S[i+1] = num_S
        I[i+1] = num_I
        R[i+1] = num_R
    
    # add the result into the list
    N_list.append(I)
   
    # output the plot
plt.figure(figsize=(10, 6))
for j in range(11):
    plt.plot(N_list[j], label=f'{int(0.1*j*100)}%')
    
plt.xlabel('Time step')
plt.ylabel('Number of Infected Individuals')
plt.title('Simulation of Infection Spread')
plt.legend(title='Vaccination Rate')
plt.plot(color = cm.viridis(30))
plt.show()
