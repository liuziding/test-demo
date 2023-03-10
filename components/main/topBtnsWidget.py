from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtGui import *
from PySide6.QtCore import QFile, Qt

from utils.commonhelper import CommonHelper
from ..dialog.parameterSettingDialog import ParameterSettingDialog

class TopBtnsWidget(QWidget):
    
    def __init__(self, window):
        super(TopBtnsWidget, self).__init__()
        self.setFixedHeight(36)
        self.setup_ui()

    def setup_ui(self):
        # 加载样式表文件
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))

        # 创建一个新控件，将水平布局设置为其主布局，并将其背景颜色设置为红色
        btn_widget = QWidget(self)
        btn_widget.move(0, 0)
        layout = QHBoxLayout()
        layout.setContentsMargins(8, 0, 0, 0)

        # 显示按钮组
        parameter_setting_button = QPushButton("参数设置")
        increase_video_button = QPushButton("加频")
        decrease_video_button = QPushButton("减频")
        refresh_video_button = QPushButton("刷新")

        # 设置属性
        parameter_setting_button.setObjectName("main_nav_btn")
        increase_video_button.setObjectName("main_nav_btn")
        decrease_video_button.setObjectName("main_nav_btn")
        refresh_video_button.setObjectName("main_nav_btn")

        # 设置按钮手状样式
        parameter_setting_button.setCursor(Qt.PointingHandCursor)
        increase_video_button.setCursor(Qt.PointingHandCursor)
        decrease_video_button.setCursor(Qt.PointingHandCursor)
        refresh_video_button.setCursor(Qt.PointingHandCursor)

        layout.addWidget(parameter_setting_button)
        layout.addSpacing(-10)
        layout.addWidget(increase_video_button)
        layout.addSpacing(-10)
        layout.addWidget(decrease_video_button)
        layout.addSpacing(-10)
        layout.addWidget(refresh_video_button)
        layout.addStretch()

        btn_widget.setLayout(layout)
        layout.setContentsMargins(12, 0, 0, 0)
        btn_widget.setFixedHeight(36)

        # 信号与槽
        parameter_setting_button.clicked.connect(self.parameter_setting_clicked)

    def parameter_setting_clicked(self):
        parameter_setting_dialog = ParameterSettingDialog()
        parameter_setting_dialog.exec()

