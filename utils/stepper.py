import board
import digitalio
import pwmio
from adafruit_motor import stepper

# to do: double check this...works
class motor:
    def __init__ (self, mstep_pin1, mstep_pin2, mstep_pin3, step_pin, dir_pin, delay, steps, default_dir='CW'):
    self.step = digitalio.DigitalInOut(step_pin)
    self.dirn = digitalio.DigitalInOut(dir_pin)
        
    self.step.direction = digitalio.Direction.OUTPUT
    self.dirn.direction = digitalio.Direction.OUTPUT

    if default_dir == 'CW':
        self.dirn.value = False
    else:
        self.dirn.value = True
    
    self.microstep_pins = (digitalio.DigitalInOut(mstep_pin1),digitalio.DigitalInOut(mstep_pin2),digitalio.DigitalInOut(mstep_pin3))

# these need updating
def spin(self,clockwise=True, speed=50000):
    self.in1.value, self.in2.value = (clockwise, not clockwise)
    self.enable.duty_cycle = speed

def stop(self):
    self.enable.duty_cycle = 0