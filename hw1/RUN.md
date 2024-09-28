Micah Nye, micahn

# Section 2, Question 2:
For Ant-v2 Environment:
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name bc_ant --n_iter 1 --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --video_log_freq -1
```

For Humanoid-v2 Environment:
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name bc_humanoid --n_iter 1 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --video_log_freq -1
```

For Walker2d-v2 Environment:
```
 python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Walker2d.pkl --env_name Walker2d-v2 --exp_name bc_walker2d --n_iter 1 --expert_data rob831/expert_data/expert_data_Walker2d-v2.pkl --video_log_freq -1
```

For Hopper-v2 Environment:
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name bc_hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --video_log_freq -1
```

For HalfCheetah-v2 Environment:
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/HalfCheetah.pkl --env_name HalfCheetah-v2 --exp_name bc_halfcheetah --n_iter 1 --expert_data rob831/expert_data/expert_data_HalfCheetah-v2.pkl --video_log_freq -1
```

# Section 2, Question 3:

For optimized Ant-v2 Environment:
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name bc_ant_opt --n_iter 1 --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --video_log_freq -1 --num_agent_train_steps_per_iter 2000 --eval_batch_size 5000
```

For poorly performing Humanoid-v2 Environment:
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name bc_humanoid_opt --n_iter 1 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --video_log_freq -1 --num_agent_train_steps_per_iter 2000 --eval_batch_size 5000
```

# Section 2, Question 4:

For plots:
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name bc_ant_tuning --n_iter 1 --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --video_log_freq -1 --eval_batch_size 5000 --tuning
```

# Section 3, Question 2:

For **Ant-v2** DAgger & plots:
Make sure to line 160 in rl_trainer.py is uncommented. Line 159 is commented. This is a temporary way to quickly create the plots.
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name dagger_ant --do_dagger --n_iter 10 --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --video_log_freq -1
```

For **Humanoid-v2** DAgger & plots:
Make sure to line 159 in rl_trainer.py is uncommented. Line 160 is commented. This is a temporary way to quickly create the plots.
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name dagger_humanoid --do_dagger --n_iter 10 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --video_log_freq -1
```
