from time import sleep
from usbiss.spi import SPI
import opcng as opc

spi = SPI('/dev/ttyACM0')
spi.mode = 1
spi.max_speed_hz = 500000
spi.lsbfirst = False

dev = opc.detect(spi)

print(f'device information: {dev.info()}')
print(f'serial: {dev.serial()}')
print(f'firmware version: {dev.serial()}')

# power on fan and laser
dev.on()

for i in range(10):
    # query particle mass readings
    sleep(1)
    #print(dev.pm())
    print(dev.histogram())

# power off fan and laser
dev.off()



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
