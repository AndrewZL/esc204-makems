import board
import digitalio
import pwmio

from adafruit_motor import stepper
import adafruit_hcsr04

import time
from utils.init import init_dc, init_stepper

import yaml


def grasp():
    # continuously run and adjust grasp intensity based on encoder values
    # once hit good encoder range, run cap off
    # once cap off is complete, run release
    def cap_off():
        pass
    pass


def release():
    pass


if __name__ == '__main__':

    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
    
    # Initialize DC Motor Grasp
    # in1_grasp, in2_grasp, ena_grasp = init_dc(config['grasp']['dir1_pin'], config['grasp']['dir2_pin'], config['grasp']['ena_pin'])
    in1_grasp, in2_grasp, ena_grasp = init_dc(board.D7, board.D8, board.D11)
    
    # Initialize DC Motor Load
    in1_load, in2_load, ena_load = init_dc(board.D4, board.D5, board.D6)

    # Initialize Stepper Motor Cap Removal
    # note: 200 is the number of steps per revolution, TODO: put all of this into config later
    step_pin, dirn_pin = init_stepper(board.D2, board.D3, 0.005, 200)

    # Initialize Sensing
    prox_sensor = adafruit_hcsr04.HCSR04(trigger_pin=board.GP2, echo_pin=board.GP3)

    # Main Loop
    while True:
        # while bottle is not present
        if prox_sensor.distance > config['presence_thresh']:
            continue
        else:
            # while bottle is present but farther than threshold
            while config['presence_thresh'] > prox_sensor.distance > config['prox_thresh']:
                ena_load.duty_cycle = config['load_speed']
            # bottle is present and close enough to grasp
            grasp()
            
        
        
        