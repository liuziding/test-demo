# homepage.py

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from utils.commonhelper import CommonHelper
from components.home.dialog.parameterSetting import ParameterSetting
from components.home.line.subLineView import SubLineView
from components.home.line.subAreaView import SubAreaView

# 顶部按钮组部分
class TopHomeWidget(QWidget):

    def __init__(self):
        super(TopHomeWidget, self).__init__()
        self.setFixedHeight(36)
        self.setupUi()

    def setupUi(self):
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
        parameter_setting_dialog = ParameterSetting()
        parameter_setting_dialog.exec()

# 下面内容部分
class ContentHomeWidget(QWidget):
    inner_home_signal = Signal(str)
    def __init__(self):
        super(ContentHomeWidget, self).__init__()
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
            detail_button.clicked.connect(lambda: self.content_signal(i))

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

    def resizeEvent(self, evt):
        self.windowChange()

    def content_signal(self, param):
        self.inner_home_signal.emit("homePage")

    

class HomePage(QMainWindow):
    home_signal = Signal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.resize(1500, 800)
        self.setMinimumWidth(1500)
        self.setMinimumHeight(800)

        # 中心控件
        self.home_widget = QWidget()
        # 窗口上部分按钮组
        self.top_home_widget = TopHomeWidget()
        # 窗口下部分内容
        self.content_home_widget = ContentHomeWidget()
        self.content_home_widget.inner_home_signal.connect(self.switch_detail_page)

        self.setup_ui()

        # 设置样式
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))

    def setup_ui(self):
        # 中心控件布局 分为上下两部分
        home_layout = QVBoxLayout()
        home_layout.setContentsMargins(0, 0, 0, 0)
        home_layout.setSpacing(0)

        # 绑定信号
        home_layout.addWidget(self.top_home_widget)
        home_layout.addWidget(self.content_home_widget)

        # 设置中心控件布局
        self.home_widget.setLayout(home_layout)

        # 设置中心控件
        self.setCentralWidget(self.home_widget)

    def switch_detail_page(self):
        self.home_signal.emit("homePage")










        # Create a label to show the homepage content
        # self.label = QLabel('This is the homepage')

        # # Create a vertical layout and add the label to it
        # layout = QVBoxLayout()
        # layout = QVBoxLayout()
        # btn11 = QPushButton("按钮")
        # layout.addWidget(btn11)
        # layout.addWidget(self.label)

        # # Set the layout for the widget
        # self.setLayout(layout)

        # btn11.clicked.connect(self.switch_detail_page)

    # def switch_detail_page(self):
    #     self.home_signal.emit("homePage")

