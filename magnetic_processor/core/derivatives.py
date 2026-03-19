def horizontal_derivative(data, dx):
    """Calculate horizontal derivative of the data."""
    return (data[:, 1:] - data[:, :-1]) / dx


def vertical_derivative(data, dz):
    """Calculate vertical derivative of the data."""
    return (data[1:, :] - data[:-1, :]) / dz


def analytic_signal(data):
    """Compute the analytic signal of the data using Hilbert transform."""
    from scipy.signal import hilbert
    return hilbert(data)


def total_horizontal_derivative(data, dx):
    """Calculate total horizontal derivative of the data."""
    hx = horizontal_derivative(data, dx)
    return hx


# Example Usage:  
# Assuming `data` is a 2D NumPy array with values and `dx` is the step size for the horizontal derivative.
# hx = horizontal_derivative(data, dx)
# vz = vertical_derivative(data, dz)
# analytic = analytic_signal(data)
# total_hx = total_horizontal_derivative(data, dx)