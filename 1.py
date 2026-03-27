
# Assuming 0-1, 2-3, 4-5, 6-7,..... are tooth region and 1-2, 3-4, 5-6, 7-8,....are gap region

import random
import math

num_segments = 100
num_rotations = 1000
num_per_rotation = 10000
omega = 3140                                       #30000 rpm
v = 299792458
R = .1                                             # radius 10 cm

gap_length = (2* (math.pi) *R) / num_segments                                
xmax = gap_length - ((omega * R * gap_length) / v)

def simulate(num_segments, num_rotations):
    
    total_passed = 0
    
    for n in range(num_rotations):
        
        accepted_values = set()
        
        while len(accepted_values) < num_per_rotation :
            
             i = random.randint(0, num_segments-1)# integer 0 to num_segments
             p = random.random()                  # random float 0 to 1 
             x = i + p                            # add random float (0 to 1)
             x = round(x, 5)                      # round to 5 decimal points

             if x not in accepted_values:
                accepted_values.add(x)
                if i % 2 == 1:
                    if (p*gap_length) <= xmax:
                        total_passed += 1
                    
    return total_passed / (num_rotations * num_per_rotation)


# ------------------------
# RUN
# ------------------------
probability_pass = simulate(num_segments, num_rotations)

print(f"Intensity Ratio: {probability_pass:.10f}")
