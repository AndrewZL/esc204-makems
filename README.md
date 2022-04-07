# ESC204 Makems Repository


### Objective
Improve the efficiency of upcycling projects in Ghana through automated bottle pre-processing. Plastic water bottles in good structural condition are commonly used in upcycling projects, such as art installations, plastic-based clothing and composities, and pots. It is often necessary to separate the bottle elements for these projects, for aesthetic reasons or to separate the different plastic types in the bottle, label, and ring/cap. The proposed electromechanical system will increase the efficiency and reduce the laborious nature of this task by autonomously removing bottle caps, rings, and labels.

### Current Requirements
The sensors implemented for this repository are noted in brackets.


- 2 Microcontrollers with UART Compatibility (2x RP2040, Raspberry Pi Pico and Arduino Nano Connect)
    - Note that we follow the  "controller/responder" convention for serial communication  
- Scanning Module
    - Photoresistor and LED Array (5x W/Y, R, G, and B); or Camera
    - Short-Distance Distance Sensor (Ultrasonic)
    - Stepper Motor and Driver (A4998)
    - Mini Stepper Motor; or Servo Motor
- Grasping Module
    - Distance Sensor (Ultrasonic)
    - Stepper Motor and Driver (A4998)
    - DC Motor and Driver (L298n)
- Alignment Module
    - DC Motor and Driver (L298n)
- CircuitPython
- Adafruit MicroPython libraries for the above hardware
- Numpy
- Matplotlib

### Folder Structure
- tests
    - base: functions for key components
    - hardware: widget lab code to test whether hardware is working
- utils
    - mesh: 3D plotting, reconstruction from ultrasonic data by solids of revolution, and surface grid to mesh conversion    
    - init: board object and attribute initialization
- config.json: pin map and constants/thresholds
- align.py, grasp.py, scan.py
    - classes that implement the desired functionality for each subsystem
- main_c.py, main_r.py
    - main loops for the controller and responder microcontrollers respectively
