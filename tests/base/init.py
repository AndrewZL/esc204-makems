import time
import board
import digitalio

pir = digitalio.DigitalInOut(board.GP1)
pir.direction = digitalio.Direction.INPUT


def main():
    pass

if __name__ == '__main__':
    while True:
        pir_value = pir.value
        if pir_value:
            main()
    
