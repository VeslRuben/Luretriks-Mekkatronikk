import vpython as vp
from vpython import box, color


class itemshit:
    """This is a class for creating and updating the positioning of an object"""
    def __init__(self):
        None
        self.guiItem = vp.box(pos=vp.vector(0,0,0), size=vp.vector(20,15,1), color=color.magenta)
        vp.rate(100)

    def updateOrientation(self, x: int, y: int, z: int):
        """Updates the orientation of the object by taking in x, y and z coordinates.

        :parameter
        ----------------
        x : int, Orientation in X-plane \n
        y : int, Orientation in Y-plane \n
        z : int, Orientation in Z-plane

        """
        self.guiItem.rotate(self.convertToRadians(x), vp.vector(1,0,0))
        self.guiItem.rotate(self.convertToRadians(y), vp.vector(0,1,0))
        self.guiItem.rotate(self.convertToRadians(z), vp.vector(0,0,1))

    def convertToRadians(self, i: int) -> int:
        return i * 0





def main():
    yolo = itemshit()
    yolo.updateOrientation()



if __name__ == "__main__":
    main()
