class MyWord:
    """Summary of class here.

       used to save all the information of text

        Attributes:
           txt: string og the word
           size:the size of text when showing
           position: the position of text in final picture when showing
        """

    def __init__(self):
        self.word = ""
        self.size = 30
        self.maxsize = 30
        self.position = (50, 50)

    def change_size(self, size):
        self.size = self.maxsize * size

    def change_position(self, position):
        self.position = position

    def change_txt(self, txt):
        self.word = txt

    """"
        sign is used to know what attribute to return
        1 for word
        2 for size
        3 for position
        """
    def get(self, sign):
        if sign == 1:
            return self.word
        if sign == 2:
            return self.size
        if sign == 3:
            return self.position

