from Astar import *
import rospy
from mavros_msgs.msg import xyz
from std_msgs.msg import Bool
import time

def arrived_cb(msg):
    global state
    if msg: state = 1

state = 0
path = []
s_start = (1, 1)
s_goal = (45, 25)

def add_obs_cb(msg):
    global state, path, s_start, s_goal
    rospy.loginfo("Obstacle added ("+str(msg.x)+", "+str(msg.y))
    astar = AStar(s_start, s_goal)
    astar.obs.add((msg.ox, msg.oy))
    path, visited = astar.searching()

def main():
    global state, path, s_start, s_goal
    goal_arr = 1
    z = 2
    rospy.init_node("pp_planning")
    cp_pub = rospy.Publisher("/pp/checkpoint", xyz, queue_size=1)
    arr_pub = rospy.Publisher("/pp/arr", Bool, queue_size=1)
    arrived_sub = rospy.Subscriber("/pp/cp_arr", Bool, callback = arrived_cb)
    add_obs_sub = rospy.Subscriber("/pp/obs", xyz, callback = add_obs_cb)

    astar = AStar(s_start, s_goal)
    #plot = plotting.Plotting(s_start, s_goal)
    path, visited = astar.searching()
    print(path)
    rate = rospy.Rate(20)
    while(not rospy.is_shutdown()):
        try:
            if state:
                x, y = path.pop()
                print(x, y)
                cp_pub.publish(x=x, y=y, z=z)
                state = 0
                time.sleep(2)
        except: 
            if goal_arr:
                print("goal arrived")
                goal_arr = 0
                arr_pub.publish(True)
                break
        rate.sleep()
    #plot.animation(path, visited, "A*")  # animation

    # path, visited = astar.searching_repeated_astar(2.5)               # initial weight e = 2.5
    # plot.animation_ara_star(path, visited, "Repeated A*")

if __name__ == '__main__':
    main()
