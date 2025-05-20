#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def mover_dos_tortugas():
    rospy.init_node('mover_dos_tortugas', anonymous=True)

    # Publishers para turtle1 y turtle2
    pub1 = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    pub2 = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz

    # Movimiento de turtle1
    cmd1 = Twist()
    cmd1.linear.x = 1.0
    cmd1.angular.z = 1.0

    # Movimiento de turtle2
    cmd2 = Twist()
    cmd2.linear.x = 1.0
    cmd2.angular.z = -1.0

    while not rospy.is_shutdown():
        pub1.publish(cmd1)
        pub2.publish(cmd2)
        rate.sleep()

if __name__ == '__main__':
    try:
        mover_dos_tortugas()
    except rospy.ROSInterruptException:
        pass

chmod +x ~/Robotica/src/turtle_control/scripts/move_turtle_HW.py
rosrun turtle_control move_turtle_HW.py