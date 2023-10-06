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


    # dataStr1 = ', {0}, {1}, {2},    {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}'.format(recorded_data['Bin0'],
    # dateStr =', Date:, {0}'.format(datetime.now())


        dataStr = ', {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17}, {18}, {19}, {20}, {21}, {22}, {23}, {24}, {25}, {26}, {27}, {28}, {29}, {30}, {31}, {32}, {33}, {34}, {35}, {36}, {37}, {38}, {39}, {40}, {41}, {42}, {43}, {44}, {45}, {46}, {47}, {48}, {49}, {50}, {51}, {52}, {53}'.format(
                recorded_data.get('Bin 0', ''),
                recorded_data.get('Bin 1', ''),
                recorded_data.get('Bin 2', ''),
                recorded_data.get('Bin 3', ''),
                recorded_data.get('Bin 4', ''),
                recorded_data.get('Bin 5', ''),
                recorded_data.get('Bin 6', ''),
                recorded_data.get('Bin 7', ''),
                recorded_data.get('Bin 8', ''),
                recorded_data.get('Bin 9', ''),
                recorded_data.get('Bin 10', ''),
                recorded_data.get('Bin 11', ''),
                recorded_data.get('Bin 12', ''),
                recorded_data.get('Bin 13', ''),
                recorded_data.get('Bin 14', ''),
                recorded_data.get('Bin 15', ''),
                recorded_data.get('Bin 16', ''),
                recorded_data.get('Bin 17', ''),
                recorded_data.get('Bin 18', ''),
                recorded_data.get('Bin 19', ''),
                recorded_data.get('Bin 20', ''),
                recorded_data.get('Bin 21', ''),
                recorded_data.get('Bin 22', ''),
                recorded_data.get('Bin 23', ''),
                recorded_data.get('Bin1 MToF', ''),
                recorded_data.get('Bin3 MToF', ''),
                recorded_data.get('Bin5 MToF', ''),
                recorded_data.get('Bin7 MToF', ''),
                recorded_data.get('Sampling Period', ''),
                recorded_data.get('SFR', ''),
                recorded_data.get('Temperature', ''),
                recorded_data.get('Relative humidity', ''),
                recorded_data.get('PM1', ''),
                recorded_data.get('PM2.5', ''),
                recorded_data.get('PM10', ''),
                recorded_data.get('#RejectGlitch', ''),
                recorded_data.get('#RejectLongTOF', ''),
                recorded_data.get('#RejectRatio', ''),
                recorded_data.get('#RejectOutOfRange', ''),
                recorded_data.get('Fan rev count', ''),
                recorded_data.get('Laser status', ''),
                recorded_data.get('Checksum', '')
        )

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
