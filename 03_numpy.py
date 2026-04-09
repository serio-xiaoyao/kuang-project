import numpy as np

my_list = [[10,20],[30,40]]
print(my_list, type(my_list))

my_array = np.array(my_list)
print(my_array, type(my_array))

print(my_array + 2)

print(np.max(my_array))

print(np.add(my_array, 2))