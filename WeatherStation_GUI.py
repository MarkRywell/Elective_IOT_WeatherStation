import time
import datetime
import sqlite3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count
from tkinter import *
# DHT11
import Adafruit_DHT
# BMP180
import bmpsensor
# Light GY-30
import smbus

dbname = 'test.db'
sampleFreq = 1  # time in seconds ==> Sample each 1 min


# get data from DHT sensor
def getDHTdata():
    DHT11Sensor = Adafruit_DHT.DHT11
    DHTpin = 4
    hum, temp = Adafruit_DHT.read_retry(DHT11Sensor, DHTpin)
    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp, 1)
    return temp, hum


# log sensor data on database
def logData(temp, hum, light, pressure):
    conn = sqlite3.connect(dbname)
    curs = conn.cursor()
    curs.execute("INSERT INTO testTable values(datetime('now'), ?, ?)", (temp, hum))
    conn.commit()
    conn.close()


# Light Sensor
# Define some constants from the datasheet

DEVICE = 0x23  # Default device I2C address

POWER_DOWN = 0x00  # No active state
POWER_ON = 0x01  # Power on
RESET = 0x07  # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

# bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1


def convertToNumber(data):
    # Simple function to convert 2 bytes of data
    # into a decimal number. Optional parameter 'decimals'
    # will round to specified number of decimal places.
    result = (data[1] + (256 * data[0])) / 1.2
    return (result)


def readLight(addr=DEVICE):
    # Read data from I2C interface
    data = bus.read_i2c_block_data(addr, ONE_TIME_HIGH_RES_MODE_1)
    return convertToNumber(data)


def getPressure():
    pressure = bmpsensor.readBmp180()
    if (pressure is not None):
        return pressure[1]


temp = getDHTdata()
current_time = datetime.datetime.now()

x = []
y_light = []
y_temp = []
y_hum = []
y_pressure = []
counter = count(0, 1)

fig, ax = plt.subplots(2, 3, constrained_layout=True)
fig.suptitle("Weather Station IOT")
ax[1][1].set_title("Humidity")
ax[0][0].set_title("Light")
ax[0][1].set_title("Pressure")
ax[1][0].set_title("Temperature")


def displayData(i):
    ax[1][1].plot(x, y_hum)
    ax[0][0].plot(x, y_light)
    ax[0][1].plot(x, y_pressure)
    ax[1][0].plot(x, y_temp)

    idx = next(counter)
    x.append(idx)
    yLight = readLight()
    yTemp, yHum = getDHTdata()
    yPressure = getPressure()

    y_temp.append(int(yTemp))
    y_light.append(int(yLight))
    y_hum.append(yHum)
    y_pressure.append(yPressure)
    plt.cla()

    if (len(x) == 20):
        x.pop(0)
        y_temp.pop(0)
        y_light.pop(0)
        y_hum.pop(0)
        y_pressure.pop(0)


def onAll():
    ani = animation.FuncAnimation(fig=fig, func=displayData, interval=1000)
    plt.show()


window = Tk()
window.title("ELECTIVE PROJECT")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("300x300")
window.resizable(0, 0)

# ==========================FRAME=====================
title = Frame(window, bd=10, bg='green', relief=FLAT, width=100, height=100)
title.pack(side=TOP)
body = Frame(window, bd=10, width=400, height=1400, relief=RAISED)
body.pack(anchor=CENTER, pady=100)

# =========================LABEL=========================
titleLabel = Label(title, text="ELECTIVE PROJECT", font=("Arial", 20), fg='blue', width=100)
titleLabel.pack()

# =========================BUTTONS======================
tempButton = Button(body, text="Show Data", font=('Arial', 20, "bold"), command=onAll, fg='blue', width=50)
tempButton.pack()