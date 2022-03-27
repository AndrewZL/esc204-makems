# ESC204 Makems Repository


### Objective
Improve the efficiency of upcycling projects in Ghana through automated bottle pre-processing. Plastic water bottles in good structural condition are commonly used in upcycling projects, such as art installations, plastic-based clothing and composities, and pots. It is often necessary to separate the bottle elements for these projects, for aesthetic reasons or to separate the different plastic types in the bottle, label, and ring/cap. The proposed electromechanical system will increase the efficiency and reduce the laborious nature of this task by autonomously removing bottle caps, rings, and labels.

### Current Requirements
- Microcontroller
    - Photoresistor
    - LED
    - Ultrasonic Sensor
    - Proximity Sensor
    - Stepper Motor and Driver
    - DC Motor (2) and Driver
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
