import rospy
from mavros_msgs.msg import xyz
rospy.init_node("satellite")
obs_pub = rospy.Publisher("/pp/obs", xyz, queue_size=1)
z = 2
print("*** Obstacle Publisher ***")
while(1):
    print("input 'x y' or '0' to terminate")
    i = input()
    if i =="0":
        break
    else:
        try:
            x, y = i.split()
            x = int(x)
            y = int(y)
            obs_pub.publish(x=x, y=y, z=z)
            print('published')
        except Exception as e:
            print('wrong input:', e)
    