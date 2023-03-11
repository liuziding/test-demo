import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)

        # 创建上下布局管理器
        vbox = QVBoxLayout(self)

        # 创建上面的QWidget对象
        top_widget = QWidget()
        top_widget.setStyleSheet("border: 2px solid black;")
        # top_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.above_label = QLabel()
        self.above_label.setAlignment(Qt.AlignCenter)
        self.above_label.setMinimumSize(1, 1)
        # self.above_label.setStyleSheet("background-color: black;")
        # above_pixmap = QPixmap("inside.jpg").scaled(self.above_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # self.above_label.setPixmap(above_pixmap)
        

        # 创建下面的QWidget对象
        bottom_widget = QWidget()
        bottom_widget.setStyleSheet("border: 1px solid black;")
        # bottom_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.below_label = QLabel()
        self.below_label.setAlignment(Qt.AlignCenter)
        self.below_label.setMinimumSize(1, 1)
        self.below_label.setStyleSheet("background-color: black;")
        belows_pixmap = QPixmap("inside.jpg").scaled(self.below_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.below_label.setPixmap(belows_pixmap)

        vbox.addWidget(self.above_label, stretch=1)
        vbox.addWidget(self.below_label, stretch=1)


        # vbox.addWidget(top_widget, stretch=1)
        # vbox.addWidget(bottom_widget, stretch=1)

        # 创建上面的QWidget对象
        # top_widget = QWidget()
        # top_widget.setStyleSheet("border: 20px solid black;")
        # top_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        
        
        

        # 创建下面的QWidget对象
        # bottom_widget = QWidget()
        # bottom_widget.setStyleSheet("border: 1px solid black;")
        # bottom_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # self.below_label = QLabel()
        # self.below_label.setAlignment(Qt.AlignCenter)
        # self.below_label.setStyleSheet("background-color: black;")
        # belows_pixmap = QPixmap("inside.jpg").scaled(self.below_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        # self.below_label.setPixmap(belows_pixmap)
        # vbox.addWidget(self.above_label)
        # vbox.addWidget(self.below_label)
        

        self.show()

    def resizeEvent(self, evt):
        # 当窗口大小改变时，调用此函数重新计算 QLabel 的大小和位置
        super().resizeEvent(evt)

        # 获取窗口的大小
        size1 = self.above_label.size()
        size3 = self.below_label.size()

        pixmap1 = QPixmap("inside.jpg")
        scaled1 = pixmap1.scaled(size1, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 使用 QPainter 绘制图片，并设置其缩放属性
        pixmap3 = QPixmap('inside.jpg')
        scaled3 = pixmap3.scaled(size3, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 设置 QLabel 的背景颜色和图片
        self.above_label.setStyleSheet("background-color: black;")
        self.above_label.setPixmap(scaled1)
        self.below_label.setStyleSheet("background-color: black;")
        self.below_label.setPixmap(scaled3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
