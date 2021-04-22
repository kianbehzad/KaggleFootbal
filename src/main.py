from kaggle_environments import make

env = make("football", debug=True)
output = env.run(["run_right", "do_nothing"])[-1]
print('Left player: reward = %s, status = %s, info = %s' % (output[0]['reward'], output[0]['status'], output[0]['info']))
print('Right player: reward = %s, status = %s, info = %s' % (output[1]['reward'], output[1]['status'], output[1]['info']))
# env.render(mode="human", width=800, height=600)