#Created by: Kaleb Nails, Erik Liebergall
#Date: 10/6/2023
#from time import sleep
from usbiss.spi import SPI
import opcng as opc
import os
import time
import signal
import subprocess
from datetime import datetime # datetime.now()


#this is a slightly ugly way to make sure the while loops are killed and the program can exit propperly
global DataLoop
global InitializeLoop
InitializeLoop = True
DataLoop = True

# This is to handle interuptions and turn the alphasense
def handle_interrupt(signal, frame):
    global DataLoop
    global InitializeLoop
    print("Ctrl+C pressed. Performing cleanup or other actions...")

    #exits the while loops
    DataLoop = False
    InitializeLoop = False
    time.sleep(.5)
    dev.off()
    print('sensor off')
    exit(0)  # Terminate the script gracefully

signal.signal(signal.SIGINT, handle_interrupt)


#setting up more sensor stuff from the library
spi = SPI('/dev/ttyACM0')
spi.mode = 1
spi.max_speed_hz = 500000
spi.lsbfirst = False

#This loop initializes the sensor and should only run at the start
while InitializeLoop == True:
    try:
        #This detects which model of opc and prints the relevent data
        dev = opc.detect(spi)
        # print(type(dev))
        print(f'device information: {dev.info()}')
        print(f'serial: {dev.serial()}')

        #this just formats the serial number string to look better
        SerialNumberStr = str(dev.serial())
        SerialNumberStr = SerialNumberStr.replace("N3","N3-")
        SerialNumberStr = SerialNumberStr.replace(" ","")

        print(f'firmware version: {dev.serial()}')
        print('sucessfully connected to device')
        break

    except Exception as e:
        print('ERROR connecting to sensor, trying again........')
        print(e)
        time.sleep(1)


#This exits one directory at a time so its on the local computer so you dont get csvs on your repository
os.chdir("..")
os.chdir("..")

#This creates the file and the first row and and the labels
fname = '{0}_Alphasense_{1}.csv'.format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S"), SerialNumberStr)
file = open(fname,'w')
titleStr = 'Serial Number,Date Label, Dates (YMD), Bin 0, Bin 1, Bin 2, Bin 3, Bin 4, Bin 5, Bin 6, Bin 7, Bin 8, Bin 9, Bin 10, Bin 11, Bin 12, Bin 13, Bin 14, Bin 15, Bin 16, Bin 17, Bin 18, Bin 19, Bin 20, Bin 21, Bin 22, Bin 23, Bin1 MToF,Bin3 MToF,Bin5 MToF,Bin7 MToF,Sampling Period,SFR,Temperature,Relative humidity,PM1,PM2.5,PM10,#RejectGlitch,#RejectLongTOF,#RejectRatio,#RejectOutOfRange,Fan rev count,Laser status,Checksum'
file.write(titleStr  +"\n")
file.flush()
dev.on()

#This loop controls data collection
while DataLoop ==True:
    try:
       # query particle mass readings
        time.sleep(1)
        #print(dev.pm())
        recorded_data = dev.histogram()
        #print(recorded_data)

        dataStr = ', {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}'.format(recorded_data.get('Bin 0', ''),recorded_data.get('Bin 1', ''),recorded_data.get('Bin 2', ''),recorded_data.get('Bin 3', ''),recorded_data.get('Bin 4', ''),recorded_data.get('Bin 5', ''),recorded_data.get('Bin 6', ''),recorded_data.get('Bin 7', ''),recorded_data.get('Bin 8', ''),recorded_data.get('Bin 9', ''),recorded_data.get('Bin 10', ''),recorded_data.get('Bin 11', ''),recorded_data.get('Bin 12', ''),recorded_data.get('Bin 13', ''),recorded_data.get('Bin 14', ''),recorded_data.get('Bin 15', ''),recorded_data.get('Bin 16', ''),recorded_data.get('Bin 17', ''),recorded_data.get('Bin 18', ''),recorded_data.get('Bin 19', ''),recorded_data.get('Bin 20', ''),recorded_data.get('Bin 21', ''),recorded_data.get('Bin 22', ''),recorded_data.get('Bin 23', ''),recorded_data.get('Bin1 MToF', ''),recorded_data.get('Bin3 MToF', ''),recorded_data.get('Bin5 MToF', ''),recorded_data.get('Bin7 MToF', ''),recorded_data.get('Sampling Period', ''),recorded_data.get('SFR', ''),recorded_data.get('Temperature', ''),recorded_data.get('Relative humidity', ''),recorded_data.get('PM1', ''),recorded_data.get('PM2.5', ''),recorded_data.get('PM10', ''),recorded_data.get('#RejectGlitch', ''),recorded_data.get('#RejectLongTOF', ''),recorded_data.get('#RejectRatio', ''),recorded_data.get('#RejectOutOfRange', ''),recorded_data.get('Fan rev count', ''),recorded_data.get('Laser status', ''),recorded_data.get('Checksum', ''))

        dateStr =', Date:, {0}'.format(datetime.now())

        print("\n" + SerialNumberStr + dateStr + dataStr + "\n")
        file.write(SerialNumberStr + dateStr + dataStr + "\n")
        file.flush()

    except BaseException as e:
        print(e)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
