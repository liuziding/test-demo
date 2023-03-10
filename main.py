import sys

from PySide6.QtWidgets import (QApplication,QPushButton,QVBoxLayout, QLabel, QMenu,
                      QHBoxLayout,QFileDialog,QWidget,QSlider, QScrollArea, QTextEdit,
                      QListWidget, QListWidgetItem, QMainWindow, QMenuBar, QTableWidget)
from PySide6.QtCore import QUrl, Qt, QSize
from PySide6.QtGui import QAction, QColor, QPixmap, QIcon
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

from components.main.topBtnsWidget import TopBtnsWidget
from components.main.contentWidget import ContentWidget
from utils.commonhelper import CommonHelper

class MyMainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.resize(1300, 800)
        self.setMinimumWidth(1300)
        self.setMinimumHeight(800)
        self.setStyleSheet("background-color: red;")

        # 窗口上部分按钮组
        self.top_widget = TopBtnsWidget(self)

        # 窗口下半部分控件
        self.content_widget = ContentWidget(self)

        self.setup_ui()

        # 设置样式
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))
        # 显示窗口
        self.show()

    def setup_ui(self):

        # 中心控件
        centre_widget = QWidget()

        # 中心控件布局 分为上下两部分
        centre_layout = QVBoxLayout()
        centre_layout.setContentsMargins(0, 0, 0, 0)
        centre_layout.setSpacing(0)

        # 绑定信号
        centre_layout.addWidget(self.top_widget)
        centre_layout.addWidget(self.content_widget)

        # 设置中心控件布局
        centre_widget.setLayout(centre_layout)

        # 设置中心控件
        self.setCentralWidget(centre_widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWidget()
    window.setWindowTitle("主窗口")
    sys.exit(app.exec())


