import time
import matplotlib.pyplot as plt

# Paper thickness before folding (in meters)
THICKNESS = 0.00008

# 1. Calculate the thickness using the exponentiation operator (t_43 = t_0 * 2^43)
folded_thickness = THICKNESS * (2 ** 43)

# Unit conversion to Output the result in meters and kilometers
print("Thickness after 43 folds: {:.2f} meters".format(folded_thickness))
print("Thickness after 43 folds: {:.2f} kilometers".format(folded_thickness / 1000))

# 2. Measure execution time for the exponentiation method
start = time.time()
folded_thickness = THICKNESS * (2 ** 43)
elapsed_time = time.time() - start
print("Execution time for exponentiation method: {:.6f} seconds".format(elapsed_time))

# 3. Calculate the thickness using a for loop (without using exponentiation)
current_thickness = THICKNESS
for _ in range(43):
    current_thickness *= 2

print("Thickness after 43 folds (using loop): {:.2f} meters".format(current_thickness))

# 4. Measure execution time for the for loop method
start = time.time()
current_thickness = THICKNESS
for _ in range(43):
    current_thickness *= 2
elapsed_time = time.time() - start
print("Execution time for for-loop method: {:.6f} seconds".format(elapsed_time))

# 5. save thickness values after each fold to a list for graph visualization
thickness_list = [THICKNESS]
for _ in range(43):
    thickness_list.append(thickness_list[-1] * 2)

# Verify the list contains 44 values (including the original thickness)
print("Number of values in the list:", len(thickness_list))

# 6. Display a graph showing the thickness after each fold
plt.title("Thickness of Folded Paper")
plt.xlabel("Number of Folds")
plt.ylabel("Thickness (meters)")
plt.plot(thickness_list, color='red', linewidth=2, linestyle='dotted')  # Customization
plt.tick_params(labelsize=14)  # Increase font size of tick labels
plt.show()
