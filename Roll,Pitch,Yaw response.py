import numpy as np
import matplotlib.pyplot as plt

# Time vector
time = np.linspace(0, 10000, 1000)

# Parameters for damped oscillations
# Roll (red)
roll_amplitude = 2.5
roll_damping = 0.0004
roll_frequency = 0.002
roll = roll_amplitude * np.exp(-roll_damping * time) * np.cos(roll_frequency * time)

# Pitch (green)
pitch_amplitude = 2.0
pitch_damping = 0.0005
pitch_frequency = 0.0025
pitch = pitch_amplitude * np.exp(-pitch_damping * time) * np.cos(pitch_frequency * time)

# Yaw (blue)
yaw_amplitude = 2.5
yaw_damping = 0.0003
yaw_frequency = 0.0018
yaw = yaw_amplitude * np.exp(-yaw_damping * time) * np.cos(yaw_frequency * time)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(time, roll, label="Roll", color='red')
plt.plot(time, pitch, label="Pitch", color='green')
plt.plot(time, yaw, label="Yaw", color='blue')

# Graph labels and legend
plt.title("Attitude Control at Ideal Conditions")
plt.xlabel("Time")
plt.ylabel("Angle (rad)")
plt.legend(loc="best")
plt.grid(True)

# Display the graph
plt.show()
