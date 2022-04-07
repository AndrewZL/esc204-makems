    
from grasp import GraspModule
import board 
import time 

grasper = GraspModule()


speed = 50000
grasper.in1.value, grasper.in2.value = (True, False)
grasper.ena.duty_cycle = speed
for i in range(0,100):
    print(grasper.encoder.position, speed)
    time.sleep(0.25)
    if i / 4 == i / 4.0:
        speed = speed - 500
        grasper.ena.duty_cycle = speed
