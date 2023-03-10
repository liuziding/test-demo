# detailpage.py

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from utils.commonhelper import CommonHelper
from components.detail.dialog.parameterSetting import ParameterSetting

# 顶部按钮组部分
class TopDetailWidget(QWidget):
    inner_detail_signal = Signal(str)
    def __init__(self):
        super(TopDetailWidget, self).__init__()
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

        # 信号与槽
        parameter_setting_button.clicked.connect(self.parameter_setting_clicked)
        return_button.clicked.connect(lambda: self.content_signal("homePage"))

    def parameter_setting_clicked(self):
        parameter_setting_dialog = ParameterSetting()
        parameter_setting_dialog.exec()

    def content_signal(self, param):
        self.inner_detail_signal.emit("detailPage")

class ContentDetailWidget(QWidget):
    def __init__(self):
        super(ContentDetailWidget, self).__init__()
        self.setupUi() # 建立主界面

    def setupUi(self):
        """建立主程序界面"""
        # 创立主窗口中心部件
        centre_widget = QWidget()

        # 创建左、中、右三个部件
        self.left_widget = QListWidget()
        middle_widget = QTableWidget()
        self.right_widget = QTableWidget()

        # 设置左部件列表
        for i in range(5):
            text = f"{i+1}. video video video video video video video video"
            item = QListWidgetItem(text)
            item.setToolTip(text)
            item.setSizeHint(QSize(0, 40))
            self.left_widget.addItem(item)
        
        self.left_widget.setMaximumWidth(200)
        self.left_widget.setMaximumHeight(736)
        self.left_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # 设置中部件图片
        self.center_label = QLabel(middle_widget)
        self.center_label.setFixedSize(605, 736)
        self.center_label.setAlignment(Qt.AlignCenter)
        self.center_label.setStyleSheet("background-color: black;")
        center_pixmap = QPixmap("./images/inside.jpg").scaled(self.center_label.size(), aspectMode=Qt.KeepAspectRatio)
        self.center_label.setPixmap(center_pixmap)
        self.center_label.repaint()

        # 设置右边图片
        self.right_label = QLabel(self.right_widget)
        self.right_label.setFixedSize(605, 736)
        self.right_label.setAlignment(Qt.AlignCenter)
        self.right_label.setStyleSheet("background-color: black;")
        right_pixmap = QPixmap("./images/inside.jpg").scaled(self.right_label.size(), aspectMode=Qt.KeepAspectRatio)
        self.right_label.setPixmap(right_pixmap)
        self.right_label.repaint()

        # 创建左、中、右三个布局，并将对应部件加入到布局中
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.left_widget)

        right_layout = QVBoxLayout()
        right_layout.addWidget(self.right_widget)

        # 创建主布局，并将左、中、右三个布局加入到主布局中
        main_layout = QHBoxLayout()
        main_layout.addLayout(left_layout)
        main_layout.addWidget(self.center_label)
        main_layout.addWidget(self.right_label)

        # 将主布局设置为中心部件的布局
        centre_widget.setLayout(main_layout)

        # 将中心部件设置为主窗口的中心部件
        # self.setCentralWidget(centre_widget)

        # 点击列表item，颜色改变
        # self.left_widget.itemClicked.connect(self.handle_item_clicked)

        # 将显示菜单栏的函数绑定到 QListWidget 的 customContextMenuRequested 信号
        # self.left_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.left_widget.customContextMenuRequested.connect(self.show_menu_clicked)

    def handle_item_clicked(self, item):
        # 获取项目所在的列
        column = self.left_widget.row(item) + 1
        # 如果之前已经有某一行被点击了，则将其背景色还原为白色
        for i in range(self.left_widget.count()):
            current_item = self.left_widget.item(i)
            if current_item.background().color() == QColor("ivory"):
                current_item.setBackground(QColor("white"))

        # 将当前的背景色设置为红色，如果当前已经是红色，则将其还原为白色
        if item.background().color() == QColor("ivory"):
            item.setBackground(QColor("white"))
        else:
            item.setBackground(QColor("ivory"))
            imagePath = "{}{}{}".format("./images/", column, ".jpg")
            self.right_label.setPixmap(QPixmap(imagePath).scaled(self.right_label.size(), aspectMode=Qt.KeepAspectRatio))
            self.right_label.repaint()
            self.center_label.setPixmap(QPixmap(imagePath).scaled(self.center_label.size(), aspectMode=Qt.KeepAspectRatio))
            self.center_label.repaint()

    def show_menu_clicked(self, pos): # 右击列表，弹出菜单删除某行
        # 当在一个项上右击时显示菜单栏
        item = self.left_widget.itemAt(pos)
        if item:
            menu = QMenu()
            delete_action = QAction("删除", self.left_widget)
            delete_action.triggered.connect(lambda: self.left_widget.takeItem(self.left_widget.row(item)))
            menu.addAction(delete_action)
            menu.exec_(self.left_widget.mapToGlobal(pos))


class DetailPage(QMainWindow):
    detail_signal = Signal(str)
    def __init__(self):
        super().__init__()
        
        # 中心控件
        self.detail_widget = QWidget()
        # 窗口上部分按钮组
        self.top_detail_widget = TopDetailWidget()
        # 窗口下部分内容
        self.content_detail_widget = ContentDetailWidget()
        self.detail_widget.setStyleSheet("background: pink;")
        # self.content_detail_widget.inner_detail_signal.connect(self.switch_detail_page)

        self.setup_ui()

        # 设置样式
        self.setStyleSheet(CommonHelper.read_file("qss/app.qss"))

        # 信号与槽函数
        self.top_detail_widget.inner_detail_signal.connect(self.switch_home_page)

    def setup_ui(self):
        # 中心控件布局 分为上下两部分
        detail_layout = QVBoxLayout()
        detail_layout.setContentsMargins(0, 0, 0, 0)
        detail_layout.setSpacing(0)

        # 添加控件
        detail_layout.addWidget(self.top_detail_widget)
        detail_layout.addWidget(self.content_detail_widget)

        # 设置中心控件布局
        self.detail_widget.setLayout(detail_layout)

        # 设置中心控件
        self.setCentralWidget(self.detail_widget)

    def switch_home_page(self): # 从详情页跳转主页
        self.detail_signal.emit("detailPage")