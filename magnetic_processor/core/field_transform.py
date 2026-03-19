import numpy as np

# Gravity second vertical derivative

def gravity_second_vertical_derivative(gravity_data, dz):
    return np.gradient(np.gradient(gravity_data, dz), dz)

# Regional residual separation

def regional_residual_separation(total_field, regional_field):
    return total_field - regional_field

# Magnetic source depth calculations

def magnetic_source_depth(magnetic_data, density, gradient):
    return (magnetic_data / (density * gradient))

# Example usage:
# gravity_data = [0.1, 0.2, 0.15, 0.25]
# second_derivative = gravity_second_vertical_derivative(gravity_data=gravity_data, dz=1)
# print('Second Vertical Derivative:', second_derivative)

# total_field = [1.0, 2.0, 3.0]
# regional_field = [0.5, 1.5, 2.5]
# residual = regional_residual_separation(total_field, regional_field)
# print('Regional Residual:', residual)

# magnetic_data = 100
# density = 2.67
# gradient = 0.01
# depth = magnetic_source_depth(magnetic_data, density, gradient)
# print('Magnetic Source Depth:', depth)