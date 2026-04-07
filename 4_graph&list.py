# Assuming 0-1, 2-3, 4-5, 6-7,..... are tooth region and 1-2, 3-4, 5-6, 7-8,....are gap region

import random
import math
import csv

num_tries = 100
num_segments = 100
num_rotations = 500
omega = 3140                                    # 30000 rpm
v = 299792458
R = 0.06                                        # radius 10 cm

gap_length = (2* (math.pi) *R) / num_segments                                
xmax = gap_length - ((omega * R * gap_length) / v)

def simulate(num_per_rotation):
    
    total_passed = 0
    
    for n1 in range(num_rotations):
        
        
        for m1 in range(num_per_rotation):
            
             i = random.randint(0 , num_segments-1)# random integer in 0 to num_segments range
             x = random.uniform(0 , gap_length )   # random float in 0 to gap_length range              
             
             if i % 2 == 1:                        # odd number + x = gap range
                if x < xmax:
                    total_passed += 1
                    
    return total_passed / (num_rotations * num_per_rotation)


def tries(num_per_rotation):

    counts = 0                                      #probabilities over 0.5

    for n2 in range(num_tries):
        
         probability = simulate(num_per_rotation)

         if probability < 0.5:
              counts = counts + 1

    return counts

x_values_num_per_rotation = list(range(1000, 13000, 1000))
y_values_valid_values = [tries(p) for p in x_values_num_per_rotation ]

with open("Omega3140data.csv", "w", newline="") as file:
    writer = csv.writer(file)                    #csv file creation
    writer.writerow(["Particles per Rotation", " Validity(%)"])
    for n3 in range(len(x_values_num_per_rotation)):
        writer.writerow([x_values_num_per_rotation[n3],y_values_valid_values[n3]])

max_y = max(y_values_valid_values)
index_of_max = y_values_valid_values.index(max_y)# most accurate particle number determination
x_for_max_y = x_values_num_per_rotation[index_of_max]

print("Most accurate particle number per rotation: ", x_for_max_y)
        

    

 




