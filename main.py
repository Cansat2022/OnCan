#!/usr/bin/python
import time
from bmp import readBmp180
import serial

serial_port = serial.Serial(
  port = '/dev/ttyS0',
  baudrate = 19200,
  parity = serial.PARITY_NONE,
  stopbits = serial.STOPBITS_ONE,
  bytesize = serial.EIGHTBITS
)

def main():
  t = 0
  open('output.txt', 'w').write('')
  while 1:
    time.sleep(0.5)
    t += 0.5
    celsius, mbar = readBmp180()
    pa = mbar / 10
    pa = round(pa, 1)
    celsius = round(celsius, 1)

    output = f'{t},{celsius},{pa}\n'

    file = open('output.txt', 'a')
    file.write(output)
    file.close()

    serial_port.write(str.encode(output))
  
if __name__ == "__main__":
  main()