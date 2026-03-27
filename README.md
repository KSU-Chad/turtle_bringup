# Lab: Integrating Launch Files into a ROS 2 Package
### turtle_bringup — RA305 Robotics Programming

---

## Overview

By the end of this lab you will be able to:

- Create a minimal `ament_python` ROS 2 package that contains only launch files (no executable nodes)
- Build and install the package with `colcon`
- Launch the full turtlesim system with a single `ros2 launch` command
- Declare and override launch arguments from the command line

---

## Package Structure

After creating and populating the package, your workspace should look like this:

```
turtle_ws/
└── src/
    └── turtle_bringup/
        ├── launch/
        │   ├── turtle_bringup.launch.py          ← Part 1
        │   └── turtle_bringup_args.launch.py     ← Part 2
        ├── resource/
        │   └── turtle_bringup                    ← empty marker file (required)
        ├── turtle_bringup/
        │   └── __init__.py                       ← empty (required by Python)
        ├── package.xml
        ├── setup.cfg
        └── setup.py
```

---

## Prerequisites

Install xterm (needed for the teleop terminal window):

```bash
sudo apt install xterm
```

---

## Part 1 — Get the Package

Create your workspace folder and clone the repository directly into the `src` directory. All files,
except for the launch file we just created, are already in place.

### Step 1: Create the workspace and src directory

```bash
mkdir -p ~/turtle_ws/src
```

### Step 2: Navigate into the src directory

```bash
cd ~/turtle_ws/src
```

### Step 3: Clone the repository

```bash
git clone https://github.com/KSU-Chad/turtle_bringup.git
```
### Step 4: Confirm the structure

```bash
ls turtle_bringup/
```

You should see: `package.xml  resource/  setup.cfg  setup.py  turtle_bringup/`

```bash
ls turtle_bringup/launch/
```

You should see: `turtle_bringup_args.launch.py`

---

Copy the launch file you created in the previous activity into the 'turtle_ws/src/turtle_bringup/launch folder'

```bash
cd
mv launch/turtle_bringup_args.launch.py turtle_ws/src/turtle_bringup/launch/
```

## Part 2 — Build and Source

### Step 5: Build the package

```bash
cd ~/turtle_ws
colcon build
```

You should see output ending in:

```
Starting >>> turtle_bringup
Finished <<< turtle_bringup [...]
Summary: 1 package finished [...]
```

### Step 6: Source the install directory

**This step is required every time you open a new terminal after building.**

```bash
source ~/turtle_ws/install/setup.bash
```

> **Common mistake:** Forgetting to source after building. If `ros2 launch`
> reports "Package 'turtle_bringup' not found", you need to source.

### Step 7: Verify the package is visible

```bash
ros2 pkg list | grep turtle_bringup
```

---

## Part 3 — Launch File 1: Hardcoded Parameters

### Step 7: Launch the system

```bash
ros2 launch turtle_bringup turtle_bringup.launch.py
```

You should see:
- The turtlesim window open with a **blue background**
- A separate xterm window open with the teleop node running

Click the xterm window to give it keyboard focus, then use arrow keys to drive the turtle.

### Step 8: Inspect the running system

In a new terminal (remember to source first):

```bash
# How many nodes are running?
ros2 node list

# What topics exist?
ros2 topic list

# Confirm the background parameters were applied
ros2 param get /sim background_r
ros2 param get /sim background_g
ros2 param get /sim background_b
```

**Questions to answer in your lab notebook:**
1. Run `ros2 node list` while the simulation is running. Write down the node names you see. In the launch file, find the `name=` argument for each node — what does changing that argument appear to do to the node name?
2. Run `ros2 param get /sim background_b`. Write down the value. Now look at the launch file where `background_b` is set. Do the two numbers match?

---

## Part 4 — Launch File 2: Command-Line Arguments

### Step 9: View available arguments without launching

```bash
ros2 launch turtle_bringup turtle_bringup_args.launch.py --show-args
```

You should see the three arguments (`bg_r`, `bg_g`, `bg_b`) with their defaults and descriptions.

### Step 10: Launch with defaults (same blue background)

```bash
ros2 launch turtle_bringup turtle_bringup_args.launch.py
```

### Step 11: Launch with a custom color

Try each of these and observe the simulator background:

```bash
# Red background
ros2 launch turtle_bringup turtle_bringup_args.launch.py bg_r:=255 bg_g:=0 bg_b:=0

# Green background
ros2 launch turtle_bringup turtle_bringup_args.launch.py bg_r:=0 bg_g:=200 bg_b:=0

# Orange background
ros2 launch turtle_bringup turtle_bringup_args.launch.py bg_r:=255 bg_g:=165 bg_b:=0
```

**Question:** What happens if you pass `bg_r:=999`? (Try it.) Write down what you observe.

---

## Part 5 — Concepts Check

Answer these in your lab notebook before leaving:

1. After building the package, open a **new terminal without sourcing** `install/setup.bash` and try to run `ros2 launch turtle_bringup turtle_bringup.launch.py`. Write down the exact error message you get.

2. Look at `turtle_bringup_args.launch.py`. Find the three `DeclareLaunchArgument` blocks. What is the `default_value` for `bg_b`? Now run the launch file without passing any arguments — what color is the background? Do they match?

3. Run `ros2 launch turtle_bringup turtle_bringup_args.launch.py --show-args`. Write down what the output looks like.

4. Remove `prefix='xterm -e'` from your local copy of `turtle_bringup.launch.py`, rebuild, and relaunch. Try using the arrow keys.

5. You used `bg_r:=255 bg_g:=0 bg_b:=0` to get a red background. Without running it first, predict what values would give you a purple background. Then try it and see if you were right.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `Package 'turtle_bringup' not found` | Haven't sourced install | `source ~/turtle_ws/install/setup.bash` |
| `No executable found` | Launch file not installed | Check `data_files` in `setup.py`, rebuild |
| Teleop window opens but arrow keys do nothing | xterm doesn't have focus | Click the xterm window |
| `xterm: command not found` | xterm not installed | `sudo apt install xterm` |
| Background stays grey after setting parameters | turtlesim reads bg params on init only | Kill and relaunch — params can't be hot-reloaded on this node |

---

