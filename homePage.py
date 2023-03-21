from PySide6.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QGridLayout, QLabel, QVBoxLayout, QSplitter,
                               QMainWindow, QApplication)
from PySide6.QtCore import Signal, QFile, QTimer
from PySide6.QtGui import Qt, QPixmap

from utils.commonhelper import CommonHelper
from components.parameterSetting import ParameterSetting
from components.subLineView import SubLineView
from components.subAreaView import SubAreaView

from ui.ui_home import Ui_home

class HomePage(QMainWindow):
    home_signal = Signal(str)
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_home()
        self.ui.setupUi(self)

        self.setup_ui()

    def setup_ui(self):
        # 加载样式表文件
        file = QFile("qss/app.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll().data().decode('utf-8')

        # 一行有多少列
        self.column_count = 2

        for i in range(0, 4):
            label = QLabel("", self)
            label.setObjectName("main_video_label")
            v_video_layout = QVBoxLayout()
            h_video_layout = QHBoxLayout()
            h_btn_label = QHBoxLayout()
            stop_button = self.MyPushButton("Stop", "main_video_button")
            set_lines_button = self.MyPushButton("Set_Lines", "main_video_button")
            set_area_button = self.MyPushButton("Set_Area", "main_video_button")
            start_button = self.MyPushButton("Start", "main_video_button")
            export_button = self.MyPushButton("Export", "main_video_button")
            detail_button = self.MyPushButton("Detail", "main_video_button")

            stop_button.setStyleSheet(stylesheet)
            set_lines_button.setStyleSheet(stylesheet)
            set_area_button.setStyleSheet(stylesheet)
            start_button.setStyleSheet(stylesheet)
            export_button.setStyleSheet(stylesheet)
            detail_button.setStyleSheet(stylesheet)

            h_btn_label.addStretch()
            h_btn_label.addWidget(stop_button)
            h_btn_label.addWidget(set_lines_button)
            h_btn_label.addWidget(set_area_button)
            h_btn_label.addWidget(start_button)
            h_btn_label.addWidget(export_button)
            h_btn_label.addWidget(detail_button)
            h_btn_label.addStretch()

            self.image_label = QLabel()
            pixmap = QPixmap("images/inside.jpg")
            pixmap_w = pixmap.width()
            pixmap_h = pixmap.height()
            image_w = self.image_label.width()
            image_h = self.image_label.height()
            ratio_w = pixmap_w / image_w
            ratio_h = pixmap_h / image_h
            new_pixmap = None
            if ratio_w > ratio_h:
                new_pixmap = pixmap.scaled((pixmap.width() / ratio_w - 20), (pixmap.height() / ratio_w - 44))
            else:
                new_pixmap = pixmap.scaled((pixmap.width() / ratio_h - 20), (pixmap.height() / ratio_h - 20))
            
            self.image_label.setAlignment(Qt.AlignCenter)
            self.image_label.setPixmap(new_pixmap)
            splitter_H = QSplitter(Qt.Horizontal)
            h_video_layout.addWidget(splitter_H)
            splitter_H.addWidget(self.image_label)

            v_video_layout.addLayout(h_video_layout)
            v_video_layout.addLayout(h_btn_label)

            set_lines_button.clicked.connect(lambda: self.setLinesClicked(i))
            set_area_button.clicked.connect(lambda: self.setAreaClicked(i))
            # detail_button.clicked.connect(lambda: self.detailClicked(i))
            detail_button.clicked.connect(lambda index=i: self.detailClicked(index))

            label.setLayout(v_video_layout)

            self.ui.gl_video_content.addWidget(label, i // self.column_count, i % self.column_count)

        self.show()

    def paramSettingClicked(self): # 点击“参数设置”按钮  信号与槽函数
        parameter_setting = ParameterSetting()
        parameter_setting.exec()
    
    def increaseVideoClicked(self): # 点击“加频”按钮  信号与槽函数
        print("你点击了加频按钮")
    
    def decreaseVideoClicked(self): # 点击“减频”按钮  信号与槽函数
        print("你点击了减频按钮")
    
    def flushedClicked(self): # 点击“刷新”按钮  信号与槽函数
        print("你点击了刷新按钮")
    
    def quitClicked(self): # 点击“退出”按钮  信号与槽函数
        QApplication.quit()

    def detailClicked(self, value): # 点击跳转详情页
        self.home_signal.emit("detailPage")

    def setLinesClicked(self, index): # 点击“Set Lines”按钮  信号与槽函数
        line_win = SubLineView()
        # line_win.line_signal.connect(self.setLine_text)
        line_win.exec()

    def setAreaClicked(self, index): # 点击“Set Area”按钮  信号与槽函数
        area_win = SubAreaView()
        # area_win.area_signal.connect(self.setArea_text)
        area_win.exec()

    def resizeEvent(self, evt):
        if self.image_label:
            timer = QTimer(self)
            timer.setSingleShot(True)  # 设置为单次触发
            timer.timeout.connect(self.showImage)
            timer.start(100)  # 0.1秒后触发

        super().resizeEvent(evt)

    def showImage(self): # 展示图片
        self.image_label.setAlignment(Qt.AlignCenter)
        pixmap = QPixmap("images/inside.jpg")
        pixmap_w = pixmap.width()
        pixmap_h = pixmap.height()
        label_w = self.image_label.width() - 10
        label_h = self.image_label.height() - 10
        ratio_w = pixmap_w / label_w
        ratio_h = pixmap_h / label_h
        if ratio_w > ratio_h:
            new_pixmap = pixmap.scaled((pixmap_w / ratio_w), (pixmap_h / ratio_w))
        else:
            new_pixmap = pixmap.scaled((pixmap_w / ratio_h), (pixmap_h / ratio_h))
            
        self.image_label.setPixmap(new_pixmap)
        


    def MyPushButton(self, text, className):
            btn = QPushButton(text)
            btn.setObjectName(className)
            return btn