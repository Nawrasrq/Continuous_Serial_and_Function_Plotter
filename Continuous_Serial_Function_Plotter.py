import numpy as np
import numexpr as exp
import matplotlib.pyplot as plt
import time
import serial

# plots a graph based on serial data per seconds
# port = port the device uses
# bitSpeed = device's data rate in bits per second
# seconds = at what interval in seconds the graph should plot x at, defaults to 1 second
def plotSerial(port, bitSpeed, seconds=1):
    # serial initialization
    try:
        device = serial.Serial(port, bitSpeed, timeout=.1)
    except Exception as error:
        print(error)
        return 0

    # data initialization
    y = np.array([0])
    x = np.array([0])
    data = 0
    secPassed = 0
    
    # graph initialization
    plt.ion()
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)     
    plt.title("Serial Data", fontsize = 20)
    plt.xlabel("X-axis: Seconds")
    plt.ylabel("Y-axis")
    
    try:
        while(True):
            if (device.in_waiting > 0):
                data = int(device.readline().decode('utf-8').rstrip())
                print("At " + str(secPassed) + " seconds, recieved data " + str(data))
                y = np.append(y, data)
            else:
                y = np.append(y, data)
            
            x = np.append(x, secPassed)

            ax.plot(x, y, color = "blue")
            fig.canvas.draw()
            fig.canvas.flush_events()

            secPassed = secPassed + seconds
            time.sleep(seconds)

    except KeyboardInterrupt:
        return 0
#plotSerial("COM3", 9600, 0.5)

# plots a function
# function = the math function represented by a string (ex: "sin(x)*2 + cos(x)*2")
# interval = at what interval the graph should plot x at
# start = what x the graph should start, defaults to 0
# firstPoints = how many points the graph should start with starting from the start var, defaults to 0
def plotFunctions(function, interval, start=0, firstPoints=0):
    # graph initialization
    plt.ion()
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111)
    plt.title("Function: y=" + function, fontsize = 20)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    # data initialization
    x = np.array([])
    count = start

    try:
        if firstPoints != 0:
            for _ in range(start, firstPoints):
                x = np.append(x, count)
                count = count + interval
            y = exp.evaluate(function)
            ax.plot(y, color = "blue")
    except Exception as error:
        print(str(error) + "\n" + "Possible invalid function or value")
        return 0

    try:
        while(True):
            x = np.append(x, count)
            y = exp.evaluate(function)
            ax.plot(y, color = "blue")
            fig.canvas.draw()
            fig.canvas.flush_events()

            count = count + interval

    except KeyboardInterrupt or Exception as error:
        print(error)
        return 0
#plotFunctions("sin(x)", 1, 0, 10)
