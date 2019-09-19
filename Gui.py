import vpython as vp
from vpython import box, color
import math
from Comms import comms


class gui:
    """This is a class for creating and updating the positioning of an object"""

    def __init__(self):
        self.guiItem = vp.box(pos=vp.vector(0, 0, 0), size=vp.vector(20, 15, 1), color=color.magenta)
        # vp.rate(100)
        self.xOrient = 0
        self.yOrient = 0
        self.zOrient = 0
        self.comm = comms()

    def run(self):
        x, y, z = self.comm.getData()
        self.updateOrientation(x, y, z)

    def updateOrientation(self, x, y, z):
        """Updates the orientation of the object by taking in x, y and z coordinates.

        :parameter
        ----------------
        x : int, Orientation in X-plane \n
        y : int, Orientation in Y-plane \n
        z : int, Orientation in Z-plane

        """
        self.xOrient += self.convertToRadians(x)
        self.yOrient += self.convertToRadians(y)
        self.zOrient += self.convertToRadians(z)

        self.guiItem.rotate(self.convertToRadians(x), vp.vector(0, 1, 0))
        self.guiItem.rotate(self.convertToRadians(y), vp.vector(1, 0, 0))
        self.guiItem.rotate(self.convertToRadians(z), vp.vector(0, 0, 1))

    def convertToRadians(self, i):
        rad = (i / 180) * math.pi
        print(rad)
        if abs(rad) < 0.0009:
            return 0

        return rad


def main():
    print()


if __name__ == "__main__":
    main()
