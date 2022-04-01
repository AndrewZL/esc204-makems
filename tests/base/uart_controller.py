# PI 0

import board
import busio

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

message_started = False

while True:
    byte_read = uart.read(1)
    if byte_read is None:
        continue
    
    if byte_read == b"<":
        message = []
        message_started = True
        continue

    if message_started:
        if byte_read == b">":
            message_parts = "".join(message).split(",")
            message_type = message_parts[0]
            message_started = False            
            if message_parts[0] == "R":
                co2=message_parts[1]
                temperature=message_parts[2]
                humidity=message_parts[3]
                print(f"CO2 {co2}")
                print(f"T {temperature}")
                print(f"H {humidity}")
        else:
            message.append(chr(byte_read[0]))