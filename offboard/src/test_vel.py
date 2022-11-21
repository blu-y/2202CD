"""
 * File: offb_node.py
 * Stack and tested in Gazebo 9 SITL
"""

#! /usr/bin/env python3

import rospy
import time
import numpy as np
from geometry_msgs.msg import PoseStamped, TwistStamped
from mavros_msgs.msg import State, xyz
from mavros_msgs.srv import CommandBool, CommandBoolRequest, SetMode, SetModeRequest
from std_msgs.msg import Bool
import matplotlib.pyplot as plt

current_state = State()
cpose = PoseStamped()
x = 0
y = 0
z = 2
arr = 0
traj = [[],[],[],[]]
sig = np.linspace(-6, 6, 10)
xs = 1/(1+np.exp(-sig))
ys = 1/(1+np.exp(-sig))
s = 5

def arrived_cb(msg):
    global arr
    if msg: arr = 1

def state_cb(msg):
    global current_state
    current_state = msg

def cp_cb(msg):
    global x, y, z
    x = msg.x
    y = msg.y
    z = msg.z

def cxyz_cb(msg):
    global cpose
    cpose = msg

if __name__ == "__main__":
    rospy.init_node("pp_control")
    state_sub = rospy.Subscriber("mavros/state", State, callback = state_cb)
    cp_sub = rospy.Subscriber("/pp/checkpoint", xyz, callback = cp_cb)
    arrived_pub = rospy.Publisher("/pp/cp_arr", Bool, queue_size=1)
    final_arr_sub = rospy.Subscriber("/pp/arr", Bool, callback = arrived_cb)
    local_pos_pub = rospy.Publisher("mavros/setpoint_position/local", PoseStamped, queue_size=10)
    vel_pub = rospy.Publisher("mavros/setpoint_velocity/cmd_vel", TwistStamped, queue_size=1)
    local_pos_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, cxyz_cb)
    rospy.wait_for_service("/mavros/cmd/arming")
    arming_client = rospy.ServiceProxy("mavros/cmd/arming", CommandBool)    
    rospy.wait_for_service("/mavros/set_mode")
    set_mode_client = rospy.ServiceProxy("mavros/set_mode", SetMode)
    # Setpoint publishing MUST be faster than 2Hz
    rate = rospy.Rate(20)
    # Wait for Flight Controller connection
    while(not rospy.is_shutdown() and not current_state.connected):
        rate.sleep()
    pose = PoseStamped()
    twist = TwistStamped()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = z
    # Send a few setpoints before starting
    for i in range(100):   
        if(rospy.is_shutdown()):
            break
        local_pos_pub.publish(pose)
        rate.sleep()
    offb_set_mode = SetModeRequest()
    offb_set_mode.custom_mode = 'OFFBOARD'
    arm_cmd = CommandBoolRequest()
    arm_cmd.value = True
    last_req = rospy.Time.now()
    start = time.time()
    while(not rospy.is_shutdown()):
        if(current_state.mode != "OFFBOARD" and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
            if(set_mode_client.call(offb_set_mode).mode_sent == True):
                rospy.loginfo("OFFBOARD enabled")
            last_req = rospy.Time.now()
        else:
            if(not current_state.armed and (rospy.Time.now() - last_req) > rospy.Duration(5.0)):
                if(arming_client.call(arm_cmd).success == True):
                    rospy.loginfo("Vehicle armed")
                last_req = rospy.Time.now()
                start = time.time()
                traj = [[],[],[],[]]
        pose.pose.position.x = 0
        pose.pose.position.y = 0
        pose.pose.position.z = 2
        local_pos_pub.publish(pose)
        x0 = cpose.pose.position.x
        y0 = cpose.pose.position.y
        z0 = cpose.pose.position.z
        traj[0].append(x0)
        traj[1].append(y0)
        traj[2].append(z0)
        traj[3].append(time.time()-start)
        dist = (x-x0)**2+(y-y0)**2+(z-z0)**2
        if time.time()-start > 15: break
        rate.sleep()
    start = time.time()
    traj = [[],[],[],[]]
    x = 1
    y = 1
    p = 3
    d = 1000
    ex = [0]
    ey = [0]
    ez = [0]
    while(not rospy.is_shutdown()):
        ex.append(x-x0)
        ey.append(y-y0)
        ez.append(z-z0)
        twist.twist.linear.x = p*ex[-1]+d*0.05*(ex[-1]-ex[-2])
        twist.twist.linear.y = p*ey[-1]+d*0.05*(ey[-1]-ey[-2])
        print(twist.twist.linear.x, twist.twist.linear.y)
        vel_pub.publish(twist)
        x0 = cpose.pose.position.x
        y0 = cpose.pose.position.y
        z0 = cpose.pose.position.z
        traj[0].append(x0)
        traj[1].append(y0)
        traj[2].append(z0)
        traj[3].append(time.time()-start)
        dist = ex[-1]**2+ey[-1]**2+ez[-1]**2
        if time.time()-start > 15: break
        rate.sleep()
    plt.plot(traj[3], traj[0], label='x')
    plt.plot(traj[3], traj[1], label='y')
    plt.legend()
    plt.show()

# rostopic pub /pp/checkpoint mavros_msgs/xyz "{x: 5, y: 5, z: 2}"
# rostopic echo /pp/cp_arr
# rostopic pub /pp/cp_arr std_msgs/Bool "data: true"





