import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define system parameters
Kp = np.array([1.0, 1.0, 1.0])  # Proportional gains for roll, pitch, yaw
Ki = np.array([0.1, 0.1, 0.1])  # Integral gains for roll, pitch, yaw
Kd = np.array([0.01, 0.01, 0.01])  # Derivative gains for roll, pitch, yaw
T_i = np.array([0.1, 0.1, 0.1])  # Integrator time constants
T_d = np.array([0.1, 0.1, 0.1])  # Derivative time constants

# Initial conditions (initial angles and velocities)
initial_conditions = [0, 0, 0, 0, 0, 0]  # [roll, pitch, yaw, roll_dot, pitch_dot, yaw_dot]

# Desired angles (setpoints)
desired_angles = np.array([10, 10, 10])  # [roll_setpoint, pitch_setpoint, yaw_setpoint]

# Define system dynamics (State-Space Model)
def satellite_dynamics(y, t, Kp, Ki, Kd, T_i, T_d, desired_angles):
    # Extract the current state from the solution vector
    roll, pitch, yaw, roll_dot, pitch_dot, yaw_dot = y
    
    # Calculate errors
    error_roll = desired_angles[0] - roll
    error_pitch = desired_angles[1] - pitch
    error_yaw = desired_angles[2] - yaw
    
    # Calculate PID control terms (Proportional, Integral, Derivative)
    integral_roll = error_roll * T_i[0]
    integral_pitch = error_pitch * T_i[1]
    integral_yaw = error_yaw * T_i[2]
    
    derivative_roll = (error_roll - (desired_angles[0] - roll)) * T_d[0]
    derivative_pitch = (error_pitch - (desired_angles[1] - pitch)) * T_d[1]
    derivative_yaw = (error_yaw - (desired_angles[2] - yaw)) * T_d[2]
    
    # Control signals (inputs to the system)
    control_roll = Kp[0] * error_roll + Ki[0] * integral_roll + Kd[0] * derivative_roll
    control_pitch = Kp[1] * error_pitch + Ki[1] * integral_pitch + Kd[1] * derivative_pitch
    control_yaw = Kp[2] * error_yaw + Ki[2] * integral_yaw + Kd[2] * derivative_yaw
    
    # Satellite dynamics (simplified model)
    # These are basic dynamics assuming a simple linear system
    # (For real-world systems, these dynamics will be more complex)
    roll_dot_dot = -roll_dot + control_roll  # Roll angular acceleration
    pitch_dot_dot = -pitch_dot + control_pitch  # Pitch angular acceleration
    yaw_dot_dot = -yaw_dot + control_yaw  # Yaw angular acceleration
    
    # Return the derivatives of the state variables
    return [roll_dot, pitch_dot, yaw_dot, roll_dot_dot, pitch_dot_dot, yaw_dot_dot]

# Time vector for simulation (0 to 10 seconds, with 0.01s time step)
t = np.linspace(0, 10, 1000)

# Solve the system of differential equations using odeint
solution = odeint(satellite_dynamics, initial_conditions, t, args=(Kp, Ki, Kd, T_i, T_d, desired_angles))

# Extract the results from the solution
roll = solution[:, 0]
pitch = solution[:, 1]
yaw = solution[:, 2]
roll_dot = solution[:, 3]
pitch_dot = solution[:, 4]
yaw_dot = solution[:, 5]

# Plot the results
plt.figure(figsize=(12, 8))

# Plot Roll Angle
plt.subplot(3, 1, 1)
plt.plot(t, roll, label="Roll Angle (rad)", color='b')
plt.axhline(desired_angles[0], color='r', linestyle='--', label="Desired Roll")
plt.title("Roll Angle vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.legend()

# Plot Pitch Angle
plt.subplot(3, 1, 2)
plt.plot(t, pitch, label="Pitch Angle (rad)", color='g')
plt.axhline(desired_angles[1], color='r', linestyle='--', label="Desired Pitch")
plt.title("Pitch Angle vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.legend()

# Plot Yaw Angle
plt.subplot(3, 1, 3)
plt.plot(t, yaw, label="Yaw Angle (rad)", color='m')
plt.axhline(desired_angles[2], color='r', linestyle='--', label="Desired Yaw")
plt.title("Yaw Angle vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Angle [rad]")
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
