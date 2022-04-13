from utils.init import init_dc, init_stepper
import json
import time
import board
from adafruit_motor import stepper
import adafruit_hcsr04
import rotaryio

ccw = True

class GraspModule:
    
    def __init__(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
    
        # Initialize DC Motor Grasp
        self.in1, self.in2, self.ena = init_dc(eval(config['grasp']['dir1_pin']), eval(config['grasp']['dir2_pin']), eval(config['grasp']['ena_pin']))
        self.ena.duty_cycle = 0
        # Initialize Stepper Motor Cap Removal
        # note: 200 is the number of steps per revolution, TODO: put all of this into config later
        self.step, self.step_dirn = init_stepper(eval(config['cap_removal']['direction_pin']),eval(config['cap_removal']['step_pin']))

        # Initialize Sensing
        # self.prox = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

        # Initialize Encoder
        self.encoder = rotaryio.IncrementalEncoder(eval(config['grasp']['encoder_a']), eval(config['grasp']['encoder_b']))
        self.last_position = 0

    def ping(self):
        print("ping!")
    
    def dostep(self):
        """
        Sends a pulse to the STEP output to actuate the stepper motor through one step.
        """
        # pulse high to drive step
        self.step.value = True
        time.sleep(0.05)

        # bring low in between steps
        self.step.value = False
        time.sleep(0.05)

    # grasp
    def close(self, target_speed):
        time_running = 0
        self.in1.value, self.in2.value = (True, False)
        self.ena.duty_cycle = target_speed
        self.last_position = self.encoder.position
        time.sleep(0.05) # give time for motor to come to speed
        target_encoder_speed = self.encoder.position - last_position 
        # units in encoder are not necessarily units in pwm control, so we can't compare the two. 
        # this assumes that initially, a good speed is attainable
        # if the jam is right away, this method produces garbage
        while True: 
            speed = self.encoder.position - self.last_position
            if speed < target_encoder_speed * 0.01:
                break
            self.last_position = self.encoder.position
            
            print(self.encoder.position, speed)
            time.sleep(0.05)

            # Mostly for testing - if the motor runs too long, we want to stop
            time_running = time_running + 0.05
            if time_running > 2:
                break
        self.ena.duty_cycle = 0 # stop the motor when we're done

    def open(self):
        # We want to open it all the way - the last_position variable records how much it had to close
        self.in1.value, self.in2.value = (False, True)
        self.ena.duty_cycle = 5000
        while(self.last_position - self.encoder.position > 0):
            time.sleep(0.05)
        self.ena.duty_cycle = 0

    # removal
    def remove(self):
        self.step_dirn = ccw
        for j in range(1, 5):
            for i in range(1,200):
                self.dostep()
            print(j, "rev complete")
        
        time.sleep(1)
    
    def done_remove(self):
        self.step.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        self.ena.duty_cycle = 5000
        time.sleep(1)
    
    # sensing
    def get_distance(self):
        return self.prox.distance
    

   