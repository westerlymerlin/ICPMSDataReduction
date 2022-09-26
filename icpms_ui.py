# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ICPMS.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QToolButton, QWidget)
import main_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1213, 818)
        icon = QIcon()
        icon.addFile(u":/images/iconGTRun.svg", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"font: 9pt \"Arial\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(255, 255, 255, 255));")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 300, 1211, 521))
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.liststdout = QListWidget(self.frame)
        self.liststdout.setObjectName(u"liststdout")
        self.liststdout.setGeometry(QRect(10, 50, 1191, 451))
        self.liststdout.setStyleSheet(u"background-color: rgb(75, 75, 75);\n"
"font: 9pt \"Consolas\";\n"
"color: rgb(119, 198, 1);")
        self.liststdout.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.liststdout.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.liststdout.setMovement(QListView.Static)
        self.btnExit = QPushButton(self.frame)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(1110, 10, 93, 28))
        self.btnExit.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.lbl_console = QLabel(self.frame)
        self.lbl_console.setObjectName(u"lbl_console")
        self.lbl_console.setGeometry(QRect(10, 10, 371, 16))
        self.lbl_console.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.toolSource = QToolButton(Dialog)
        self.toolSource.setObjectName(u"toolSource")
        self.toolSource.setGeometry(QRect(1120, 80, 41, 22))
        self.toolSource.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.label_19 = QLabel(Dialog)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(130, 20, 471, 16))
        self.label_19.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.btnICPMS = QPushButton(Dialog)
        self.btnICPMS.setObjectName(u"btnICPMS")
        self.btnICPMS.setGeometry(QRect(10, 20, 93, 42))
        self.btnICPMS.setStyleSheet(u"background-color: rgb(225, 225, 225);")
        self.label_20 = QLabel(Dialog)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(10, 80, 111, 16))
        self.label_20.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.txtSourceFile = QLineEdit(Dialog)
        self.txtSourceFile.setObjectName(u"txtSourceFile")
        self.txtSourceFile.setGeometry(QRect(130, 80, 961, 22))
        self.txtSourceFile.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"PhD Python Projects - ICPMS Data Reduction", None))
#if QT_CONFIG(tooltip)
        self.liststdout.setToolTip(QCoreApplication.translate("Dialog", u"All console output is logged to pp.log", None))
#endif // QT_CONFIG(tooltip)
        self.btnExit.setText(QCoreApplication.translate("Dialog", u"Exit", None))
        self.lbl_console.setText(QCoreApplication.translate("Dialog", u"Console Output, also logged", None))
        self.toolSource.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"Process ICPMS batch data and create mean and stderr files", None))
        self.btnICPMS.setText(QCoreApplication.translate("Dialog", u"RUN", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"Batch Log (csv)", None))
        self.txtSourceFile.setText(QCoreApplication.translate("Dialog", u"C:\\Users\\garyt\\OneDrive - TS Technologies Ltd\\GTFiles\\PhD\\Samples\\Sample Database\\batchlog.csv", None))
    # retranslateUi

