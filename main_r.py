import time
import board
import busio
from scan import ScanModule

# This is the Responder - the Nano

uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=0)
UPDATE_INTERVAL = 5
last_time_sent = 0

scan = ScanModule()

detection = False

while True:
    dist = scan.get_distance()
    now = time.monotonic()
    if dist < 10 and detection and now - last_time_sent >= UPDATE_INTERVAL:
        print("<present>")
        uart.write(bytes("present", "ascii"))
        break
    if dist < 10:
        detection = True
    time.sleep(0.1)

time.sleep(10)

while True:
    byte_read = uart.read(1)
    if byte_read is None:
        continue
    else:
        break

# do scanning crap
print('hello')



