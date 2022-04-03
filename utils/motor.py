import board
import digitalio
import pwmio
from adafruit_motor import stepper

class motor:
    def __init__ (self, dir1_pin, dir2_pin, en_pin, default_dir='CW'):
        self.in1 = digitalio.DigitalInOut(dir1_pin)
        self.in2 = digitalio.DigitalInOut(dir2_pin)

        self.in1.direction = digitalio.Direction.OUTPUT
        self.in2.direction = digitalio.Direction.OUTPUT
        # TODO: check these directions lol
        if default_dir == 'CW':
            self.in1.value = True
            self.in2.value = False
        else: 
            self.in1 = False
            self.in2.value = True

        self.enable = pwmio.PWMOut(en_pin, duty_cycle = 0)


def spin(self,clockwise=True, speed=50000):
    self.in1.value, self.in2.value = (clockwise, not clockwise)
    self.enable.duty_cycle = speed

def stop(self):
    self.enable.duty_cycle = 0