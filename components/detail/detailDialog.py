import sys

from PySide6.QtWidgets import (QApplication,QPushButton,QVBoxLayout, QLabel, QMenu, QDialog,
                      QHBoxLayout,QFileDialog,QWidget,QSlider, QScrollArea, QTextEdit,
                      QListWidget, QListWidgetItem, QMainWindow, QMenuBar, QTableWidget)
from PySide6.QtCore import QUrl, Qt, QSize
from PySide6.QtGui import QAction, QColor, QPixmap
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

from utils.commonhelper import CommonHelper
from components.detail.dialog.topDetailDialog import TopDetailDialog

class DetailDialog(QDialog):
    def __init__(self):
        super(DetailDialog, self).__init__()

        self.setWindowTitle("详情窗口")
        self.resize(1500, 860)
        self.setMinimumWidth(1500)
        self.setMinimumHeight(860)
        self.setStyleSheet("border: 2px solid red;")

        #窗口上部分按钮组
        self.top_detail_widget = TopDetailDialog(self)

        # 窗口下半部分控件
        # self.content_detail_widget = QWidget(self) # ContentDetailDialog(self)

        self.setup_ui()

        # 设置样式
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))

    def setup_ui(self):

        # 中心控件
        centre_widget = QWidget(self)
        # centre_layout = QHBoxLayout()
        # btn1 = QPushButton("按钮")
        # centre_layout.addWidget(btn1)
        # centre_widget.setLayout(centre_layout)
        centre_widget.setStyleSheet("background: red;")

        # 中心控件布局 分为上下两部分
        centre_layout = QVBoxLayout()
        centre_layout.setContentsMargins(0, 0, 0, 0)
        centre_layout.setSpacing(0)

        # 绑定信号
        centre_layout.addWidget(self.top_detail_widget)
        # centre_layout.addWidget(self.content_detail_widget)

        # 设置中心控件布局
        centre_widget.setLayout(centre_layout)

        # 设置中心控件
        # self.setCentralWidget(centre_widget)
        centre_widget.setParent(self)

        


        