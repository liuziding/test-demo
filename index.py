import sys

from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication

from homePage import HomePage
from detailPage import DetailPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.resize(1200, 800) # 设置窗口大小
        self.center() # 第一次打开窗口在电脑屏幕正中间
        self.setup_ui()

    def setup_ui(self):
        # 创建QWidget对象
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.switch_page("detailPage")

    def switch_page(self, currentWidget): # 切换窗口
        # 循环删除所有子窗口
        while self.stacked_widget.count() > 0:
            widget = self.stacked_widget.widget(0)
            self.stacked_widget.removeWidget(widget)
            widget.deleteLater()
        if currentWidget == "homePage":
            # 跳转详情页
            self.setWindowTitle("详情窗口")
            self.detailPage = DetailPage()
            # 把页面添加到stacked窗口里面
            self.stacked_widget.addWidget(self.detailPage)
            # 从详情页跳转主页
            self.detailPage.detail_signal.connect(self.switch_page)
            # self.stacked_widget.setCurrentWidget(self.detailPage)
        else:
            # 跳转主页
            self.setWindowTitle("主窗口")
            self.homePage = HomePage()
            # 把页面添加到stacked窗口里面
            self.stacked_widget.addWidget(self.homePage)
            # 从详情页跳转主页
            self.homePage.home_signal.connect(self.switch_page)

    def center(self): 
        # 获取当前屏幕的尺寸和位置
        screen = QGuiApplication.screens()[0].availableGeometry()
        # 获取窗口的尺寸和位置
        size = self.geometry()
        # 计算窗口居中的位置
        x = (screen.width() - size.width()) / 2
        y = (screen.height() - size.height()) / 2
        # 移动窗口到居中位置
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())