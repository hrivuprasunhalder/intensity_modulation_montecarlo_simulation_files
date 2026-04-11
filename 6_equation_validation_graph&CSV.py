# Assuming 0-1, 2-3, 4-5, 6-7,..... are tooth region and 1-2, 3-4, 5-6, 7-8,....are gap region

import random
import numpy as np
import matplotlib.pyplot as plt
import csv

num_segments = 100
num_per_rotation = 5000
num_rotations = 500
omega = 3141.6                                     #rad/s, 30000 rpm
R = .06                                            #radius(m), 6 cm
v = np.arange(300, 20600, 100)                      #m/s 

gap_length = (2* (np.pi) *R) / num_segments                                
xmax_list = gap_length - ((omega * R * gap_length) / v)


def simulate(xmax):                                #monte carlo simulation 
    
    total_passed = 0
    
    for n in range(num_rotations):
        
        
        for m in range(num_per_rotation) :
            
             i = random.randint(0 , num_segments-1)# random integer in 0 to num_segments range
             x = random.uniform(0 , gap_length )   # random float in 0 to gap_length range              
             
             if i % 2 == 1:                        # odd number + x = gap range
                if x < xmax:
                    total_passed += 1
                    
    return total_passed / (num_rotations * num_per_rotation)



p_det = xmax_list/(2 * gap_length)                 #deterministic result using the equation
p_prob = [simulate(xmax) for xmax in xmax_list]    #probabilistic result using monte carlo simmulation

#-----------PLOT----------------

plt.plot(v, p_det, label="Deterministic", color= "blue")
plt.plot(v, p_prob, label="Probabilistic", color= "red", linestyle= "--")
plt.xlabel("Velocity(m/s)")
plt.ylabel("Transmission Probabilty(I/I0)")
plt.title("Deterministic(Equation) vs Probabilistic(Monte Carlo) Results")
plt.legend()
plt.grid(True)
plt.savefig("validation_plot_5.png")
plt.show()
#-----------csv-------------------

with open("validation_5.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["v", "p_det", "p_prob"])
    for vi, yi1, yi2 in zip(v, p_det, p_prob):
        writer.writerow([vi, yi1, yi2])
