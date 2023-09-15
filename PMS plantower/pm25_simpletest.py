# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
#
# Adafruit PM2.5 device, which is Plantower PMS5003 PM sensor:
#   https://learn.adafruit.com/pm25-air-quality-sensor/python-and-circuitpython
#   https://docs.circuitpython.org/projects/pm25/en/latest/api.html#adafruit-pm25-uart
# Original pm25_simpletest.py:
#   https://github.com/adafruit/Adafruit_CircuitPython_PM25/blob/main/examples/pm25_simpletest.py
#
# Adafruit product: https://www.adafruit.com/product/3686
# Plantower PMS5003 Datasheet: https://cdn-shop.adafruit.com/product-files/3686/plantower-pms5003-manual_v2-3.pdf
#
# Erik Liebergall, lieberg@my.erau.edu
# Leah Smith, smithl73@my.erau.edu
# Kaleb Nails, nailsk@my.erau.edu
# Marc Compere, comperem@erau.edu
# created : 10 Feb 2023
# modified: 06 Apr 2023

"""
Example sketch to connect to PM2.5 sensor with either I2C or UART.
"""

# pylint: disable=unused-import
import time
import board
import busio
from datetime import datetime # datetime.now()
from digitalio import DigitalInOut, Direction, Pull
#from adafruit_pm25.i2c import PM25_I2C


reset_pin = None
# If you have a GPIO, its not a bad idea to connect it to the RESET pin
# reset_pin = DigitalInOut(board.G0)
# reset_pin.direction = Direction.OUTPUT
# reset_pin.value = False


# For use with a computer running Windows:
# import serial
# uart = serial.Serial("COM30", baudrate=9600, timeout=1)

# For use with microcontroller board:
# (Connect the sensor TX pin to the board/computer RX pin)
# uart = busio.UART(board.TX, board.RX, baudrate=9600)

# For use with Raspberry Pi/Linux:
# import serial
# uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)

# For use with USB-to-serial cable:
import serial

dev1='/dev/ttyUSB1'
dev2='/dev/ttyUSB2'

uart = serial.Serial(dev1, baudrate=9600, timeout=0.25)
uart2 = serial.Serial(dev2, baudrate=9600, timeout=0.25)

# Connect to a PM2.5 sensor over UART
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)
pm25_2 = PM25_UART(uart2, reset_pin)

# Create library object, use 'slow' 100KHz frequency!
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
# Connect to a PM2.5 sensor over I2C
#pm25 = PM25_I2C(i2c, reset_pin)
fname = '{0}_pm25_simplest_CSV.csv'.format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S") )
file = open(fname,'w')
                                           
print("Found PM2.5 sensor, reading data...")

while True:
    time.sleep(1)

    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
    print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
    print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
    print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
    print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
    print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
    print("---------------------------------------")


# while False:
    time.sleep(1)

    try:
        aqdata2 = pm25_2.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue

    print()
    print("Concentration Units (standard)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata2["pm10 standard"], aqdata2["pm25 standard"], aqdata2["pm100 standard"])
    )
    print("Concentration Units (environmental)")
    print("---------------------------------------")
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata2["pm10 env"], aqdata2["pm25 env"], aqdata2["pm100 env"])
    )
    print("---------------------------------------")
    print("Particles2 > 0.3um / 0.1L air:", aqdata2["particles 03um"])
    print("Particles2 > 0.5um / 0.1L air:", aqdata2["particles 05um"])
    print("Particles2 > 1.0um / 0.1L air:", aqdata2["particles 10um"])
    print("Particles2 > 2.5um / 0.1L air:", aqdata2["particles 25um"])
    print("Particles2 > 5.0um / 0.1L air:", aqdata2["particles 50um"])
    print("Particles2 > 10 um / 0.1L air:", aqdata2["particles 100um"])
    print("---------------------------------------")
    
    dateStr =', Date:, {0}'.format(datetime.now())
    #dataStr1 = ', Data1:, {0}, {1}, {2}, {3}, {4}, {5}'.format(aqdata["particles 03um"],aqdata["particles 05um"],aqdata["particles 10um"],aqdata["particles 25um"],aqdata["particles 50um"],aqdata["particles 100um"])
    #dataStr2 = ', Data2:, {0}, {1}, {2}, {3}, {4}, {5}'.format(aqdata2["particles 03um"],aqdata2["particles 05um"],aqdata2["particles 10um"],aqdata2["particles 25um"],aqdata2["particles 50um"],aqdata2["particles 100um"])
    
    dataStr1 = ', Data1:, {0}, {1}, {2},    {3}, {4}, {5},    {6}, {7}, {8}, {9}, {10}, {11}'.format( \
                    aqdata["pm10 standard"],       \
                    aqdata["pm25 standard"],       \
                    aqdata["pm100 standard"],      \
                     
                    aqdata["pm10 env"],            \
                    aqdata["pm25 env"],            \
                    aqdata["pm100 env"],           \
                    
                    aqdata["particles 03um"],      \
                    aqdata["particles 05um"],      \
                    aqdata["particles 10um"],      \
                    aqdata["particles 25um"],      \
                    aqdata["particles 50um"],      \
                    aqdata["particles 100um"])
                     
    dataStr2 = ', Data2:, {0}, {1}, {2},    {3}, {4}, {5},    {6}, {7}, {8}, {9}, {10}, {11}'.format( \
                    aqdata2["pm10 standard"],      \
                    aqdata2["pm25 standard"],      \
                    aqdata2["pm100 standard"],     \
                    
                    aqdata2["pm10 env"],           \
                    aqdata2["pm25 env"],           \
                    aqdata2["pm100 env"],          \
                    
                    aqdata2["particles 03um"],     \
                    aqdata2["particles 05um"],     \
                    aqdata2["particles 10um"],     \
                    aqdata2["particles 25um"],     \
                    aqdata2["particles 50um"],     \
                    aqdata2["particles 100um"])
    file.write(dateStr + dataStr1 + dataStr2 + "\n")
    file.flush()


























