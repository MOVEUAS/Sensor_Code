from time import sleep
from usbiss.spi import SPI
import opcng as opc
from datetime import datetime # datetime.now()


fname = '{0}_pm25_simplest_CSV.csv'.format(datetime.now().strftime("%Y_%m_%d__%H_%M_%S") )
file = open(fname,'w')
titleStr = ',Date Label, Dates (YMD), Sensor 1, pm10 standard, pm25 standard, pm100 standard, pm10 env, pm25 env, pm100 env,particles 03um, particles 05um, particles 10um, particles 25um, particles 50um, particles 100um, Dates (YMD), Sensor 2, pm10 standard, pm25 standard, pm100 standard, pm10 env, pm25 env, pm100 env,particles 03um, particles 05um, particles 10um, particles 25um, particles 50um, particles 100um'
file.write(titleStr  +"\n")
file.flush()



spi = SPI('/dev/ttyACM0')
spi.mode = 1
spi.max_speed_hz = 500000
spi.lsbfirst = False

dev = opc.detect(spi)

print(f'device information: {dev.info()}')
print(f'serial: {dev.serial()}')
print(f'firmware version: {dev.serial()}')


while True:

    try:
        # power on fan and laser
        dev.on()

        recorded_data = dev.histogram()
        #print(dev.histogram())

        # power off fan and laser
        dev.off()

    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue


    dataStr1 = ', {0}, {1}, {2},    {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}'.format(recorded_data['Bin0'],
    dateStr =', Date:, {0}'.format(datetime.now())
    file.write(dateStr + dataStr + "\n")
    file.flush()




#This is what the bins apparently are:
#_OPC_N3_HISTOGRAM_MODEL = [['Bin 0',              'H'],
#                           ['Bin 1',              'H'],
#                           ['Bin 2',              'H'],
#                           ['Bin 3',              'H'],
#                           ['Bin 4',              'H'],
#                           ['Bin 5',              'H'],
#                           ['Bin 6',              'H'],
#                           ['Bin 7',              'H'],
#                           ['Bin 8',              'H'],
#                           ['Bin 9',              'H'],
#                           ['Bin 10',             'H'],
#                           ['Bin 11',             'H'],
#                           ['Bin 12',             'H'],
#                           ['Bin 13',             'H'],
#                           ['Bin 14',             'H'],
#                           ['Bin 15',             'H'],
#                           ['Bin 16',             'H'],
#                           ['Bin 17',             'H'],
#                           ['Bin 18',             'H'],
#                           ['Bin 19',             'H'],
#                           ['Bin 20',             'H'],
#                           ['Bin 21',             'H'],
#                           ['Bin 22',             'H'],
#                           ['Bin 23',             'H'],
#                           ['Bin1 MToF',          'B'],
#                           ['Bin3 MToF',          'B'],
#                           ['Bin5 MToF',          'B'],
#                           ['Bin7 MToF',          'B'],
#                           ['Sampling Period',    'H'],
#                           ['SFR',                'H'],
#                           ['Temperature',        'H'],
#                           ['Relative humidity',  'H'],
#                           ['PM1',                'f'],
#                           ['PM2.5',              'f'],
#                           ['PM10',               'f'],
#                           ['#RejectGlitch',      'H'],
#                           ['#RejectLongTOF',     'H'],
#                           ['#RejectRatio',       'H'],
#                           ['#RejectOutOfRange',  'H'],
#                           ['Fan rev count',      'H'],
#                           ['Laser status',       'H'],
#                           ['Checksum',           'H']]
