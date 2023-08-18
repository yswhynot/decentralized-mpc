#!/usr/bin/env python

import sys
import rospy
from puzzlebot_dec.hardware_planner import HardwarePlanner
from puzzlebot_dec.robots import Robots, RobotParam
from puzzlebot_dec.control import Controller, ControlParam
from puzzlebot_dec.behavior_lib import BehaviorLib

if __name__ == "__main__":
    try:
        N = rospy.get_param("/robot_num")
        eth = 1.5e-3
        dt = 0.1
        r_param = RobotParam(L=5e-2, anchor_base_L=8e-3, anchor_L=1.5e-2)
        c_param = ControlParam(vmax=0.06, wmax=2.0,
                        uvmax=1.0, uwmax=5.0,
                        mpc_horizon=3, constr_horizon=3, eth=eth)
        c = Controller(N, dt, c_param)
        rsys = Robots(N, c, robot_param=r_param, eth=eth, pilot_ids=[0])
        hp = HardwarePlanner(N, c_param, c, rsys)
        hp.start()
    except rospy.ROSInterruptException:
        pass
