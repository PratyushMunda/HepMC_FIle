import pyhepmc
import numpy as np
import matplotlib.pyplot as plt

path = "D:/Code/gsoc/McNet/top1/top.hepmc"

#Assigning Variables
pt_values = []
particles_per_event = []

#Finding number of events and calcualting values for ploting the histogram
with pyhepmc.open(path) as f:
    num_events = 0  
    for event in f:
        num_events += 1
        num_particles = len(event.particles)  
        particles_per_event.append(num_particles)

print(f"Total number of events: {num_events}")


with pyhepmc.open(path) as f:
    for event in f:
        for particle in event.particles:
            if particle.status == 1: 
                px, py = particle.momentum.x, particle.momentum.y
                pt = np.sqrt(px**2 + py**2) 
                pt_values.append(pt)

number_of_particle=int(input(f"Enter number of final state particle you want to see range from(1-{len(pt_values)})"))                
for i, pt in enumerate(pt_values[:number_of_particle]): 
    print(f"Particle {i+1}: pT = {pt:.2f} GeV/c")


print(f"\nTotal number of final-state particles: {len(pt_values)}")
print(f"Mean pT: {np.mean(pt_values):.2f} GeV/c")
print(f"Max pT: {np.max(pt_values):.2f} GeV/c")
print(f"Min pT: {np.min(pt_values):.2f} GeV/c")      

#Histogram for Distribution of Particle
plt.figure(figsize=(8, 5))
plt.hist(particles_per_event, bins=30, color="blue", edgecolor="black", alpha=0.7)
plt.xlabel("Number of Particles per Event")
plt.ylabel("Frequency")
plt.title("Distribution of Particles per Event")
plt.grid(True)
plt.show()

#Histogram for Distribution of Transverse Momentum
plt.figure(figsize=(10, 6))
plt.hist(pt_values, bins=50, color='blue', edgecolor='black', alpha=0.7)
plt.yscale('log') 
plt.xlabel("Transverse Momentum pT (GeV/c)")
plt.ylabel("Frequency")
plt.title("Distribution of Transverse Momentum (pT) for Status=1 Particles")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()