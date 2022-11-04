from Astar import *
import rospy
from mavros_msgs.msg import xyz
from std_msgs.msg import Bool
import time

def arrived_cb(msg):
    global state
    if msg: state = 1

state = 0

def main():
    global state
    goal_arr = 1
    z = 2
    rospy.init_node("pp_planning")
    
    cp_pub = rospy.Publisher("/pp/checkpoint", xyz, queue_size=1)
    arrived_pub = rospy.Subscriber("/pp/cp_arr", Bool, callback = arrived_cb)
    s_start = (5, 5)
    s_goal = (45, 25)

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
        rate.sleep()
    #plot.animation(path, visited, "A*")  # animation

    # path, visited = astar.searching_repeated_astar(2.5)               # initial weight e = 2.5
    # plot.animation_ara_star(path, visited, "Repeated A*")

if __name__ == '__main__':
    main()