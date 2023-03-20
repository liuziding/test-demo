from PySide6 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题
        self.setWindowTitle("列表示例")

        # 设置窗口大小
        self.resize(400, 200)

        # 创建列表控件
        self.list_widget = QtWidgets.QListWidget()

        # 创建文本控件
        self.text_edit = QtWidgets.QTextEdit()

        # 创建删除按钮
        self.delete_button = QtWidgets.QPushButton("删除")

        # 设置布局
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QHBoxLayout()
        central_widget.setLayout(layout)

        left_layout = QtWidgets.QVBoxLayout()
        left_layout.addWidget(self.list_widget)
        left_layout.addWidget(self.delete_button)
        layout.addLayout(left_layout)

        layout.addWidget(self.text_edit)

        # 为删除按钮添加点击事件
        self.delete_button.clicked.connect(self.delete_selected_item)

        # 为列表控件添加项和点击事件
        self.list_widget.addItems(["项目1", "项目2", "项目3", "项目2", "项目3", "项目2", "项目3", "项目2", "项目3", "项目2", "项目3", "项目2", "项目3"])
        self.list_widget.itemClicked.connect(self.show_text)

    def show_text(self, item):
        # 在文本控件中显示所选项的文本
        self.text_edit.setText(item.text())

    def delete_selected_item(self):
        # 删除选定的项
        selected_items = self.list_widget.selectedItems()
        for item in selected_items:
            self.list_widget.takeItem(self.list_widget.row(item))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
