# Satellite Attitude Control System


**🌌 Design and Simulation of Satellite Attitude Control System 🚀
Using State-Space Modelling, Feedback Control, and State Estimation**


**📖 Project Overview**


This project explores the design and simulation of a satellite attitude control system using advanced control techniques. We utilize state-space modeling, PID feedback control, and state estimation (Kalman Filter) to stabilize and control the satellite's Roll, Pitch, and Yaw angles.


**✨ Key Features:**


1.Mathematical modeling of satellite dynamics using state-space representation.


2.Implementation of state feedback control with a PID controller.


3.Kalman Filter for robust state estimation.


4.Simulation results showcasing stabilization and precision.


**🎯 Objectives**
Model Satellite Attitude Dynamics


Represent Roll, Pitch, and Yaw motions mathematically using state-space equations.


Design a PID-based state feedback control system to achieve stability.


Minimize overshoot, oscillations, and steady-state error.


Use Python and Simulink for system simulation.


Generate graphs to analyze system behavior over time.


Apply a Kalman Filter for precise state tracking.


**🛠️ Tools & Technologies**


**Python:** For simulation and visualization of system responses.


**Simulink:** For block diagram modeling and real-time system simulation.


**LaTeX:** For documenting mathematical formulations and simulation results.


**Control Theory:** PID, state-space representation, Kalman filtering.


**📂 File Structure**
bash
Copy code
📁 Satellite_Attitude_Control_System  
├── 📜 README.md                # Project Documentation  
├── 📜 satellite_model.py       # Python script for system simulation  
├── 📜 satellite_simulink.slx   # Simulink model file  
├── 📜 report.pdf              # Detailed report with equations, graphs, and analysis  
└── 📜 images/                  # Visualization graphs and block diagrams  


**🖥️ Simulation Results**


**Key Observations:**


**Damped Oscillations:** Smooth stabilization after initial overshoot.


**Roll, Pitch, Yaw Differences:** Yaw exhibits higher overshoot and longer settling time.


**Steady-State Accuracy:** Negligible steady-state error in all axes.


🔗 Check the detailed analysis in report.pdf.

**📚 How to Use**


Clone this repository:


bash


Copy code


git clone https://github.com/your-repo/satellite-attitude-control.git  


Install dependencies:


bash


Copy code


pip install -r requirements.txt 


Run the Python simulation:


bash


Copy code


python satellite_model.py 


Open and modify the Simulink model as needed:


**🤝 Contributions**


Contributions are welcome! If you have suggestions or improvements, feel free to submit a pull request or open an issue.

**🎓 Acknowledgments**


Special thanks to the developers of:


**Python libraries:** NumPy, SciPy, Matplotlib


**MATLAB/Simulink** for dynamic system simulation


**Researchers and enthusiasts** in control theory and satellite dynamics


**🪐 Future Work**


Integrate disturbance rejection algorithms.


Explore nonlinear control methods for satellite systems.


Add hardware-in-the-loop (HIL) simulation.


**🚀 Happy Simulating! 🌟**
