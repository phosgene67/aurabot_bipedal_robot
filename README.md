# MjLab AuraBot

AuraBot is a two-wheeled biped robot trained with reinforcement learning to follow commanded forward and angular velocities while balancing and resisting disturbances. The environments use the MjLab framework and MuJoCo physics. The project repository is [phosgene67/mjlab_aurabot](https://github.com/phosgene67/mjlab_aurabot).

## Install

Install the [uv package manager](https://docs.astral.sh/uv/getting-started/installation/#installation-methods), then run:

```
uv sync
```

## Run the pre-trained agent

Run the agent in an MjLab environment (GPU required):

```
uv run play Mjlab-Velocity-AuraBot --checkpoint-file logs/rsl_rl/aurabot_velocity/bests/default.pt
```

Or run the same exported ONNX policy in the CPU-compatible MuJoCo simulation:

```
uv run python sim.py
```
uv run python sim.py `
  --onnx-model-path logs/rsl_rl/aurabot_bird_pose/2026-09-07_23-55-43/2026-09-07_23-55-43.onnx
  
Keyboard controls in the MuJoCo simulation:

- Up/Down: increase/decrease forward velocity
- Left/Right: increase/decrease angular velocity
- Space: reset commanded velocities to zero

## Train an agent

Test the environment with a simple agent:

```
uv run play Mjlab-Velocity-AuraBot --agent zero
uv run play Mjlab-Velocity-AuraBot --agent random
```

Train with 2,048 parallel environments:

```
uv run train Mjlab-Velocity-AuraBot --env.scene.num-envs 2048
```

Train the new mode-conditioned policy:

```
uv run train Mjlab-Mode-AuraBot --env.scene.num-envs 1000
```

This policy receives the target leg pose as part of its observation and trains
on both the normal and bird poses. Its checkpoints are saved under
`logs/rsl_rl/aurabot_mode_conditioned/`.

Training outputs are saved under `logs/rsl_rl/aurabot_velocity/`. Play a checkpoint with:

```
uv run play Mjlab-Velocity-AuraBot --checkpoint-file [path-to-checkpoint]
```
uv run play Mjlab-Velocity-AuraBot --checkpoint-file logs/rsl_rl/aurabot_bird_pose/2026-09-07_23-55-43/model_5000.pt

## Project layout

- `src/mjlab_aurabot/tasks/aurabot_velocity_env_cfg.py`: RL environment, rewards, curriculum, and PPO configuration.
- `src/mjlab_aurabot/robot/aurabot/`: MuJoCo robot model and assets.
- `src/mjlab_aurabot/robot/aurabot_kinematics.py`: differential-drive wheel kinematics.
- `sim.py`: standalone MuJoCo + ONNX policy playback.

Run a trained mode-conditioned ONNX policy with `M` to switch between poses:

```
uv run python sim.py --mode-model-path logs/rsl_rl/aurabot_mode_conditioned/[run]/[model].onnx
```
