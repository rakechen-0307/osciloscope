import time
import matplotlib.pyplot as plt
from drawnow import *
import serial
import keyboard

val = []
cnt = 0
count = 0

port = serial.Serial('COM19', 2000000, timeout=0.5)
plt.ion()


def makefig():
    plt.ylim(0, 1.5)
    plt.title('Osciloscope')
    plt.grid(True)
    plt.ylabel('ADC outputs')
    plt.plot(val, 'ro-', label='Channel 0')
    plt.legend(loc='lower right')


time.sleep(2)
while port.inWaiting():
    value = port.readline()
start_time = time.time()

# while (time.time() - start_time < 30):
while True:
    port.write(b's')
    if (port.inWaiting()):
        value = port.readline()
        value = value[0:-2]
        number = float(value)
        val.append(float(number))
        count = count + 1
    else:
        val.append(0)

    cnt = cnt + 1

    drawnow(makefig)

    if keyboard.is_pressed('1'):
        break
    if cnt > 50:
        val.pop(0)

print("total count : " + str(count))
