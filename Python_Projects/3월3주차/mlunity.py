import numpy as np
from mlagents_envs.environment import UnityEnvironment

env = UnityEnvironment(file_name="220317_main", seed = 1, side_channels=[])
env.reset()

# behavior_name
agent_prefab = env.get_behavior_names()[0]
print(agent_prefab)

# observation shape, action type, action shape
behavior_parameter_spec = env.get_behavior_spec(behavior_name=agent_prefab)
print(behavior_parameter_spec)

decision_terminal_step = env.get_steps(behavior_name=agent_prefab)
print(decision_terminal_step)
# decision steps
print(decision_terminal_step[0])
# terminal steps
print(decision_terminal_step[1])

# decision steps... 
# action
print(decision_terminal_step[0].action_mask[0])
# observation
print(decision_terminal_step[0].obs[0])



# print(decision_terminal_step[0].action_mask(0))

# print(decision_terminal_step[0].action_mask[0:][0][0])
# print(env.set_actions(behavior_name=agent_prefab[0], action=decision_terminal_step[0].action_mask[0][0:][0]))
