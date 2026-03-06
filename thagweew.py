import time, math
import browserbotics as bb

bb.addGroundPlane()

fixedBase = False # try setting to False to see the robot walk
robot = bb.loadURDF(
        'spot.urdf', position=[0, 0, 0.75], fixedBase=fixedBase
)
front_left_hip_joint_id = 1
front_left_knee_joint_id = 2
front_right_hip_joint_id = 4
front_right_knee_joint_id = 5
rear_left_hip_joint_id = 7
rear_left_knee_joint_id = 8
rear_right_hip_joint_id = 10
rear_right_knee_joint_id = 11


i = 0
tau = 8
hip_pos_base = 1
knee_pos_base = -1.8
hip_swing_magn = 0.5
knee_swing_magn = 0.8
front_back_phase_delay = math.pi/2
while True:
        hip_pos_front = hip_pos_base + hip_swing_magn * math.sin(i / tau)
        knee_pos_front = knee_pos_base + knee_swing_magn * math.cos(i / tau)
        for ji in [front_left_hip_joint_id, front_right_hip_joint_id]:
                bb.setJointMotorControl(
                        robot, ji, targetPosition=hip_pos_front
                )
        for ji in [front_left_knee_joint_id, front_right_knee_joint_id]:
                bb.setJointMotorControl(
                        robot, ji, targetPosition=knee_pos_front
                )

        hip_pos_rear = hip_pos_base + hip_swing_magn * math.sin(i / tau + front_back_phase_delay)
        knee_pos_rear = knee_pos_base + knee_swing_magn * math.cos(i / tau + front_back_phase_delay)
        for ji in [rear_left_hip_joint_id, rear_right_hip_joint_id]:
                bb.setJointMotorControl(
                        robot, ji, targetPosition=hip_pos_rear
                )
        for ji in [rear_left_knee_joint_id, rear_right_knee_joint_id]:
                bb.setJointMotorControl(
                        robot, ji, targetPosition=knee_pos_rear
                )

        time.sleep(0.01)
        i += 1
