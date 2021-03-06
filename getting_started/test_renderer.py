import grid2op
from grid2op.Agent import DoNothingAgent, RandomAgent, MLAgent
from grid2op.Converters import IdToAct
import pdb
env = grid2op.make("case5_example")
# my_agent = DoNothingAgent(env.action_space)
# my_agent = RandomAgent(env.action_space)
my_agent = MLAgent(env.action_space)

all_obs = []
obs = env.reset()
all_obs.append(obs)
reward = env.reward_range[0]
done = False
nb_step = 0
graph_layout =  [(0,0), (0,400), (200,400), (400, 400), (400, 0)]
env.attach_renderer(graph_layout)
while True:
    action = my_agent.act(obs, reward, done)
    obs, reward, done, _ = env.step(action)
    print("Rendering timestep {}".format(nb_step))
    arr_ = env.render()
#     arr_ = env.render(mode="rgb_array")
#     print(arr_.shape)
    if done:
        break
    all_obs.append(obs)
    nb_step += 1
