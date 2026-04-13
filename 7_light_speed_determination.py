# Assuming 0-1, 2-3, 4-5, 6-7,..... are tooth region and 1-2, 3-4, 5-6, 7-8,....are gap region

import random
import numpy as np
import matplotlib.pyplot as plt
import csv

num_segments = 100
num_per_rotation = 5000
num_rotations = 500
omega = 55000000                                     #rad/s
R = 1                                                #radius(m)
v = np.arange(1e8, 1e9, 1e7)                         #m/s 

gap_length = (2* (np.pi) *R) / num_segments                                
xmax_list = gap_length - ((omega * R * gap_length) / v)


def simulate(xmax):                                 #monte carlo simulation 
    
    total_passed = 0
    
    for n in range(num_rotations):
        
        
        for m in range(num_per_rotation) :
            
             i = random.randint(0 , num_segments-1)# random integer in 0 to num_segments range
             x = random.uniform(0 , gap_length )   # random float in 0 to gap_length range              
             
             if i % 2 == 1:                        # odd number + x = gap range
                if x < xmax:
                    total_passed += 1
                    
    return total_passed / (num_rotations * num_per_rotation)


p_prob = [simulate(xmax) for xmax in xmax_list]    #probabilistic result using monte carlo simmulation

# Save results to CSV
with open("probability_vs_velocity_8.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Probability", "Velocity (m/s)"])
    for pi, vi in zip(p_prob, v):
        writer.writerow([pi, vi])

# Plot probability vs velocity
plt.figure(figsize=(8,6))
plt.plot(p_prob, v, marker=".", label="Monte Carlo Simulation")
plt.xlabel("Probability (Intensity Ratio)")
plt.ylabel("Velocity (m/s)")

# Draw vertical line at given intensity ratio (from equation)
intensity_ratio_eq = 0.5*(1- ((omega*R)/299792458))
plt.axvline(x=intensity_ratio_eq, color="red", linestyle="--", label="Equation Intensity Ratio")

# Find intersection (closest probability to intensity ratio)
closest_idx = np.argmin(np.abs(np.array(p_prob) - intensity_ratio_eq))
speed_of_light_est = v[closest_idx]

# Draw horizontal line at intersection
plt.axhline(y=speed_of_light_est, color="green", linestyle="--", label=f"Speed of Light ≈ {speed_of_light_est:.2e} m/s")

plt.legend()
plt.savefig("probability_vs_velocity_8.png")
plt.show()

print(f"Estimated speed of light from simulation: {speed_of_light_est:.2e} m/s")        

