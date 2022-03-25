import time
import board
import analogio


photoresistor_pin = board.GP26_A0
photoresistor = analogio.AnalogIn(photoresistor_pin)

ADC_HIGH = 65535
ADC_REF = photoresistor.reference_voltage


def adc_to_voltage(adc_value):
    return  ADC_REF * (float(adc_value)/float(ADC_HIGH)) * 100

while True:
    print((adc_to_voltage(photoresistor.value,)))    
    time.sleep(0.5)