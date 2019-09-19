import serial


def test():
    from time import sleep
    ser = serial.Serial('COM7', 9600)  # Establish the connection on a specific port
    counter = 32  # Below 32 everything in ASCII is gibberish
    while True:
        print(ser.readline())



def main():
    print()
    test()


if __name__ == "__main__":
    main()
