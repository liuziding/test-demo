import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # 创建布局
        layout = QVBoxLayout(self)

        # 创建上方边框
        top_frame = QWidget(self)
        top_frame.setObjectName('topFrame')  # 用于设置样式表
        top_frame.setFixedHeight(100)
        top_frame_layout = QVBoxLayout(top_frame)
        layout.addWidget(top_frame)

        # 添加上方边框内的图像
        top_image = QLabel(self)
        top_image.setObjectName('topImage')  # 用于设置样式表
        top_image.setAlignment(Qt.AlignCenter)
        top_pixmap = QPixmap('path_to_top_image')
        top_image.setPixmap(top_pixmap)
        top_frame_layout.addWidget(top_image)

        # 创建下方边框
        bottom_frame = QWidget(self)
        bottom_frame.setObjectName('bottomFrame')  # 用于设置样式表
        bottom_frame.setFixedHeight(120)
        bottom_frame_layout = QVBoxLayout(bottom_frame)
        layout.addWidget(bottom_frame)

        # 添加下方边框内的图像
        bottom_image = QLabel(self)
        bottom_image.setObjectName('bottomImage')  # 用于设置样式表
        bottom_image.setAlignment(Qt.AlignCenter)
        bottom_pixmap = QPixmap('path_to_bottom_image')
        bottom_image.setPixmap(bottom_pixmap)
        bottom_frame_layout.addWidget(bottom_image)

        # 设置布局属性
        layout.setContentsMargins(0, 20, 0, 0)
        layout.setSpacing(0)

        # 设置样式表，以便设置边框颜色和图像大小调整
        self.setStyleSheet('''
            #topFrame, #bottomFrame {
                border: 1px solid gray;
                border-radius: 5px;
            }
            #topImage, #bottomImage {
                max-width: 100%;
                max-height: 100%;
            }
        ''')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
