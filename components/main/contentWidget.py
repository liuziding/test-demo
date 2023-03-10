from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from ..line.subLineView import SubLineView
from ..line.subAreaView import SubAreaView

from components.detail.detailDialog import DetailDialog  # ..detailDialog detail.detailDialog import DetailDialog

# 内容部分
class ContentWidget(QWidget):
    def __init__(self, window):
        super(ContentWidget, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)

        # 总的控件个数
        self.widget_list = [{"name": "张三", "age": 18}, {"name": "李四", "age": 19}, {"name": "王五", "age": 20}, {"name": "小六", "age": 21}]
        
        # 一行有多少列
        self.column_count = 2

        self.setup_ui()

    def setup_ui(self):
        self.windowChange()

    def windowChange(self):
        # 加载样式表文件
        file = QFile("qss/app.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll().data().decode('utf-8')

        # 创建一个QWidget来显示QGridLayout
        # self.video_area_widget = QWidget(self)

        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)
        for i in range(0, 4):
            label = QLabel("", self)
            label.setObjectName("main_video_label")
            v_video_layout = QVBoxLayout()
            h_video_layout = QHBoxLayout()
            h_btn_label = QHBoxLayout()
            # h_btn_label.setSpacing(6)
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

            image_label = QLabel()
            pixmap = QPixmap("./images/inside.jpg")
            pixmap_w = pixmap.width()
            pixmap_h = pixmap.height()
            image_w = image_label.width()
            image_h = image_label.height()
            ratio_w = pixmap_w / image_w
            ratio_h = pixmap_h / image_h
            new_pixmap = None
            if ratio_w > ratio_h:
                new_pixmap = pixmap.scaled((pixmap.width() / ratio_w - 20), (pixmap.height() / ratio_w - 44))
            else:
                new_pixmap = pixmap.scaled((pixmap.width() / ratio_h - 20), (pixmap.height() / ratio_h - 20))
            
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setPixmap(new_pixmap)
            # label.setStyleSheet("border: 1px solid red;")
            splitter_H = QSplitter(Qt.Horizontal)
            h_video_layout.addWidget(splitter_H)
            splitter_H.addWidget(image_label)

            v_video_layout.addLayout(h_video_layout)
            v_video_layout.addLayout(h_btn_label)

            set_lines_button.clicked.connect(lambda: self.setLine_clicked(i))
            set_area_button.clicked.connect(lambda: self.setArea_clicked(i))
            detail_button.clicked.connect(lambda: self.detail_clicked(i))

            label.setLayout(v_video_layout)

            grid_layout.addWidget(label, i // self.column_count, i % self.column_count)

        # 将QGridLayout设置为video_area_widget的布局
        self.setLayout(grid_layout)

    def MyPushButton(self, text, className):
            btn = QPushButton(text)
            btn.setObjectName(className)
            return btn
    
    def setLine_clicked(self, index):
        line_win = SubLineView()
        line_win.line_signal.connect(self.setLine_text)
        line_win.exec()

    def setLine_text(self, chosen_line):
        pass

    def setArea_clicked(self, index):
        area_win = SubAreaView()
        area_win.area_signal.connect(self.setArea_text)
        area_win.exec()

    def setArea_text(self):
        pass

    def detail_clicked(self, obj): # 点击按钮进入详情页
        detail_win = DetailDialog()
        detail_win.exec()

    def resizeEvent(self, evt):
        self.windowChange()




