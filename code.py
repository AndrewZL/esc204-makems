"""
Main Code for Widget Lab 3
"""

import board
import microcontroller
import digitalio
import pwmio

from adafruit_motor import stepper
import adafruit_hcsr04

import time
from utils.init import init_dc, init_stepper

import json


def grasp():
    # continuously run and adjust grasp intensity based on encoder values
    # once hit good encoder range, run cap off
    # once cap off is complete, run release
    print('grasping')
    def cap_off():
        pass
    pass


def release():
    pass


if __name__ == '__main__':

    with open('config.json', 'r') as file:
        config = json.load(file)

    # Initialize DC Motor Grasp
    in1_grasp, in2_grasp, ena_grasp = init_dc(eval(config['grasp']['dir1_pin']), eval(config['grasp']['dir2_pin']), eval(config['grasp']['ena_pin']))
    
    # Initialize DC Motor Load
    in1_load, in2_load, ena_load = init_dc(board.D4, board.D5, board.D6)

    # Initialize Stepper Motor Cap Removal
    # note: 200 is the number of steps per revolution, TODO: put all of this into config later
    step_pin, dirn_pin = init_stepper(board.D2, board.D3, 0.005, 200)

    # Initialize Sensing
    prox_sensor = adafruit_hcsr04.HCSR04(eval(config['ultrasonic']['trig_pin']), eval(config['ultrasonic']['echo_pin']))

    # Main Loop
    while True:
        print(prox_sensor.distance)
        # while bottle is not present
        if prox_sensor.distance > config['presence_thresh']:
            continue
        else: # bottle is present and close enough to grasp
            grasp()
        time.sleep(1)
        
        