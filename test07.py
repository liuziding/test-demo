from PySide6.QtWidgets import QApplication, QWidget, QLabel, QFrame, QVBoxLayout
from PySide6.QtGui import QPixmap, Qt
import sys

class ImageFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Box)  # 设置框架的形状
        self.setFixedWidth(300)  # 固定宽度
        self.setFixedHeight(200)  # 固定高度

        self.label = QLabel(self)  # 创建标签
        self.label.setAlignment(Qt.AlignCenter)  # 标签居中对齐

        vbox = QVBoxLayout(self)  # 垂直布局管理器
        vbox.addWidget(self.label)  # 添加标签到布局管理器

    def set_image(self, image_path):
        pixmap = QPixmap(image_path)  # 创建pixmap对象
        frame_size = self.size()  # 获取QFrame的大小
        scaled_pixmap = pixmap.scaledToHeight(frame_size.height(), Qt.SmoothTransformation)
        if scaled_pixmap.width() > frame_size.width():
            scaled_pixmap = pixmap.scaledToWidth(frame_size.width(), Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)  # 设置标签的pixmap

        # 设置标签的位置，使其居中
        label_size = self.label.size()
        x = (frame_size.width() - label_size.width()) / 2
        y = (frame_size.height() - label_size.height()) / 2
        self.label.move(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    frame = ImageFrame(window)
    frame.set_image('images/inside.jpg')
    window.show()
    sys.exit(app.exec_())
