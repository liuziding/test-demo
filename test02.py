import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        """建立主程序界面"""
        # 创建主窗口中心部件
        centre_widget = QWidget()

        # 创建左、中、右三个部件
        self.left_widget = QListWidget()
        center_widget = QTableWidget()
        right_widget = QTableWidget()

        # 设置左部件列表
        for i in range(5):
            text = f"{i+1}. video video video video video video video video"
            item = QListWidgetItem(text)
            item.setToolTip(text)
            item.setSizeHint(QSize(0, 40))
            self.left_widget.addItem(item)
        
        # self.left_widget.setMaximumWidth(200)
        # self.left_widget.setMaximumHeight(736)
        self.left_widget.setFixedWidth(200)
        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # 设置中部件图片
        self.center_label = QLabel(center_widget)
        # self.center_label.setFixedSize(605, 736)
        self.center_label.setAlignment(Qt.AlignCenter)
        self.center_label.setStyleSheet("background-color: black;")
        center_pixmap = QPixmap("./images/inside.jpg").scaled(self.center_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.center_label.setPixmap(center_pixmap)
        self.center_label.setMinimumSize(1, 1)  # 设置最小大小
        self.center_label.repaint()

        # 设置右边图片
        self.right_label = QLabel(right_widget)
        self.right_label.setFixedWidth(300)
        self.right_label.setAlignment(Qt.AlignCenter)
        self.right_label.setStyleSheet("background-color: black;")
        right_pixmap = QPixmap("./images/inside.jpg").scaled(self.right_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.right_label.setPixmap(right_pixmap)
        self.center_label.setMinimumSize(1, 1)  # 设置最小大小
        self.right_label.repaint()

        # 创建左、中、右三个布局，并将对应部件加入到布局中
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.left_widget)

        right_layout = QVBoxLayout()
        right_layout.addWidget(right_widget)

        # 创建主布局，并将左、中、右三个布局加入到主布局中
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.center_label)
        main_layout.addWidget(self.right_label)

        # 将主布局设置为中心部件的布局
        centre_widget.setLayout(main_layout)

        # 将中心部件设置为主窗口的中心部件
        self.setCentralWidget(centre_widget)

        self.show()

    def resizeEvent(self, evt):
        # 当窗口大小改变时，调用此函数重新计算 QLabel 的大小和位置
        super().resizeEvent(evt)

        # 获取窗口的大小
        size1 = self.center_label.size()
        size3 = self.right_label.size()

        pixmap1 = QPixmap("images/inside.jpg")
        scaled1 = pixmap1.scaled(size1, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 使用 QPainter 绘制图片，并设置其缩放属性
        pixmap3 = QPixmap('images/inside.jpg')
        scaled3 = pixmap3.scaled(size3, Qt.KeepAspectRatio, Qt.SmoothTransformation)



        # 设置 QLabel 的背景颜色和图片
        self.center_label.setStyleSheet("background-color: black;")
        self.center_label.setPixmap(scaled1)
        self.right_label.setStyleSheet("background-color: black;")
        self.right_label.setPixmap(scaled3)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.resize(1500, 800)
    sys.exit(app.exec())