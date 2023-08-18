#!/usr/bin/env python

import sys
import rospy
from puzzlebot_dec.hardware_wrap import HardwareWrap 
from puzzlebot_dec.robots import Robots, RobotParam
from puzzlebot_dec.control import Controller, ControlParam
from puzzlebot_dec.behavior_lib import BehaviorLib

if __name__ == "__main__":
    try:
        #  N = int(sys.argv[1])
        N = rospy.get_param("/robot_num")
        hc = HardwareWrap(N)
        hc.setup()
        hc.start()
    except rospy.ROSInterruptException:
        pass
