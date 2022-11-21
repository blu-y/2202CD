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
x0, y0 = (-1, -1)

def add_obs_cb(msg):
    global state, path, s_start, s_goal, astar
    rospy.loginfo("Obstacle added ("+str(msg.x)+", "+str(msg.y))
    if (msg.x, msg.y) in path:
        astar = AStar(s_start, s_goal)
        astar.obs.add((msg.x, msg.y))
        path, visited = astar.searching()
        path = simplepath(path)
        print('new path : ',path)
    else: astar.obs.add((msg.x, msg.y))

def simplepath(path):
    l = len(path)
    od = 0
    dpath = [(0, 0)]
    for i in range(l-1):
        dpath.append((path[i+1][0]-path[i][0],path[i+1][1]-path[i][1]))
    for i in range(l-1):
        if dpath[i] == dpath[i+1]: path[i] = path[i-1]
    return path

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
    path = simplepath(path)
    print(path)
    rate = rospy.Rate(20)
    while(not rospy.is_shutdown()):
        try:
            if state:
                x, y = path.pop()
                if (x, y) != (x0, y0):
                    print(x, y)
                    cp_pub.publish(x=x, y=y, z=z)
                    state = 0
                    time.sleep(0.1)
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
