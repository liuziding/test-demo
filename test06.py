from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSizePolicy

app = QApplication([])

# 创建一个主窗口和一个垂直布局
window = QMainWindow()
widget = QWidget()
layout = QVBoxLayout(widget)

# 创建第一个小部件，并为其添加样式表和最小高度
widget1 = QWidget()
widget1.setMinimumHeight(200)
widget1.setStyleSheet("border: 2px solid red;")
layout.addWidget(widget1)

# 创建第二个小部件，并为其添加样式表
widget2 = QWidget()
widget2.setStyleSheet("border: 2px solid red;")
layout.addWidget(widget2)

# 将第一个小部件的拉伸因子设置为0，将第二个小部件的拉伸因子设置为1，使其自适应窗口大小
layout.setStretchFactor(widget1, 0)
layout.setStretchFactor(widget2, 1)

# 设置窗口的中心部件为垂直布局中的小部件，并显示窗口
window.setCentralWidget(widget)
window.show()

app.exec()
