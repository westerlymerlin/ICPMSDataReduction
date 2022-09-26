from PySide6.QtWidgets import *
from app_settings import *
import sys
from os import path, mkdir
from icpms_ui import Ui_Dialog
from ICPMS_Cruncher import get_icpms_data
import logging
from logging.handlers import RotatingFileHandler


class StdRedirector:
    def __init__(self):
        self.data = []

    def write(self, s):
        app.processEvents()
        if len(s) > 1:
            logger.info(s)
            dialog.liststdout.addItem(s)
            dialog.liststdout.scrollToBottom()


class Mainform(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnExit.clicked.connect(runappexit)
        self.btnICPMS.clicked.connect(runicpms)
        self.toolSource.clicked.connect(self.choose_source_file)  # tiff to stl
        self.txtSourceFile.setText(settings['batchfilepath'])
        self.lbl_console.setText('Console output is also found at: %s%s.log'
                                 % (settings['logging']['logfilepath'], settings['logging']['logappname']))

    def choose_source_file(self):
        filename = QFileDialog.getOpenFileName(self, 'Batchlog file', dialog.txtSourceFile.text(), 'batchlog.csv')
        dialog.txtSourceFile.setText(filename[0])
        settings['batchfilepath'] = filename[0]


def runicpms():
    # icpmsloader.py
    get_icpms_data(dialog.txtSourceFile.text())


def runappexit():
    writesettings()
    print('Exit button pressed')
    app.quit()


if path.isdir(settings['logging']['logfilepath']) is False:
    mkdir(settings['logging']['logfilepath'])
logger = logging.getLogger(settings['logging']['logappname'])
logger.setLevel(logging.INFO)
logfilename = '%s%s.log' % (settings['logging']['logfilepath'], settings['logging']['logappname'])
LogFile = RotatingFileHandler(logfilename, maxBytes=1048576, backupCount=10)
formatter = logging.Formatter('%(asctime)s, %(name)s, %(levelname)s : %(message)s')
LogFile.setFormatter(formatter)
logger.addHandler(LogFile)
sys.stdout = x = StdRedirector()
app = QApplication(sys.argv)
dialog = Mainform()
print("********************** Starting ICPMS Data Reduction Version %s ***********************" % version)
dialog.show()
sys.exit(app.exec())
