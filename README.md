# 🍈 Jackfruit Problem: Autonomous Drone Simulation and Control

## 1. Project Overview

This project is developed for the **Mobile and Autonomous Robots (UE23CS343BB7)** course at **PES University**.

It implements a **high-fidelity 3D drone simulation** using **ROS 2 Jazzy** and **Gazebo Sim**, focusing on autonomous navigation in complex environments with dynamic obstacles.

The system follows a **modular architecture**, ensuring scalability, maintainability, and clear separation of responsibilities.

---

## 2. Team Members & Contributions

| Member | Responsibility | Description |
|--------|----------------|-------------|
| Omkar | Motion Control | Developed 6-DOF velocity mapping logic (`motion_controller.py`) |
| Srikar | Safety & Error Handling | Implemented emergency kill switch and reset system (`safety_monitor.py`) |
| Praneeth | Vision & Status | Handled sensor logging and RViz visualization (`vision_processor.py`) |
| Vikhyath | Integration & Interface | Managed ROS 2 node orchestration and system execution (`drone_main.py`) |

---

## 3. Features

- 🚨 **Emergency Kill Switch** — Immediate shutdown of drone motion for safety-critical scenarios
- 🌍 **Realistic Physics (DART Engine)** — Accurate collision detection with obstacles like trees, barrels, and barriers
- 🧩 **Modular Architecture** — Clean separation across multiple modules for maintainability
- 📡 **ROS 2 Integration** — Seamless communication between simulation and control layers
- 🎥 **RViz Visualization** — Real-time camera feed and debugging interface

---

## 4. System Requirements

- Ubuntu 22.04 (Recommended)
- ROS 2 Jazzy
- Gazebo Sim (Ignition Gazebo)
- RViz2

---

## 5. Execution Instructions

> ⚠️ **Important:** Open **4 separate terminals** and run commands in order.

---

### 🖥️ Terminal 1: Launch Gazebo Simulation

Loads the 3D world and physics engine.

```bash
export GZ_SIM_RESOURCE_PATH=~/drone_project_ws/src/drone_sim/models
gz sim -r ~/drone_project_ws/src/drone_sim/worlds/drone_world.sdf
```

---

### 🔗 Terminal 2: ROS 2 – Gazebo Bridge

Connects Gazebo topics with ROS 2.

```bash
ros2 run ros_gz_bridge parameter_bridge \
  /model/x3/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist \
  /camera@sensor_msgs/msg/Image@gz.msgs.Image
```

---

### 📊 Terminal 3: RViz2 Visualization

Launch the visualization interface.

```bash
ros2 run rviz2 rviz2
```

**RViz Setup:**
- Set **Fixed Frame** → `world`
- Add → **Image Display**
- Topic → `/camera`

---

### 🎮 Terminal 4: Drone Controller

Start the main control node.

```bash
source ~/drone_project_ws/install/setup.bash
ros2 run drone_sim drone_main
```

---

## 6. Control Schema

| Key | Action |
|-----|--------|
| `W` / `S` | Forward / Backward |
| `A` / `D` | Left / Right |
| `U` / `J` | Up / Down |
| `+` / `-` | Increase / Decrease Speed |
| `K` | 🚨 Emergency Kill Switch |
| `R` | 🔄 Reset / Re-arm Drone |

---

## 7. Project Structure

```
drone_project_ws/
├── src/
│   └── drone_sim/
│       ├── motion_controller.py
│       ├── safety_monitor.py
│       ├── vision_processor.py
│       ├── drone_main.py
│       ├── models/
│       └── worlds/
├── install/
├── build/
└── log/
```

---

## 8. Key Highlights for Evaluation

- ✔️ Fully functional ROS 2 + Gazebo integration
- ✔️ Modular and maintainable codebase
- ✔️ Real-time visualization via RViz
- ✔️ Safety-critical features implemented
- ✔️ Clear execution steps for reproducibility

---

## 9. Notes

- Ensure all dependencies are installed before running
- Use separate terminals as instructed
- Verify topic names if the simulation model changes

---

## 10. Future Improvements

- Autonomous navigation (path planning)
- Obstacle avoidance using sensors
- Multi-drone swarm coordination
- AI-based decision making
