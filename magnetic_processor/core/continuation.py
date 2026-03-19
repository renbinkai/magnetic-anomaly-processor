import numpy as np

# Define the Upward Continuation function

def upward_continuation(data, height):
    # Implement upward continuation logic here
    kx = np.fft.fftfreq(data.shape[0])
    kz = np.sqrt(kx**2 + (2 * np.pi * height) ** 2)
    transformed_data = np.fft.fft2(data) * np.exp(-1j * kz)
    return np.fft.ifft2(transformed_data)

# Define the Downward Continuation function

def downward_continuation(data, height):
    # Implement downward continuation logic here
    kx = np.fft.fftfreq(data.shape[0])
    kz = np.sqrt(kx**2 + (2 * np.pi * height) ** 2)
    transformed_data = np.fft.fft2(data) * np.exp(1j * kz)
    return np.fft.ifft2(transformed_data)

# Example Usage:
# data = np.random.rand(256, 256)  # Replace with actual magnetic anomaly data
# upward_data = upward_continuation(data, 100)
# downward_data = downward_continuation(data, 100)