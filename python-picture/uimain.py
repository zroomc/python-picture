# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uimain.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainfome(object):
    def setupUi(self, mainfome):
        mainfome.setObjectName("mainfome")
        mainfome.resize(1012, 834)
        self.textBack = QtWidgets.QLabel(mainfome)
        self.textBack.setGeometry(QtCore.QRect(110, 120, 101, 81))
        self.textBack.setMinimumSize(QtCore.QSize(72, 15))
        self.textBack.setLineWidth(1)
        self.textBack.setIndent(-1)
        self.textBack.setObjectName("textBack")
        self.Editforsize = QtWidgets.QLineEdit(mainfome)
        self.Editforsize.setGeometry(QtCore.QRect(430, 340, 113, 31))
        self.Editforsize.setObjectName("Editforsize")
        self.Editforpo = QtWidgets.QLineEdit(mainfome)
        self.Editforpo.setGeometry(QtCore.QRect(430, 440, 113, 31))
        self.Editforpo.setObjectName("Editforpo")
        self.Bpicture = QtWidgets.QLabel(mainfome)
        self.Bpicture.setGeometry(QtCore.QRect(20, 20, 291, 261))
        self.Bpicture.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.Bpicture.setText("")
        self.Bpicture.setPixmap(QtGui.QPixmap("../../../Pic/background.jpg"))
        self.Bpicture.setScaledContents(True)
        self.Bpicture.setWordWrap(False)
        self.Bpicture.setObjectName("Bpicture")
        self.UPicture = QtWidgets.QLabel(mainfome)
        self.UPicture.setGeometry(QtCore.QRect(20, 300, 301, 291))
        self.UPicture.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.UPicture.setText("")
        self.UPicture.setObjectName("UPicture")
        self.TextforUp = QtWidgets.QLabel(mainfome)
        self.TextforUp.setGeometry(QtCore.QRect(130, 420, 101, 81))
        self.TextforUp.setMinimumSize(QtCore.QSize(72, 15))
        self.TextforUp.setLineWidth(1)
        self.TextforUp.setIndent(-1)
        self.TextforUp.setObjectName("TextforUp")
        self.buttunforMake = QtWidgets.QPushButton(mainfome)
        self.buttunforMake.setGeometry(QtCore.QRect(280, 680, 141, 71))
        self.buttunforMake.setObjectName("buttunforMake")
        self.TextforUpsize = QtWidgets.QLabel(mainfome)
        self.TextforUpsize.setGeometry(QtCore.QRect(330, 340, 101, 31))
        self.TextforUpsize.setMinimumSize(QtCore.QSize(72, 15))
        self.TextforUpsize.setLineWidth(1)
        self.TextforUpsize.setIndent(-1)
        self.TextforUpsize.setObjectName("TextforUpsize")
        self.TextforUp_3 = QtWidgets.QLabel(mainfome)
        self.TextforUp_3.setGeometry(QtCore.QRect(340, 430, 101, 61))
        self.TextforUp_3.setMinimumSize(QtCore.QSize(72, 15))
        self.TextforUp_3.setLineWidth(1)
        self.TextforUp_3.setIndent(-1)
        self.TextforUp_3.setObjectName("TextforUp_3")
        self.Lookpicture = QtWidgets.QLabel(mainfome)
        self.Lookpicture.setGeometry(QtCore.QRect(560, 210, 441, 421))
        self.Lookpicture.setStyleSheet("background-color: rgb(212, 237, 255);")
        self.Lookpicture.setText("")
        self.Lookpicture.setObjectName("Lookpicture")
        self.Textfortop = QtWidgets.QLabel(mainfome)
        self.Textfortop.setGeometry(QtCore.QRect(740, 170, 101, 31))
        self.Textfortop.setMinimumSize(QtCore.QSize(72, 15))
        self.Textfortop.setLineWidth(1)
        self.Textfortop.setIndent(-1)
        self.Textfortop.setObjectName("Textfortop")
        self.Textfortext = QtWidgets.QLabel(mainfome)
        self.Textfortext.setGeometry(QtCore.QRect(470, 80, 101, 31))
        self.Textfortext.setMinimumSize(QtCore.QSize(72, 15))
        self.Textfortext.setLineWidth(1)
        self.Textfortext.setIndent(-1)
        self.Textfortext.setObjectName("Textfortext")
        self.EditforText = QtWidgets.QLineEdit(mainfome)
        self.EditforText.setGeometry(QtCore.QRect(552, 70, 431, 41))
        self.EditforText.setObjectName("EditforText")
        self.toUpic = QtWidgets.QPushButton(mainfome)
        self.toUpic.setGeometry(QtCore.QRect(370, 530, 93, 28))
        self.toUpic.setObjectName("toUpic")
        self.label = QtWidgets.QLabel(mainfome)
        self.label.setGeometry(QtCore.QRect(481, 140, 81, 20))
        self.label.setObjectName("label")
        self.fontsize = QtWidgets.QSlider(mainfome)
        self.fontsize.setGeometry(QtCore.QRect(620, 140, 160, 22))
        self.fontsize.setMinimum(1)
        self.fontsize.setMaximum(10)
        self.fontsize.setOrientation(QtCore.Qt.Horizontal)
        self.fontsize.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.fontsize.setTickInterval(1)
        self.fontsize.setObjectName("fontsize")
        self.Editforsize.raise_()
        self.Editforpo.raise_()
        self.Bpicture.raise_()
        self.textBack.raise_()
        self.UPicture.raise_()
        self.TextforUp.raise_()
        self.buttunforMake.raise_()
        self.TextforUpsize.raise_()
        self.TextforUp_3.raise_()
        self.Lookpicture.raise_()
        self.Textfortop.raise_()
        self.Textfortext.raise_()
        self.EditforText.raise_()
        self.toUpic.raise_()
        self.label.raise_()
        self.fontsize.raise_()

        self.retranslateUi(mainfome)
        QtCore.QMetaObject.connectSlotsByName(mainfome)

    def retranslateUi(self, mainfome):
        _translate = QtCore.QCoreApplication.translate
        mainfome.setWindowTitle(_translate("mainfome", "我的表情包神器"))
        self.textBack.setText(_translate("mainfome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">背景</span></p><p><span style=\" font-size:16pt; font-weight:600;\">图片</span></p></body></html>"))
        self.TextforUp.setText(_translate("mainfome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">上方</span></p><p><span style=\" font-size:16pt; font-weight:600;\">图片</span></p></body></html>"))
        self.buttunforMake.setText(_translate("mainfome", "生成"))
        self.TextforUpsize.setText(_translate("mainfome", "大小调整(%)："))
        self.TextforUp_3.setText(_translate("mainfome", "角度："))
        self.Textfortop.setText(_translate("mainfome", "<html><head/><body><p><span style=\" font-weight:600;\">预览图</span></p></body></html>"))
        self.Textfortext.setText(_translate("mainfome", "插入文字："))
        self.toUpic.setText(_translate("mainfome", "选择照片"))
        self.label.setText(_translate("mainfome", "大小(倍数)："))

