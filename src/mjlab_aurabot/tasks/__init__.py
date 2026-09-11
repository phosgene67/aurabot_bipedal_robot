from mjlab.tasks.registry import register_mjlab_task

from .aurabot_velocity_env_cfg import (
    aurabot_velocity_env_cfg,
    AuraBotVelocityRlCfg,
    aurabot_mode_env_cfg,
    AuraBotModeRlCfg,
)

from mjlab.tasks.velocity.rl.runner import VelocityOnPolicyRunner

register_mjlab_task(
    task_id="Mjlab-Velocity-AuraBot",
    env_cfg=aurabot_velocity_env_cfg(),
    play_env_cfg=aurabot_velocity_env_cfg(play=True),
    rl_cfg=AuraBotVelocityRlCfg,
    runner_cls=VelocityOnPolicyRunner,
)

register_mjlab_task(
    task_id="Mjlab-Mode-AuraBot",
    env_cfg=aurabot_mode_env_cfg(),
    play_env_cfg=aurabot_mode_env_cfg(play=True),
    rl_cfg=AuraBotModeRlCfg,
    runner_cls=VelocityOnPolicyRunner,
)
