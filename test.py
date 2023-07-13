import serial
import threading
import time
port="/dev/ttyUSB0"#Linux
baudrate=115200
tty=serial.Serial(port=port,baudrate=baudrate,timeout=1)

tty.close()
tty.open()
tty.write("julien\n".encode('utf-8'))

read=tty.readline().decode()#
#read=tty.read(6).decode()
tty.flush()#vide le cache
tty.close()

print(read)





