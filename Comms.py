import numpy as np
import serial




class comms:

    def __init__(self):
        # Window size
        self.n = 20

        self.i = 0

        self.xList = [0] * self.n
        self.yList = [0] * self.n
        self.zList = [0] * self.n

        self.ser = serial.Serial('COM8', 19200)

        good = False

        while good == False:
            try:
                info = self.ser.readline()
                info = info[0:len(info) - 2].decode()
                good = True
            except UnicodeDecodeError:
                print('Error')


    def splitData(self, info):
        data = info.split(" ")
        return data

    def saveData(self, x, y, z):
        self.xList[self.i] = x
        self.yList[self.i] = y
        self.zList[self.i] = z

        if self.i == 19:
            self.i = 0

    def movingAverage(self, values, window):
        weights = np.repeat(1.0, window) / window
        sma = np.convolve(values, weights, 'valid')
        return sma

    def getData(self):
        info = self.ser.readline()
        info = info[0:len(info) - 2].decode()
        data = self.splitData(info)
        self.saveData(int(data[0]) / 700, int(data[1]) / 700, int(data[2]) / 700)
        x = self.movingAverage(self.xList, self.n)
        y = self.movingAverage(self.yList, self.n)
        z = self.movingAverage(self.zList, self.n)
        #print('X: ' + str(x[0]))
        #print('Y: ' + str(y[0]))
        #print('Z: ' + str(z[0]))
        return x[0], y[0], z[0]

def main():
    print()


if __name__ == "__main__":
    main()
