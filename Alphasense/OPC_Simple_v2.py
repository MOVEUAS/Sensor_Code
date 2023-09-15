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
    print(dev.pm())

# power off fan and laser
dev.off()