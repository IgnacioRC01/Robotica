#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def pose_callback_turtle1(msg):
    rospy.loginfo(f"Tortuga 1 - x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}")

def pose_callback_turtle2(msg):
    rospy.loginfo(f"Tortuga 2 - x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}")

def mostrar_posiciones():
    rospy.init_node('mostrar_posiciones_dos_tortugas', anonymous=True)

    rospy.Subscriber('/turtle1/pose', Pose, pose_callback_turtle1)
    rospy.Subscriber('/turtle2/pose', Pose, pose_callback_turtle2)

    rospy.spin()  # Mantiene el nodo corriendo y escuchando

if __name__ == '__main__':
    try:
        mostrar_posiciones()
    except rospy.ROSInterruptException:
        pass

