import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Initialize parameters
beta = 0.3  # infection probability
gamma = 0.05  # recovery probability
size = 100  # size of the grid (100x100)
timesteps = 100  # number of time steps to simulate

# Create population grid 
population = np.zeros((size, size))

# Randomly select one infected individual
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# Set up the figure
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title("Initial Outbreak")
plt.colorbar(label="State (0=S, 1=I, 2=R)") # use numbers to represent status: 0 = susceptible, 1 = infected, 2 = recovered
plt.show()

# Simulation loop
for t in range(timesteps):
    # Find all infected points
    infected_indices = np.where(population == 1)
    infected_points = list(zip(infected_indices[0], infected_indices[1]))
    
    # Infect neighbors
    for (i, j) in infected_points:
        # Check all 8 neighbors of an infector
        for x in range(max(0, i-1), min(size, i+2)):
            for y in range(max(0, j-1), min(size, j+2)):
                if (x, y) != (i, j) and population[x, y] == 0:  # don't infect self and only susceptible
                    if np.random.random() < beta:
                        population[x, y] = 1
        
        # Recover with probability gamma
        if np.random.random() < gamma:
            population[i, j] = 2
    
    # Plot every 10 timesteps (optional)
    if t % 10 == 0 or t == timesteps - 1: 
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time Step {t}")
        plt.colorbar(label="State (0=S, 1=I, 2=R)")
        plt.show()