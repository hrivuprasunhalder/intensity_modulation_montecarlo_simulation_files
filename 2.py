
# Assuming 0-1, 2-3, 4-5, 6-7,..... are tooth region and 1-2, 3-4, 5-6, 7-8,....are gap region

import random
import math

num_segments = 100
num_rotations = 500
num_per_rotation = 10000
omega = 100000                                    #rad/s
v = 299792458                                     #m/s
R = 10                                            #radius(m)

gap_length = (2* (math.pi) *R) / num_segments                                
xmax = gap_length - ((omega * R * gap_length) / v)

def simulate(num_segments, num_rotations):
    
    total_passed = 0
    
    for n in range(num_rotations):
        
        
        for m in range(num_per_rotation) :
            
             i = random.randint(0 , num_segments-1)# random integer in 0 to num_segments range
             x = random.uniform(0 , gap_length )   # random float in 0 to gap_length range              
             
             if i % 2 == 1:                        # odd number + x = gap range
                if x < xmax:
                    total_passed += 1
                    
    return total_passed / (num_rotations * num_per_rotation)


# ------------------------
# RUN
# ------------------------
probability_pass = simulate(num_segments, num_rotations)

print(f"Intensity Ratio: {probability_pass:.16f}")
