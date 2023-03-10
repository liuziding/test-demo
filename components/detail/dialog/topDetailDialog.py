from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import QFile, Qt

from utils.commonhelper import CommonHelper

class TopDetailDialog(QWidget):
    def __init__(self, window):
        super(TopDetailDialog, self).__init__()
        self.setFixedHeight(36)
        self.setup_ui()

    def setup_ui(self):
        # 加载样式表文件
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))

        # 创建一个新控件，将水平布局设置为其主布局，并将其背景颜色设置为红色
        btn_widget = QWidget(self)
        btn_widget.setStyleSheet("background: green;")
        btn_widget.move(0, 0)
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 0, 0)

        # 显示按钮组
        parameter_setting_button = QPushButton("参数设置")
        import_video_button = QPushButton("导入视频")
        start_identify_button = QPushButton("开始识别")
        export_video_button = QPushButton("导出结果")
        delete_video_button = QPushButton("删除结果")
        refresh_video_button = QPushButton("刷新")
        return_button = QPushButton("返回")

        # 设置属性
        parameter_setting_button.setObjectName("nav_bar_btn")
        import_video_button.setObjectName("nav_bar_btn")
        start_identify_button.setObjectName("nav_bar_btn")
        export_video_button.setObjectName("nav_bar_btn")
        delete_video_button.setObjectName("nav_bar_btn")
        refresh_video_button.setObjectName("nav_bar_btn")
        return_button.setObjectName("nav_bar_btn")

        # 设置按钮手状样式
        parameter_setting_button.setCursor(Qt.PointingHandCursor)
        import_video_button.setCursor(Qt.PointingHandCursor)
        start_identify_button.setCursor(Qt.PointingHandCursor)
        export_video_button.setCursor(Qt.PointingHandCursor)
        delete_video_button.setCursor(Qt.PointingHandCursor)
        refresh_video_button.setCursor(Qt.PointingHandCursor)
        return_button.setCursor(Qt.PointingHandCursor)

        layout.addWidget(parameter_setting_button)
        layout.addSpacing(-10)
        layout.addWidget(import_video_button)
        layout.addSpacing(-10)
        layout.addWidget(start_identify_button)
        layout.addSpacing(-10)
        layout.addWidget(export_video_button)
        layout.addSpacing(-10)
        layout.addWidget(delete_video_button)
        layout.addSpacing(-10)
        layout.addWidget(refresh_video_button)
        layout.addSpacing(-10)
        layout.addWidget(return_button)
        layout.addStretch()

        btn_widget.setLayout(layout)
        layout.setContentsMargins(12, 0, 0, 0)
        btn_widget.setFixedHeight(36)

