import numpy as np

time_intervals = np.array([3,6,9,4,3])
vertical_positions = np.array([33,44,12,34,24])  


delta_vertical_position = np.diff(vertical_positions)

delta_time = np.diff(time_intervals)

average_velocity = delta_vertical_position / delta_time

print("Average Velocity:", average_velocity)
