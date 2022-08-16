import serial
import time
with serial.Serial('COM3',9600) as arduino:
    while True:
        arduino.write(b'H')
        time.sleep(0.1)
        arduino.write(b'L')
        time.sleep(0.1)
        arduino.write(b'H')
        time.sleep(0.2)
        arduino.write(b'L')
        time.sleep(1)