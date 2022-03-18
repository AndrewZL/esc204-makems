'''
ESC204 2022W Widget Lab 2, Part 10
Task: Take readings using an ultrasonic sensor.
'''

# Import libraries needed for blinking the LED
import board
import digitalio
import time

# Configure the GPIO input and output for the sensor
trigger = digitalio.DigitalInOut(board.GP2)
trigger.direction = digitalio.Direction.OUTPUT
echo = digitalio.DigitalInOut(board.GP3)
echo.direction = digitalio.Direction.INPUT
echo.pull = digitalio.Pull.UP


def capture_echo(timeout):
    #initialize data array and counter
    data = []
    i = 0

    # wait for echo from sound bouncing back and timeout if not seen
    while(not(echo.value) and not(i == timeout)):
        i+=1

    # if timeout reached, no data collection
    if i == timeout:
        print('timeout!')

    # if timeout not reached, then keep collecting data while echo is nonzero
    else:
        while(echo.value):
            data.append((1,))

    return data

def plot_data(data):
    # plot points with pauses in between to avoid overloading
    for point in data:
        print(point)
        time.sleep(0.01)

while True:
    points = capture_echo(1000)
    if(len(points) > 0):
        plot_data(points)

    # print a low value and wait a second to avoid overloading
    print((0.001,))
    time.sleep(1.0)

