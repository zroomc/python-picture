import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QSlider
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from uimain import Ui_mainfome
from PIL import Image, ImageDraw, ImageFont, ImageQt
import traceback
from pympler import tracker
import gc
from UpPicture import UpPicture
from MyWord import MyWord


class App(QWidget, Ui_mainfome):
    BkPath = "back.jpg"
    up_picture = UpPicture()
    txt = MyWord()

    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.buttunforMake.clicked.connect(self.makePicture)
        self.toUpic.clicked.connect(self.addP)
        self.tr = tracker.SummaryTracker()
        # 窗口建立时初始化背景
        if os.path.exists(self.BkPath):
            mpp = QPixmap(self.BkPath)
            self.Bpicture.setPixmap(mpp)
            self.Bpicture.setScaledContents(True)
            self.fontsize.valueChanged[int].connect(self.changeValue)

    def addP(self):

        image, file_type = QFileDialog.getOpenFileName(self, "Image", "", "Image (*.png *.xpm *.jpg)")  # 设置文件扩展名过滤,注意用双分号间隔
        if os.path.exists(image):
            self.up_picture.change_path(image)
            mpp = QPixmap(image)
            self.UPicture.setPixmap(mpp)
            self.UPicture.setScaledContents(True)

    def makePicture(self):
        try:
            self.txt.change_txt(self.EditforText.text())
            img = Image.open(self.BkPath)
            path = self.up_picture.get(1)
            jgz = Image.open(path)
            size = self.Editforsize.text()
            if size != "":
                size = int(size)
                old_size = self.up_picture.get(2)
                new_size = (old_size[0]*size, old_size[1]*size)
                old_jgz = jgz.resize(new_size)
                jgz = old_jgz
                self.up_picture.change_size(int(size))

            img.paste(jgz, self.up_picture.get(3))
            draw = ImageDraw.Draw(img)
            ttfront = ImageFont.truetype("simhei.ttf", self.txt.get(2))
            draw.text((32, 19), self.txt.get(1), fill=(0, 0, 0), font=ttfront)
            img.save(os.path.join("final.jpg"))
            # jj = ImageQt.ImageQt(img)
            # jj.save("final0.jpg")
            # final_picture = QPixmap.fromImage(jj)
            # fpic.save("final00.jpg")
            # self.Lookpicture.setPixmap(QPixmap.fromImage(jj))
            self.Lookpicture.setPixmap(QPixmap("final.jpg"))
            self.Lookpicture.setScaledContents(True)
        except:
            traceback.print_exc()
        # self.tr.print_diff()
        # gc.collect()

    def changeValue(self, value):
        # self.fontsize.setValue(value)
        if self.txt.word == "":
            print("请先输入文字")
        else:
            self.txt.change_size(value)
            self.makePicture()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
