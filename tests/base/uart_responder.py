# NANO 1

import time
import board
import busio

uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=0)

UPDATE_INTERVAL = 5
last_time_sent = 0

while True:
    try:
        now = time.monotonic()
        if now - last_time_sent >= UPDATE_INTERVAL:

            # test msg
            temperature = "{:.2f}".format(10.420)
            relative_humidity = "{:.2f}".format(420.69)
            co2_ppm_level = "{:.2f}".format(360.69)
            print("CO2: "+co2_ppm_level+" ,Temperature : "+temperature+" Humidity "+relative_humidity)
            
            uart.write(bytes("<R,"+co2_ppm_level+","+temperature+","+relative_humidity+">", "ascii"))
            
            last_time_sent = now

    except:
        print("smth wrong idk")