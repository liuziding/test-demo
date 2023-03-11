import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget
from homePage import HomePage
from detailPage import DetailPage

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个stacked窗口
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 创建主页和详情页
        self.homePage = HomePage()
        self.detailPage = DetailPage()
        
        # 把页面添加到stacked窗口里面
        self.stacked_widget.addWidget(self.homePage)
        self.stacked_widget.addWidget(self.detailPage)
        
        # 从主页跳转详情页
        self.homePage.home_signal.connect(self.switch_page)
        # 从详情页跳转主页
        self.detailPage.detail_signal.connect(self.switch_page)

    def switch_page(self, currentWidget):
        if currentWidget == "homePage":
            # 跳转详情页
            self.setWindowTitle("详情窗口")
            self.stacked_widget.setCurrentWidget(self.detailPage)
        else:
            # 跳转主页
            self.setWindowTitle("主窗口")
            self.stacked_widget.setCurrentWidget(self.homePage)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.setWindowTitle("主窗口")
    window.show()
    sys.exit(app.exec())
