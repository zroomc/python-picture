from PIL import Image


class UpPicture:
    """Summary of class here.

           used to set all attribution of upper picture

            Attributes:
               txt:  path of the image
               maxsize: the standard of bigger or smaller
               size:the size of image when showing
               position: the position of image in final picture when showing
            """

    def __init__(self):

        self.path = ""
        self.position = (73, 42)
        self.maxsize = 30
        self.mine_size = [30, 30]
        self.size = self.mine_size

    def change_size(self, size):
        self.size[0] = self.mine_size[0]*size
        self.size[1] = self.mine_size[1]*size

    def change_position(self, position):
        self.position = position

    def change_path(self, up_picture):
        self.path = up_picture

    """"
            sign is used to know what attribute to return
            1 for path
            2 for size
            3 for position
            """
    def get(self, sign):
        if sign == 1:
            return self.path
        if sign == 2:
            return self.size
        if sign == 3:
            return self.position

